# PAN-OS Hello World Example


This skillet will set the hostname of a PAN-OS device. This is purely for example purposes only. The 'device_system.xml'
file will be rendered and inserted into the config at the 'xpath' named in the 'snippets' section of the skillet file.

The hostname of the device will be set to the value entered from the user in the 'Firewall hostname' field. This will 
set a variable called 'FW_NAME', which is then inserted into the 'device_system.xnl' file via jinja templating.  