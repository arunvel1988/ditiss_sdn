#!/bin/bash

# Check if the controller IP is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <controller-ip>"
  exit 1
fi

CONTROLLER_IP=$1

# Update package index
sudo apt-get update -y

# Install Java 8
sudo apt-get install -y openjdk-8-jdk

# Set JAVA_HOME environment variable
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc
echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc

# Verify Java version
java -version

# Download OpenDaylight Karaf distribution
wget https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.5.0-Boron/distribution-karaf-0.5.0-Boron.zip

# Install unzip if not already installed
sudo apt-get install -y unzip

# Unzip the downloaded Karaf distribution
    unzip distribution-karaf-0.5.0-Boron.zip

# Change directory to the Karaf distribution
cd distribution-karaf-0.5.0-Boron

# Start Karaf
./bin/karaf &

# Wait for Karaf to start
sleep 60

# Install necessary OpenDaylight features
./bin/client feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs odl-dlux-all

# Install Mininet if not already installed
sudo apt-get install -y mininet

# Run Mininet with a linear topology of 2 switches
sudo mn --topo linear,2 --mac --controller=remote,ip=$CONTROLLER_IP,port=6633 --switch ovs,protocols=OpenFlow10

# Run pingall to test connectivity
sudo mn -c
sudo mn --topo linear,2 --mac --controller=remote,ip=$CONTROLLER_IP,port=6633 --switch ovs,protocols=OpenFlow10 --test pingall



sudo apt-get update
sudo apt-get install python3-venv

python3 -m venv venv

source venv/bin/activate
pip install requests networkx matplotlib

python3 sdn_basic.py
python3 sdn_visual.py
