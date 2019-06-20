# Skillets

A skillet is just a collection of templates with a bit of meta-data that goes along with them. Meta-data can include things like a 
name for the collection, a type that describes how the templates can be consumed, a description, optional labels, etc.

All skillets can be consumed by [Panhandler](github.com/Paloaltonetworks/panhandler), 
though other apps may exist to consume specific skillets as well. 

## Skillet types

Although most skillets consist of loadable PAN-OS configurations, Panhandler can also load additional types
of Skillets including:

* PAN-OS
* Terraform
* Python
* REST

For more information, see the Panhandler [documentation](panhandler.readthedocs.io).


## Examples

For more example Skillets, visit the 
[Example Skillets Repository](https://github.com/PaloAltoNetworks/Example_Skillets)


## Disclaimer and Support Policy

This template/solution is released under an as-is, best effort, support policy. These scripts should be seen as community 
supported and Palo Alto Networks will contribute our expertise as and when possible. We do not provide technical support or 
help in using or troubleshooting the components of the project through our normal support options such as Palo Alto Networks 
support teams, or ASC (Authorized Support Centers) partners and backline support options. The underlying product used (the VM-
Series firewall) by the scripts or templates are still supported, but the support is only for the product functionality and 
not for help in deploying or using the template or script itself. Unless explicitly tagged, all projects or work posted in our 
GitHub repository (at https://github.com/PaloAltoNetworks) or sites other than our official Downloads page on 
https://support.paloaltonetworks.com are provided under the best effort policy.