//variable "subscription_id" {
//  description = "Azure Subscription Id"
//  default = "0000-0000-0000-0000"
//}
//
//variable "client_id" {
//  description = "Client Id"
//  default = "0000-0000-0000-0000"
//}
//
//variable "client_secret" {
//  description = "Client Secret"
//  default = "0000-0000-0000-0000"
//}
//
//variable "tenant_id" {
//  description = "Tenant Id"
//  default = "0000-0000-0000-0000"
//}

variable "admin_username" {
  description = "PAN-OS NGFW Admin Username"
  default = "admin"
}

variable "admin_password" {
  description = "PAN-OS NGFW Admin Password"
  default = "admin"
}

variable "admin_ssh_key" {
  description = "Admin SSH authorized key"
  default = "admin"
}

variable "resource_group" {
  description = "Resource Group to use to build"
  default = "admin"
}

variable "hostname" {
  description = "Host name of the PA VM-Series"
  default = "pavm"
}

