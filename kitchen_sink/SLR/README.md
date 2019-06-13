# SLR_Bot

SLR Bot exists to help you generate Security Lifecycle Reviews automatically.
This version does require you to enter the username and password for the firewall
that you are running the SLR against when the script is run. This can be modified
as needed.



The configuration file ('slr.conf') contains the options currently supported by 
the script. These options (and format) are:

PreparedBy:your name<br>
sendTo:recipient1@yourcompany.com<br>
sendTo:recipient2@yourcompany.com<br>
RequestedBy:requestor@yourcompany.com<br>
cspKey:your_csp_Key


<br><br><br>

You can have up to 20 sendTo recipients per SLR request. In case you would like
to modify the script to include the other supported parameters, the complete list
is:


1.	AccountName - (if null/empty will be default to Salesforce Account Name based on license key)
2.	Industry - (if null/empty will be default to Salesforce Account Industry)
3.	Country - (if null/empty will be default to Salesforce Account Billing Country)
4.	GeographicRegion - (if null/empty will be default to Salesforce Account Theatre)
5.	DeploymentLocation - (if null/empty will be default to "Perimeter/Internet Gateway")
6.	Language - (if null/empty will be default to "English")
7.	PreparedBy - (if not null or not empty will be displayed on report cover page)
8.	files *
9.	EmailIdList * (multiple email id's comma or ';' separated max 20)
10.	RequestedBy * (multiple email id's comma or ';' separated max 10)
11.	SendReportToRequestor - (by default false true/false)


## Usage

Modify the configuration file to set the options you would like.

To run the script, simply pass the IP address of the firewall that you would like
to run the SLR for using the -f or --firewall option:

"/usr/bin/python slr_bot.py -f 192.168.1.1"



