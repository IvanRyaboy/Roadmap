# Roadmap
# How to Run Project

## Download Codes
```
git clone https://github.com/IvanRyaboy/Roadmap
```
```
cd Roadmap
```

## Build Virtual Environment
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```


## Setup PostgreSQL
Create `dbRoadmap` Database in PostgreSQL and change `USER` `PASSWORD` `HOST` in the `roadmap/setting.py`


## Migrate Models
```
python manage.py makemigrations 
```
```
python manage.py migrate
```

## Add Super User
```
python manage.py createsuperuser
```

## Run Codes
```
python manage.py runserver
```
