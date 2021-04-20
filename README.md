# Service_for_upload_images

 Service_for_upload_images - a service that allows you to download images from a user's computer, or from a link, and then resize them.
The project can be deployed in three Docker containers using docker-compose.

![](schema/schema.PNG)

### How to deploy a project

* Clone the repository to your local machine
* Create file .env and specify parameters
   
```bash
  SECRET_KEY=<укажите secret_key>
  DEBUG_VALUE='FALSE'
```
* Generation SECRET_KEY - you can get by [ссылке](https://djecrety.ir/).
     
### Starting docker-compose
```
docker-compose up --build
```
### First Start
**For the first launch**, for project functionality, go inside to the container:
```
docker exec -t -i <WEB CONTAINER ID> bash
```
**Make migrations**
```
python manage.py migrate
```
**To create a superuser**
```
python manage.py createsuperuser
```

### Tech Stack
* [Python 3.8.5](https://www.python.org/)
* [Django 3.1.4](https://www.djangoproject.com/)
* [Docker](https://www.docker.com/)

### Автор

[Ирина Назарова](https://github.com/Irina-Nazarova)