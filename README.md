# Django-SouthWest-Walkers

pip3 install django gunicorn

pip3 install dj_database_url psycopg2

# To run cloudinary

pip3 install dj3-cloudinary-storage

# To create a requirements.txt

pip3 freeze --local > requirements.txt

# To create a new Django Project

django-admin startproject southwestwalkers .

# To create the app 

python3 manage.py startapp blog

>> This now needs to be added to settings.py in the install apps section add 'blog', to the end

# To migrate these changes

python3 manage.py migrate

# To see these changes have worked

python3 manage.py runserver

>> you will see the little rocket if it worked

# Contents of env.py for now: 

import os

os.environ["DATABASE_URL"] = "postgres://soybsfcfvfpvkf:6f2c9e7d69d9062e9e8a03962d99a49dd196ba9443f113fb5bb194b734fca5e6@ec2-34-242-84-130.eu-west-1.compute.amazonaws.com:5432/d6cqgnjbeo3jng"
os.environ["SECRET_KEY"] = "s@uthwest!84"
os.environ["CLOUDINARY_URL"] = "cloudinary://624189548942148:RmTrYOVf13gQzqCqeo-cJuTy12o@dkzungvzx"

# Allow Multiple Images

https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django


Using AllAuth because there are advantages such as account and password and single sign on with google or facebook 
# https://learndjango.com/tutorials/django-allauth-tutorial


to find the allauth directory

python
help(‘allauth')

cp -r /home/gitpod/.pyenv/versions/3.8.13/lib/python3.8/site-packages/allauth/templates/* templates/allauth/

have to create an allauth folder in the templates folder in the general area. 
