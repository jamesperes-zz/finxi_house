# Finxi House
Project to Finxi

## Versions

### Tags

   - 0.1 - Django only(BETA)

   
  

## Running local server

### Requeriments

   - Python 3
 
   

### Docker
this project is very easy to install and deploy in a Docker container.

```sh
docker-compose build
docker-compose up 
```


### ENV
configure the settings file (finxi_house/settings.py) with your credentials
I used Python-Decouple to read the ENV file
more information in this [link](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html) 

```sh
SECRET_KEY=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
DEBUG=
```

### Runing migrate

for reasons of clean code, you need to run the Django migrate separately
with this

```sh
docker-compose exec web python manage.py migrate
```


### Access to django-admin
when you run the migrate for the first time it will create a user admin

login: admin@admin.com

password: admin1234

### pep8
this project all PEP8 rules have been tested and formatted by [Black] (https://github.com/ambv/black)
