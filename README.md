# portfolioAPI

The following project is a web API which serves data such as informations about projects, bio etc. to the frontend.
It is written in Django REST Framework.

# installation & configuration
In order to get the api working locally, you need to create new django project.
Then, fork the project from repository and paste all files in your new project's directory.
*While in project's root directory, run
`pip install -r requirements.txt`
This will install all unnecessary packages.

In your settings.py:
 - add `rest_framework`, `rest_framework.authtoken`, `base`, `corsheaders`, `django_cleanup.apps.CleanupConfig` app to `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'base',
    'corsheaders',
    'django_cleanup.apps.CleanupConfig',
   ]
   ```
 - add `corsheaders.middleware.CorsMiddleware` as first element of `MIDDLEWARE`:
   ```python
   MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
   ]
   ```
 - add `REST_FRAMEWORK` variable:
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
       ],
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
       'PAGE_SIZE': 10,
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
       ]
   }
   ```
  
- specify urls for `corsheaders`: 
  ```python
   CORS_ORIGIN_WHITELIST = [
     "https://yoururl1.com",
     "https://www.yoururl1.com",
   ]
  ```
  If you want to run it just on local server, you can skip adding `CORS_ORIGIN_WHITELIST` and set `CORS_ALLOW_ALL_ORIGINS` to `True`
 - specify static directories:  
   ```
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
   ]
   STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
   MEDIA_DIR = ''
   ```

After that, in your terminal:
* `python manage.py makemigrations`
and then
* `python manage.py migrate`
finally
* `python manage.py runserver`




   


