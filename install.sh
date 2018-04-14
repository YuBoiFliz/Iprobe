#/bin/bash/
sudo mkdir /etc/iprobe
cd /etc/iprobe
sudo apt-get install -y nikto nmap proxychains tor sqlmap ruby
sudo git clone https://github.com/wpscanteam/wpscan.git
sudo git clone https://github.com/laramies/theHarvester.git
