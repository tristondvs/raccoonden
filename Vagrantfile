
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
# General Vagrant VM configuration.
# config.vm.box = "ansible.box"
config.ssh.insert_key = false
config.vm.synced_folder ".", "/vagrant", disabled: true
config.vm.provider :virtualbox do |v|
v.memory = 514
v.linked_clone = true
end

# Ansible Controller
config.vm.define "cont" do |cont|
cont.vm.box = "bento/ubuntu-20.04"
cont.vm.hostname = "cont.test"
cont.vm.network :private_network, ip: "192.168.2.201"
# Update the local directory below. This will create a local file share with the vagrant box at the specified directory
cont.vm.synced_folder "D:/projects/raccoonden/mountpoint/", "/home/vagrant/ansible"
end
end
