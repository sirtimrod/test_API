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
sudo -u postgres psql -c "alter user postgres with password 'postgres';"
sudo -u postgres psql -c "create database store;"
suso -u postgres psql
# enter sudo password
\c store
create table resources(id serial primary key, title char(8) not null, amount real, measurement char(8) not null, price real, create_at date);

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
```

### Request examples with curl
```bash
# GET request resources
curl -i http://127.0.0.1:5000/resources

# POST request
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"res_1", "amount":32, "measurement":"liter", "price":10, "create_at":"2020-02-12"}' http://127.0.0.1:5000/resources

# UPDATE request
curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"res_2", "amount":157, "measurement":"kg", "price":4, "create_at":"2030-12-11"}' http://127.0.0.1:5000/resources/1

# DELETE request
curl -X DELETE http://127.0.0.1:5000/resources/1

# GET request total_cost
curl -i http://127.0.0.1:5000/total_cost
```
