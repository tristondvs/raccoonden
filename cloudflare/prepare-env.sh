#!/bin/bash
# prepares build/dev environment
# Ubuntu 22.04.1
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-pip
pip install -r requirements.txt

# prepare .env template file
# replace brackets with info obtained from cloudflare dashboard
cat <<EOF > .env
USER_EMAIL='<email for cloudflare login>'
API_KEY='<api key with edit permissions for load balancer settings>'
ZONE_ID='<zone id tied to cloudflare account>'
EOF
