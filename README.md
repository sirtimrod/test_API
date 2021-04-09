# test_API

### Requirements
* Python 3.8+
* PostgreSQL 10+

### Prepare Project Linux
```bash
# install database
sudo apt install postgresql

# add database to autostart
sudo service postgresql enable

# set default password for default database user 
sudo -u postgres -c "alter user postgres with password 'postgres';"
sudo -u postgres -c "create database store;"

# run database
sudo service postgresql start

mkdir ~/API_project && cd ~/API_project
git clone https://github.com/sirtimrod/test_API.git
python3 -m venv test_project
cd test_project
source bin/activate
pip install -r  requirements.txt
```

### Run Project
```bash
sudo service postgresql start

cd ~/API_project/test_project
source bin/activate
python run_server.py

# or run admin-panel
./run_admin.py
```
