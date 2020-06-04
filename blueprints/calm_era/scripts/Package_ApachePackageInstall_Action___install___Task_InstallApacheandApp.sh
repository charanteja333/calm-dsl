
#!/bin/bash
set -ex

# Install python3, httpd and flask
sudo yum -y update
sudo yum -y install epel-release centos-release-scl
sudo yum -y install httpd gcc psacct mod_proxy_uwsgi
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm 
sudo yum -y install git2u-all rh-python36
sudo yum clean all

echo "@@{db_server_cred.secret}@@" | tee ~/.ssh/id_rsa
echo "@@{db_server_cred.public_key}@@" | tee ~/.ssh/id_rsa.pub

sudo chmod 600 ~/.ssh/id_rsa
sudo chmod 644 ~/.ssh/id_rsa.pub

# Init and activate a python-virtualenv with prereqs
GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git clone git@github.com:AmitVasantSalunke/sample-flask-app.git
scl enable rh-python36 "python -m venv /home/centos/sample-flask-app/env"
source /home/centos/sample-flask-app/env/bin/activate && pip install -r /home/centos/sample-flask-app/requirements.txt

## Get Postgres Env vars
echo "export POSTGRES_SERVER='@@{Postgres.address}@@'
export POSTGRES_USER='@@{DB_USER}@@'      
export POSTGRES_PASSWORD='@@{DB_PASSWORD}@@'
export POSTGRES_DATABASE='@@{DB_NAME}@@' " | tee /home/centos/sample-flask-app/config.env

sudo /usr/sbin/setsebool -P httpd_can_network_connect 1

echo "[Unit]
Description=uWSGI server for ntnxdemoapp
After=network.target

[Service]
User=centos
Group=apache
WorkingDirectory=/home/centos/sample-flask-app
Environment='PATH=/home/centos/sample-flask-app/env/bin'
ExecStart=/bin/bash /home/centos/sample-flask-app/start.sh

[Install]
WantedBy=multi-user.target
" | sudo tee /etc/systemd/system/ntnxdemoapp.service

chmod +x /home/centos/sample-flask-app/start.sh

echo "LoadModule proxy_uwsgi_module modules/mod_proxy_uwsgi.so
<VirtualHost *>
    ServerName @@{address}@@
    ProxyPass / uwsgi://127.0.0.1:8000/
</VirtualHost> " | sudo tee -a /etc/httpd/conf/httpd.conf

sudo systemctl enable ntnxdemoapp
sudo systemctl start ntnxdemoapp

sudo systemctl restart httpd
sudo systemctl enable httpd