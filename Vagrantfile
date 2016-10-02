# -*- mode: ruby -*-
# vi: set ft=ruby :
 
VAGRANTFILE_API_VERSION = "2"
 
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 
  # Insertar ubuntu 16 en la maquina virtual
  config.vm.box = "bento/ubuntu-16.04"
  # Redireccionamiento de puertos para luego porbar la web
  config.vm.network "forwarded_port", guest: 80, host: 8080
  # Carpeta compartida para hacer las modificaciones desde la maquina local
  config.vm.synced_folder "htdocs", "/var/www/html"
  config.vm.synced_folder "Ejercicios", "/Ejercicios"
  # configuración de LAMP
  config.vm.provision "shell", path: "config.sh"
  
  config.vm.provider "virtualbox" do |v|
    # Para que tenga entorno visual
	# v.gui = true
	# Cambiar el nombre de la maquina
	v.name = "DAI"
  end
end
