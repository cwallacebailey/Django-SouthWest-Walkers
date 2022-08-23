# South West Walkers

[Please see link to the final project]() (holding ctrl when clicking this link will open it in a new tab)

South West Walkers is a social media blog. 




This site was built using Django as its framework with HTML, CSS, Bootstrap, JavaScript & Python. The database is created using SQL through PostgreSQL.

# The below needs to be updated

![Final project responsive image below]() 


## Contents

* [User Experience](#user-experience)
    * [Opening Discussions](#opening-discussions)
    * [User Stories](#user-stories)
    * [Project Goals](#project-goals)

* [Design](#design)
    * [Colours](#color-scheme)
    * [Typography](#typography)
    * [Wireframe](#wireframes)
    * [Features](#features)
    * [Future Features](#future-features)
    * [Navigation bar](#navigation-bar)
    * [Footer](#footer)

* [Database](#database)

* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Workspace](#workspace)
    * [Version Control](#version-control)
    * [Responsive Design](#responsive-design)
    * [Documentation](#documentation)
    * [Site Design](#site-design)
    * [Database Design](#database-design)
    * [Frameworks, Libraries and Others](#frameworks-libraries-and-others)

* [How to Deploy](#how-to-deploy)

* [Testing](#testing)
    * [Solved Bugs](#solved-bugs)
    * [Known Bugs](#known-bugs)

* [Credits](#credits)
    * [Code](#code)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

## User Experience
[Back to contents](#contents)

### Initial Discussion
[Back to contents](#contents)

### User Stories
[Back to contents](#contents)

### Project Goals
[Back to contents](#contents)

---

## Design
[Back to contents](#contents)

### Color Scheme
[Back to contents](#contents)

### Typography
[Back to contents](#contents)

### Imagery
[Back to contents](#contents)

### Wireframes
[Back to contents](#contents)

### Features
[Back to contents](#contents)

#### Create a user profile
[Back to contents](#contents)

#### Navigation bar

The navigation bar changes depending on user status and screen size:
[Back to contents](#contents)

### Future Features
[Back to contents](#contents)

### Defensive Design
[Back to contents](#contents)

## Database Design
[Back to contents](#contents)

## Technologies Used
[Back to contents](#contents)

### Languages Used

#### HTML

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

#### CSS

* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)

#### JavaScript

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* This project uses JavaScript ES6 and jQuery.

#### Python

* [Python](https://www.python.org/)
* This project uses Python 3.8.11.

### Workspace

#### GitPod

[GitPod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.

### Version Control

#### Git

[Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.

#### GitHub

[GitHub](https://github.com/) is used to store the code for this project after being pushed from Git.

### Wireframing

#### Balsamiq

[Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.

[Back to contents](#contents)

---

### Responsive Design

#### Am I Responsive Design

[Am I Responsive Design](http://ami.responsivedesign.is/#) was used to check the responsive design of the site, and to create the final site image.

[Back to contents](#contents)

---

### Site Design

#### Font Awesome

[Font Awesome](https://fontawesome.com/) was used on all pages to add the icons.

#### Google Fonts

[Google Fonts](https://fonts.google.com/) was used to select all the fonts on the site.

#### Favicon.io

[favicon.io](https://favicon.io/) used to create a site favicon.

### Packages

| Name | Purpose |
|------|---------|
| Django | Framework |
| Flake-8 | Syntax |
| Pylint | Syntax |
| Pillow | Images |
| django-allauth | Authentication |
| Stripe | Secure Payment Services |
| Boto3 | AWS Management |
| django-storages | Custom Storage Backends |
| django-countries | Country Form Field |
| python-magic | Audio Form Field |
| gunicorn | WSGI HTTP Server |
| django-crispy-forms | Front End Form Rendering |
| dj-database-url | Database Configuration |
| psycopg2-binary | PostgreSQL DB Adaptor |
| coverage | Test Coverage |
| travis.ci | Testing |
| | |

[Back to contents](#contents)

---

## Hosting

#### Heroku

[Heroku](https://www.heroku.com) was used to deploy the live site.

### Frameworks, Libraries, and Others

#### Google DevTools

[Google DevTools]() was used to help find what code correlated to which feature.

#### Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to ensure that the code was as performant as possible, conforming to best practices, and SEO and Accessibility guidelines.

#### WebPageTest

#### Bootstrap

[Bootstrap](https://getbootstrap.com/) was used 

## Deployment

[Please click here for all Deployment steps and requirements](static/docs/DEPLOYMENT.md).

[Back to contents](#contents)

---

## Testing

### Solved Bugs

### Known Bugs


## Credits

### Code

* [Font Awesome](https://fontawesome.com/): Library of icons used for social media and download links.
* This website was made with the help of the tutorials from Code institute for the 
* [Django Documentation](https://docs.djangoproject.com/en/3.2/) has been used to ensure correct syntax usage throughout the code.
* [Stack Overflow](https://stackoverflow.com/) has been used to help with deciphering the django error codes, and searching for bug fixes.
* 
* 
* 


























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

to add dropdown to form for region

https://thewebdev.info/2022/04/05/how-to-create-a-dropdown-in-python-django-model-form/#:~:text=To%20create%20a%20dropdown%20in%20Python%20Django%20model%20form%2C%20we,the%20model%20for%20the%20form.&text=to%20add%20the%20color%20field%20to%20the%20MyModel%20model%20class.



List of all the hills in the mendips

https://peakvisor.com/park/mendip-hills-aonb.html


Add summernote to blog post creation
https://github.com/summernote/django-summernote


Image: 

https://www.pexels.com/photo/brown-and-green-mountains-under-white-sky-10874914/