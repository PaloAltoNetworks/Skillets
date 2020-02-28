data "azurerm_public_ip" "pavm_public_ip_address_data" {
  name                = "${azurerm_public_ip.pavm_public_ip.name}"
  resource_group_name = "${azurerm_virtual_machine.pavm.resource_group_name}"
}

output "pavm_public_ip_address" {
  value = "${data.azurerm_public_ip.pavm_public_ip_address_data.ip_address}"
}
