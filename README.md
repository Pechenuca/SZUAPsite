# szuap

## backend

### Project setup
```
pip install -r requirements.txt
```

### Migrations
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Start app
```
python manage.py runserver
```

## frontend

### Project setup
```
yarn install
```

#### Compiles and hot-reloads for development
```
yarn serve
```

#### Compiles and minifies for production
```
yarn build
```

#### Lints and fixes files
```
yarn lint
```

#### docker 

0. Uncomment
frontend: 
```
src/vuex/store.js getters:
baseUrl: state => {
    //return state.backendBaseUrlDev
      return state.backendBaseUrlProd
}
```

backend: 
```
SZUAPsite/settings.py:
# DATABASES = {
#     'default': {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

1. Create .env for django like this:
```
DEBUG=0
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 
```

2. create static files for django 
```
docker-compose exec backend python manage.py collectstatic
```

3. create superuser
```
docker-compose exec backend python manage.py createsuperuser
```

