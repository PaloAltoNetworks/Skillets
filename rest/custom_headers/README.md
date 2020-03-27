# REST Example with custom headers and output capturing

Rest Skillets can be used to issues calls to REST based APIs. This example gathers some information from your
Prisma Access Cloud instance using a provided API-KEY.

## Variables 

In this example, we only use the api_key variable:

* api_key

## Snippets

This example uses the 'headers' attribute to set the 'header-api-key' custom header. This is required for Prisma Access
REST API calls. It also uses output capturing to parse out the values we are particular interested in. This API 
calls returns JSON data, so the output_type is set to 'json'. We can then use 'capture_pattern' to use json_path 
expressions to parse the values we can about. Each entry in the 'outputs' list will set a variable in the context
with the corresponding name. 

```yaml

snippets:
  - name: Retrieve Remote Network Service IP from Prisma Access
    path: https://api.gpcloudservice.com/getAddrList/latest?fwType=gpcs_remote_network&addrType=public_ip
    operation: GET
    headers:
      header-api-key: '{{ api_key }}'
    output_type: json
    outputs:
      - name: status
        capture_pattern: $.status
      - name: fwType
        capture_pattern: $.result.fwType
      - name: addrList
        capture_pattern: $.result.addrList

```

