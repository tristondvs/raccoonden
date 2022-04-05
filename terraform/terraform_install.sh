#!/bin/bash
## terraform install bash script
## will make ansible role later
#add gpg keys
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
#add hashicorp package repo
sudo apt-add-repository "deb [arch=$(dpkg --print-architecture)] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
#invoke apt and install terraform
sudo apt update && sudo apt install terraform
#confirm terraform installation
terraform -v
