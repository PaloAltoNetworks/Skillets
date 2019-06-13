#!/usr/bin/python3

import argparse
import os
import sys
import xml.etree.ElementTree as et
from time import sleep

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


def readOpts():
    """Reads options from configuration file"""
    opts_dict = dict()
    opts_dict['EmailIdList'] = []
    opts_file = open('./slr.conf', 'r')
    for line in opts_file:
        line = line.strip("\n")
        line = line.split(":")
        if line[0] == "sendTo":
            opts_dict['EmailIdList'].append(line[1])
        else:
            opts_dict[line[0]] = line[1]
    if len(opts_dict['EmailIdList']) > 20:
        print("Maximum number of recipients is 20. Please remove 'sendTo' entries" \
              " in the configuration file until this criteria is met. Exiting now.")
        exit(1)
    return opts_dict


def getKey(dev_IP, user, passwd):
    """Retrieves an API key from the porvided firewall"""
    key_params = {"type": "keygen",
                  "user": user,
                  "password": passwd}
    key_req = requests.get("https://{}/api/?".format(dev_IP), params=key_params, verify=False)
    key_xml = et.fromstring(key_req.content)
    api_key = key_xml.find('./result/key').text
    return api_key


def genStats(dev_ip, panos_key):
    """Issues call to the firewall to generate a stats dump"""
    stat_params = {"type": "export",
                   "category": "stats-dump",
                   "key": panos_key}
    stats_req = requests.get("https://{}/api/?".format(dev_ip), params=stat_params, verify=False)
    if stats_req.status_code != 200:
        print("Request to generate stats dump failed. Exiting now.")
        exit(1)
    stats_xml = et.fromstring(stats_req.content)
    job_id = stats_xml.find('./result/job').text
    job_result = jobChecker(dev_ip, panos_key, job_id)
    if job_result != "OK":
        print("There was an issue with generating the statsdump. Please check " \
              "the device.")
    return job_id


def jobChecker(dev_ip, panos_key, job_id):
    """Checks the status of the job that is passed in."""
    cmd = "<show><jobs><id>{}</id></jobs></show>".format(job_id)
    status_params = {"type": "op",
                     "cmd": cmd,
                     "key": panos_key}
    status = ""
    while status != "FIN":
        status_req = requests.get("https://{}/api/?".format(dev_ip), params=status_params, verify=False)
        if status_req.status_code != 200:
            print("Request to check job status failed. Please log into device and " \
                  "download the stats dump manually. Exiting now.")
            print(status_req)
            print(status_req.text)
            exit(1)
        status_xml = et.fromstring(status_req.content)
        status = status_xml.find('./result/job/status').text
        result = status_xml.find('./result/job/result').text
        if result == "PEND":
            progress = status_xml.find('./result/job/progress').text
            print("Stats dump job progress: {}%".format(progress))
        sleep(5)
    print('stats dump file creation complete')
    return result


def downloadStats(dev_ip, panos_key, job_id):
    """Downloads the statsdump file"""
    stats_file = "stats_dump.tar.gz"
    dl_params = {"type": "export",
                 "category": "stats-dump",
                 "action": "get",
                 "job-id": job_id,
                 "key": panos_key}
    dl_req = requests.get("https://{}/api/?".format(dev_ip), params=dl_params, stream=True, verify=False)
    print('downloading stats dump file')
    with open(stats_file, 'wb') as f:
        for chunk in dl_req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return stats_file


def submitStats(file_name, opts):
    """Test function to submit stats dump for SLR generation"""
    file1 = open(file_name, 'rb')
    url = "https://riskreport.paloaltonetworks.com/API/v1/Create"
    headers = {"apiKey": opts['cspKey']}
    file = {"file1": ('stats_dump.tar.gz', file1, 'application/gzip')}
    payload = {"EmailIdList": ",".join(opts['EmailIdList']),
               "RequestedBy": opts["RequestedBy"],
               "PreparedBy": opts['PreparedBy']}
    print('uploading stats file and SLR parameters')
    slr_req = requests.post(url, headers=headers, data=payload, files=file)
    if slr_req.status_code != 200:
        print("There was an issue submitting the stats dump:\n".format(slr_req.content))
        print(slr_req)
        print(slr_req.text)
        exit(1)
    print(slr_req.content)
    print("Cleaning up stats dump.")
    os.remove(file_name)


def main():
    # python skillets currently use CLI arguments to get input from the operator / user. Each argparse argument long
    # name must match a variable in the .meta-cnc file directly
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--firewall", help="IP address of the firewall to pull the stats dump from", type=str)
    parser.add_argument("-u", "--username", help="Firewall Username", type=str)
    parser.add_argument("-p", "--password", help="Firewall Password", type=str)
    parser.add_argument("-a", "--support_api_key", help="Support Portal API Key", type=str)
    parser.add_argument("-e", "--email", help="Email Address to send the SLR", type=str)
    parser.add_argument("-r", "--requester_email", help="Email of SLR Requester", type=str)
    parser.add_argument("-b", "--prepared_by", help="Name to use as prepared by field", type=str)
    args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_help()
        parser.exit()
        exit(1)
    fw_ip = args.firewall
    username = args.username
    password = args.password
    requester = args.requester_email
    prepared_by = args.prepared_by
    support_api_key = args.support_api_key
    emails = args.email
    email_list = list()
    if ',' in emails:
        email_list.extend(emails.split(','))
    else:
        email_list.append(emails)
    options = {
        "EmailIdList": email_list,
        "RequestedBy": requester,
        "PreparedBy": prepared_by,
        "cspKey": support_api_key
    }
    key = getKey(fw_ip, username, password)
    job_key = genStats(fw_ip, key)
    stats_file = downloadStats(fw_ip, key, job_key)
    submitStats(stats_file, options)
    print('SLR creation complete. Check email provided for full report.')


if __name__ == '__main__':
    main()
