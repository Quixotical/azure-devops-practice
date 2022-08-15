terraform {
  backend "azurerm" {
    resource_group_name  = "tf_res_blobstore"
    storage_account_name = "quixoticalterraformstate"
    container_name       = "tfstate"
    key                  = "terraform.state"
  }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.15.0"
    }
  }
}

provider "azurerm" {
  features {

  }
}

resource "azurerm_resource_group" "test_group" {
  name     = "tfresgroup"
  location = "switzerlandnorth"
}

resource "azurerm_container_group" "tfcg_test" {
  name                = "weatherapi"
  location            = azurerm_resource_group.test_group.location
  resource_group_name = azurerm_resource_group.test_group.name

  ip_address_type = "Public"
  dns_name_label  = "quixoticalweatherapi"
  os_type         = "Linux"

  container {
    name   = "weatherapi"
    image  = "quixotical/weatherapi"
    cpu    = "1"
    memory = "1"

    ports {
      port     = 80
      protocol = "TCP"
    }
  }
}