## Initial Deployment
Below the steps to to deploy the site to Heroku are outlined with console commands needed to initiate the processes steps

### Create repository:

Create a new repository in GitHub or clone it using the below: 

Note - If you are cloning the project, non pip installs are required. Instead a shorter method can be followed by entering the below command to install all the required libraries/packages at once:

  * pip install -r requirements.txt

Its important to note that if developing on your local device, the virtual environment must be set up as the first step, followed by loading the the requirements.txt. 

#### Set the workspace up:

1. Install Django and gunicorn

  * Terminal Command - pip3 install django gunicorn

2. Install the supporting libraries 

  * Terminal Command for psycopg2 - pip3 install dj_database_url psycopg2
  * Terminal Command for cloudinary - pip install dj3-cloudinary-storage

3. Create requirements.txt:

  * Terminal Command - pip freeze --local > requirements.txt

4. Create a new Django Project

  * Terminal Command - django-admin startproject southwestwalkers 

Note southwestwalkers is my project name. You can insert any project name you like here. 

5. To create the app 

  * Terminal Command - python3 manage.py startapp blog

Note blog is my app name. You can insert any name you like here. 

6. Add this app to the list of installed apps in setting.py. This needs to be added in the install apps section, add 'blog' or your project name, to the end.

7. Migrate changes:

  * Terminal Command to migrate - python manage.py migrate

8. To see these changes have worked

  * Terminal Command to run project - python3 manage.py runserver

Note a successfull run will show the little rocket aka the Django success page

#### Create Heroku App:

The below works on the assumption that you already have an account with Heroku and are signed in. If you do not create an account in the normal way for any site. 

1. Create a new Heroku app:

In the top right corner of the landing page click "New", then hit "Create new app."

2. The app requires a unique name as this will be used in the URL
3. Select the nearest location to you
4. Add your Database to your Heroku app

  * Head to the Resources tab of the app dashboard. Under heading for "Add ons," search for and select "Heroku Postgres"
  * Select what applies to you, here its probably "Hobby Dev - Free" from the plan name drop-down menu.
  * Click "Submit Order Form"

5. From the editor, head to your projects settings.py file, copy the SECRET_KEY variable and add this to the same name variable in the Heroku App's "config vars" where the left box will read variable key
6. Directly beneath the config vars (variable VALUE) = Value copied from settings.py in project.


#### Creating Environmental Variables Locally:

1. Install env package:

Terminal Command to run project - pip install python-dotenv

2. env.py file requirements:

  * The Heroku app settings tab will have items required to be entered into your env.py file.
  * Click "reveal config vars" and copy the variable DATABASE_URL "value". 
  * Add this value to a variable called DATABASE_URL in your create .env file:

  * DATABASE_URL= Paste the value from heroku here
  * From the settings.py file, copy the SECRET_KEY value assign it the variable SECRET_KEY in env.py
  * Add CLOUDINARY_URL variable to .env file:
    1. Log into cloudinary and from the dashboard copy the API Environmental Variable.
    2. Add to .env file
  * Add the port, will be 8000. 

Example for all fields below: 

    import os

    os.environ["DATABASE_URL"] = "postgres://owumvojxztoygj:1d34f431bec69f9c4500a5b26e3bc3b88abeafe442fa00d3e3c4d7baf5c1cac3@ec2-52-208-164-5.eu-west-1.compute.amazonaws.com:5432/dcs6efs2v9m73e"
    os.environ["SECRET_KEY"] = "s@uthwest!94"
    os.environ["CLOUDINARY_URL"] = "cloudinary://914791143219863:8e67DEooJ6CYPWJM9gnMcBM2tXg@dg0zmsaoc"
    os.environ["PORT"]="8000"

#### Settings.py file

1. Setting up settings.py File:

The below code should go at the top of your settings.py:

    import os
    from pathlib import Path

    import dj_database_url
    if os.path.isfile('env.py'):  # This prevents an import error if env does not exist
        import env
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

2. Remove the value from setting.py DATABASES section to be replaced with the below to link the Heroku Postgres server:

    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

3. Add Cloudinary libraries to the installed apps section of settings.py file:

 INSTALLED_APPS = [
  'cloudinary_storage',
  'django.contrib.staticfiles',
  'cloudinary',
]

4. Django should then use Cloudinary for media and static files storage:

  Static files (CSS, JavaScript, Images)
  https://docs.djangoproject.com/en/4.0/howto/static-files/

  STATIC_URL = 'static/'
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

  MEDIA_URL = '/media/'
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

5. Under BASE_DIR, link in Heroku:

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

6. Add allowed hosts:

ALLOWED_HOSTS = ['south-west-walkers.herokuapp.com', 'localhost']

7. Create Procfile at the top level of the file structure and insert the following:

8. Commit and push the code to the GitHub Repository.

  * Terminal Command - git add .
  * Terminal Command - git commit -m "write whatever you like here that is meaningful to you and others who may see your code"
  * Terminal Command - git push


### Cloning on a Local machine

Head to the GitHub repository then follow the steps below to clone the project:

1. Gitpod requires you to have the web extension installed. From here click the green Gitpod button from the main page of the repository. 
2. Install the requirements listed in requirements.txt 

  * Terminal command - pip3 install -r requirements.txt

3. Create your .env file.
4. Run the server

  * Terminal command - python mange.py runserver

