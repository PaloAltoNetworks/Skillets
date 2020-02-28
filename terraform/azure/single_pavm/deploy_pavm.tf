# Configure the Microsoft Azure Provider
provider "azurerm" {
}

# Create a resource group if it doesn’t exist
resource "azurerm_resource_group" "panhandler" {
  name = "${var.resource_group}"
  location = "eastus"

  tags {
    environment = "test"
  }
}

resource "azurerm_public_ip" "pavm_public_ip" {
  name = "pavm_public_ip"
  location = "eastus"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"
//  public_ip_address_allocation = "Dynamic"
  allocation_method = "Dynamic"

  tags {
    environment = "test"
  }
}

# Create Network Security Group and rule
resource "azurerm_network_security_group" "panhander_security_group" {
  name = "panhandher_single_pavm_sg"
  location = "eastus"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"

  security_rule {
    name = "SSH"
    priority = 1001
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"
    source_port_range = "*"
    destination_port_range = "22"
    source_address_prefix = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name = "HTTPS"
    priority = 1100
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"
    source_port_range = "*"
    destination_port_range = "443"
    source_address_prefix = "*"
    destination_address_prefix = "*"
  }

  tags {
    environment = "test"
  }
}

resource "azurerm_virtual_network" "vn_10_5_0_0" {
  name = "myVnet"
  address_space = [
    "10.5.0.0/16"]
  location = "eastus"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"

  tags {
    environment = "test"
  }
}

# Create subnet
resource "azurerm_subnet" "subnet_10_5_0_0" {
  name = "vsubnet0"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"
  virtual_network_name = "${azurerm_virtual_network.vn_10_5_0_0.name}"
  address_prefix = "10.5.0.0/24"
}

resource "azurerm_subnet_network_security_group_association" "vsubnet0" {
  subnet_id = "${azurerm_subnet.subnet_10_5_0_0.id}"
  network_security_group_id = "${azurerm_network_security_group.panhander_security_group.id}"
}

# Create network interface
resource "azurerm_network_interface" "pavm-mgmt-nic" {
  name = "pavm-mgmt-nic"
  location = "eastus"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"
  //    network_security_group_id = "${azurerm_network_security_group.myterraformnsg.id}"

  ip_configuration {
    name = "pavm-mgmt-nic_config"
    subnet_id = "${azurerm_subnet.subnet_10_5_0_0.id}"
    private_ip_address_allocation = "Static"
    private_ip_address = "10.5.0.5"
    public_ip_address_id = "${azurerm_public_ip.pavm_public_ip.id}"

  }

  tags {
    environment = "test"
  }
}

# Generate random text for a unique storage account name
resource "random_id" "randomId" {
  keepers = {
    # Generate a new ID only when a new resource group is defined
    resource_group = "${azurerm_resource_group.panhandler.name}"
  }

  byte_length = 8
}

# Create storage account for boot diagnostics
resource "azurerm_storage_account" "panhandler_storage_ac" {
  name = "diag${random_id.randomId.hex}"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"
  location = "eastus"
  account_tier = "Standard"
  account_replication_type = "LRS"

  tags {
    environment = "test"
  }
}

resource "azurerm_virtual_machine" "pavm" {
  name = "${var.hostname}"
  location = "eastus"
  resource_group_name = "${azurerm_resource_group.panhandler.name}"
  vm_size = "Standard_D3_v2"

  depends_on = [
    "azurerm_network_interface.pavm-mgmt-nic"
  ]
  plan {
    name = "bundle2"
    publisher = "paloaltonetworks"
    product = "vmseries1"
  }

  storage_image_reference {
    publisher = "paloaltonetworks"
    offer = "vmseries1"
    sku = "bundle2"
    version = "latest"
  }

  storage_os_disk {
    name = "${var.hostname}-osdisk"
    vhd_uri = "${azurerm_storage_account.panhandler_storage_ac.primary_blob_endpoint}vhds/${var.hostname}.vhd"
    caching = "ReadWrite"
    create_option = "FromImage"
  }

  //  storage_data_disk {
  //    name = "config_drive"
  //    create_option = "attach"
  //  }

  os_profile {
    computer_name = "${var.hostname}"
    admin_username = "${var.admin_username}"
    admin_password = "${var.admin_password}"
  }

  primary_network_interface_id = "${azurerm_network_interface.pavm-mgmt-nic.id}"
  network_interface_ids = [
    "${azurerm_network_interface.pavm-mgmt-nic.id}"
  ]

  os_profile_linux_config {
    disable_password_authentication = false
  }
}
