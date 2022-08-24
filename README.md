# South West Walkers

[Please see link to the final project]() (holding ctrl when clicking this link will open it in a new tab)

South West Walkers is django built blog to record treks in the brecon beacons. It gamify's hiking allowing users to 'collect' peaks and achievements by walking distance challenges and climbing different mountains in the region. 

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

### Site aims

While strava exists to map peoples runs and walks, it tracks time, distance and the route. It then offers medals for speed of each segments. It does not, however, reward reaching the peaks of mountains in certain ranges and as mountain peaks are usually reached by walking / hiking the medal system in strava is not as rewarding to hikers who would never travel fast. 

All trails and kamoot offers fantastic hiking routes but do not track which you have completed. They also do not reward reaching the peaks of trails and mountains. 

Hiking is a fantastic way to lose weight and improve your mental health, to spend time with friends and family. By 'gamifying' it more people would hike and learn to love a great sport that people of all ages can take part in. 

This site aims to allow users to track walks / hikes which they have completed, the peaks they reached on this walk, the distance travelled and meters climbed. This is stored in a database which then shows on the users profile which peaks they have to reach, those they've completed and achievements they have... achieved. This will be for the brecon beacons, a mountain range in south wales with an aim to expand to all ranges as soon as I have learnt the skills necessary to do this. 

### Initial Discussion 

* I wanted to create a website linked to a database, which is able to authenticate a user by having them log in. 
* The site would allow users to track which Cairns (aka hill / mountain) peaks they have climbed. To offer challenges for hiking distances and reached a number of peaks in the area and to allow other details of the walk such as notes on how it felt and images of the walk to inspire others to get out there and hike. 
* This would be tracked through the user making posts similar to strava (though without mapping / user tracking abilities as this would be outside of the course material) where they record a walk they had done
* I wanted to be able to add, edit and delete posts, to comment and like others and your own posts. 
* I want the user to have a profile which tracks their progress, shows their posts, their progress and achievements. 

[Back to contents](#contents)

### User Stories

* As an Admin I should be able to:
    * Log into a user interface so that I can easily manage the database/s
    * Filter and search models data from the admin page to easily find posts / profiles and delete them if necessary
    * Navigate the admin panel with relative ease to view, search, add and delete posts and or profiles if needs be.
    * Users will be able to comment. If offensive the admin should be able to delete the comment

* The project will require authentication. An un-authenticated user will be able to: 
    * Immediately understand the sites purpose to see if is to their taste and if they want to register
    * Create / register for an account to be able to post and build their profile
    * Browse posts of all users and look at detail only (no comments or likes)

* A register & logged in user will be able to: 
    * Create posts and record peaks / cairns reached, distance walked and meters climbed, edit and delete their own previously created posts
    * Comment on their own and others posts
    * Like or "star" posts to show they are impressed 
    * View their profile where they can add social media links and a profile picture, view progress towards climbing the regions hills and achievements they've completed. 
    * access a detailed guide or 'tips' on how each page can and should be used. 
    
* Any user of the site will get to: 
    * Be met with an enjoyable colour scheme and uniform site style in order for the entire site to stimulate a positive response.
    * Enjoy the site from any screen size (within reason)
    * Follow smooth navigation or, in theory, type in a URL in order to reach a page of the site
    * See a guide for how each page should be used

* User Stories dropped as part of the agile process
    * Create an interactive map showing the location of peaks / cairns to be climbed and if they have or have not been climbed yet
    * View and connect with other users profiles

[Back to contents](#contents)

---

## Design

### Color Scheme

I went with a Scandanavian vibe for the sites colours which have been used throughout the site. 

![Color scheme](static/media/site_colours.png)

[Back to contents](#contents)

### Typography

Two fonts were used for this project, 'Uchen' from google fonts and where this would not work, sans-serif takes over. Sans-serif fonts are easy to read for people with dyslexia and partially visually impaired users. 'Ulchen' is also very easily read. 

[Back to contents](#contents)

### Imagery
[Back to contents](#contents)

### Wireframes
[Back to contents](#contents)

### Features
[Back to contents](#contents)

#### Navigation bar

The navigation bar changes depending on user status and screen size and allows the user to easily login, sign up and logout. The can access all key areas of the site through the nav bar which appears on each page. If logged with a profile created in this includes:

* Home - shows the blogs posts which can be clicked through to see the detailed views
* About - gives an overview of the sites purpose
* Tips - This changes depending on the page the user is viewing or if they are logged in or not
* Logout - allows user to logout
* Profile - view the users profile, created 

![Full Navigation Bar](static/media/navbar_full.png)

If the user is logged in with no profile instead of a link to profile they see "Create Profile" instead:

![Full Navigation Bar No Profile](static/media/nav_bar_no_profile.png)

If not logged in / a new user with no account: 

* Home - as described above
* About - as described above
* Tips - as described above, as not logged in this will always prompt the user to sign up or sign in. 
* Login - allows user to login
* Sign Up - allows the user to create an account

![Full Navigation Bar Not Logged In](static/media/nav_bar_not_logged_in.png)

When viewed on a smaller screen, such as a phone, the navbar compresses to look like the below:

![Truncated Navigation Bar](static/media/nav_bar_compressed.png)

The Navbar shows the site logo, which is also a link to home. On the footer a hiker is included, this was excluded on the nav bar due to the additional space it took up which made the site look less neat. 

![Site Logo from Footer](static/media/site_logo.png)

[Back to contents](#contents)

### All Auth

#### Sign Up

If a user is new to the sign they have the option to sign up. This uses allauth so I wont go into a huge amount of detail however when the user 

![Sign Up](static/media/sign_up.png)

If the username has already been taken the form refreshes and the user is asked to pick another one. 

![Sign Up Check Username](static/media/signup_check_user.png)

If the password is not deemed strong enough the user will see the below: 

![Sign Up Check Password](static/media/site_check.png)

#### Login

If the user has an account already they are able to sign in, they can even select "remember me" on the login page. If they enter a password that is incorrect they get the error message seen below:  

![Login Check Password](static/media/sign_in_check.png)

Once they have logged in they will be met by a message to confirm they have logged in as they are redirected to the home page

![Login message](static/media/logged_in_message.png)

#### Logout

If the user is logged in they are able to logout through the link in the nav bar and the footer. They will be met with the page below

![Sign Out page](static/media/sign_out_page.png)

Once signed out they will be redirected to the home page and see the message below: 

![Sign Out message](static/media/sign_out.png)

#### Create a user profile

Once a user has signed in they are able to create a profile using the link in the navbar. They are taken to the page below: 

![Create Profile Page](static/media/create_profile_page.png)

The only section of this form that has to be completed is the display name. If the user tries to update their profile without one they will be met with the message below: 

![Create Profile Page](static/media/create_profile_display_name_check.png)

To prevent the user putting sordid or incorrect links into their user profile checks are in place that the instagram link has to include https://www.instagram.com. This pushes the user to copy and past a link and stops any other social media site being put in this section of the form. 

If they attempt to they are met with the message below: 

![Create Profile Page](static/media/create_profile_social_links_check.png)

If they successfully create their profile they are redirected to the home page and will see the 'profile' link in the navbar. 

[Back to contents](#contents)

#### User Profile

The user profile has multiple roles. At the top the users profile picture is shown alongside their display name, the total distance they have walked, the number of mountain peaks they have reached as well as their social media links and the option to update their profile if they should want to change their display name or profile picture / social media links. 

If the user has not added social media links they are met with a paragraph saying they would be able to see links to them if they added any in the update profile section. 

![Profile Page](static/media/profile_no_profile_picture.png)

If they do add social media links font awesome icons are added which change color on hovering, the icons change depending on the social media link they have added to their profile: 

![Profile Page without social media links](static/media/profile_view.png)

The user has the option to add a profile picture. If no profile picture is used then a default image is used seen in the snap shot above. If they add their own the default image is replaced with this

The user profile displays all posts the user has made, paginated by 6 shown in rows of 3. This allows the user to see everything they have done and feel a sense of pride over their achievements. Note pagination will be explained in the home section. 

The user is able to see their progress towards walking all of the brecon beacons major peaks which is picked up from any posts they have added to the blog. Peaks reached get a gold mountain next to them and are put into the "You've conquered:" section. Peaks still left to walk have a silver hiker symbol and are left in the "Still left to conquer:" section

![Profile Progress](static/media/progress.png)

This section of the profile picture has buttons which switch the tabs the user sees. If they hit "Achievements" they see the achievements and if they hit "progress" they go back to the progress page. Achievements are a result of accumulated posts so if the user covers 50km distance walked over any number of posts they receive an award, if they reach 5 cairns / mountains they receive another award. This is designed to keep the user moving and posting. 

![Profile Progress](static/media/achievements.png)

#### Home

The home page simply shows the posts made by all users, paginated by 8 in rows of four on a larger screen, rows of 1 post on mobile. When you hover over the posts they change colour to highlight that you are hovering over them. This interactivity is designed to provoke a positive response with the user. 

![Profile Progress](static/media/home_page_post_hover.png)

##### Pagination

Pagination comes with a navigation bar at the bottom, available on both the home and profile page. if the user is on the first page they are only able to see right pointing arrows as there is no previous page to go to. Clicking the double arrows will take you all the way to the last page, single arrow will take the user to the next page. 

![Pagination](static/media/pagination_1.png)

If there are previous pages of posts to view the user will see left facing arrows, as shown below: 

![Pagination](static/media/pagination_2.png)

This allows clear navigation of posts for the user. 

#### Tips

In order for usage of the site to be clear at all times I added a "tip" function to the navbar which relies on javascript to change the modal's message depending on the page the user is viewing. The tips item clearly seen in the navigation bar gives the user instructions on how each page can and should be used. It appears as a modal on each page and the text changes depending on whether the user is logged in, logged out or where they are in the site. 

If the user is not logged in they are welcomed to the page and prompted to log in or sign up, this message will occur regardless of where they are in the site: 

![Tips](static/media/tip_not_logged_in.png)

If the user is logged in on the home page they see the below: 

![Tips Home Page](static/media/tip_home_page.png)

If the user is creating or updating their profile they see the below making the URL item clear: 

![Tips Create Profile](static/media/tip_create_profile.png)

If the user is on the about page or logging out they see the message below as in theory no explanation would be required for anyone on these pages. 

![Tips about or logout](static/media/tip_logout.png)

If the user is creating or editing a post they see the tip below which makes clear that up to 3 images and 3 cairns / mountains can be added to each hike: 

![Tips about or logout](static/media/tip_add_post.png)

#### About

The about page shows the sites purpose and is available through the navbar: 

![About Page](static/media/about_main_view.png)

When viewed on a mobile the image is no longer visible and a simple text box appears: 

![About Page](static/media/about_main_mobile.png)

#### Add Post

A user can add a post once they have logged in. They are prompted to complete the form through a series of checks. The only sections of the form which must be filled in to submit the form are the title, distance (all works would have a distance, otherwise they would be a stand) and the notes to review their walk.  

![Add Post](static/media/add_post_first.png)

Up to three images can be added and three cairns / mountains. As the three peaks is an enormous challenge in the brecons it is likely that three walks would be the most someone would do in a day. If they do more this would be pushed to two walks. 

The option to fill in a second cairn / mountain or second image appears once the first has been filled in. 

The first cairn can be deleted once entered and the second mountain / cairn  kept with no ill effects however this is all summed into a single column in the profile view so does not matter. 

![Add Post second image](static/media/add_post_second.png)

The the user tries to submit the form without a title or distance they are met with the below: 

![Add Post warning](static/media/add_post_no_name.png)

No distance: 

![Add Post warning distance](static/media/add_post_no_distance.png)

Once they have submit the post correctly they will be taken to the main home page where they can see it as the most recent post. 

#### Detailed View

The detailed view allows users to see a greater level of detail on each post than presented on the home page including the three images the user added (if they used this option) presented as a slide show. Otherwise a default image will be shown if no images were added to the post. Finally if only one image added by the user then no slide show is available and the "next image" link is hidden. 

![detail view](static/media/detail_header.png)
![detail view second image](static/media/detail_second_image.png)

This appears under the title and the users chosen display name. 

If the user reached the top of mountains / cairns these will be displayed on the detail view. If they did not then the caption reads "No cairns reached, still proud". We want to inspire users to walk regardless of reaching the tops of mountains for the site to be fully inclusive. 

Defensive design is employed here as the user will only see the links to update or delete the post if they are the creator of the post

If a user is logged in they will be able to star or comment on the users post: 

![detail view comment 1](static/media/detail_post_comment.png)

The comments are then ordered by date created. 

![detail view comment 2](static/media/detail_post_comment_2.png)

I have not opted to approve any comments or posts similar to facebook or strava. Instead the user if bullying or antisocial in anyway can simply be deleted from the admin panel. 

A post can be 'starred' similar to a like system, the method for this was taken from the code institute tutorial video. When not starred by a user the star appears empty. If you star it then it fills with gold: 

![star 1](static/media/star_not_clicked.png)
![star 2](static/media/star_clicked.png)

If the user is not logged in or signed up they will see the below level of detail with the aim of inspiring people to join and signup by letting them see what other people are achieving: 

![detail view not logged in](static/media/detail_not_logged_in.png)

#### Delete Post

A post can be deleted using djangos built in system. Any user can delete their own posts using the delete post button on the detail view. They are taken to a new screen to confirm and then taken to the home screen if they confirm. 

#### Footer

The footer holds the site logo, social links for the site (fillers used for now) and the option to logout when logged in. If not logged in the footer shows the option to sign up or login. 

![Footer](static/media/footer_full.png)

When compressed the footer items are hidden to make viewing easier

![Footer compressed](static/media/footer_compressed.png)

When you hover over items on the footer they change colour to give a greater sense of user interactivity

![Footer hover](static/media/hover.png)

#### accessing tabs if not logged in

If any user somehow gets to the add post page, create profile page they are met with the below and cannot perform other actions. 

![accessing tabs if not logged in](static/media/login_prompt.png)

If the access another users post and attempt to delete it or update is they are met with the below

![delete or update post if not logged in](static/media/not_your_post.png)

### Future Features

These are endless, however key items below

* I would like to design a map which lights up in sections when a user has hiked that section of the map to further gamify the system. In addition it would show the location of the other major peaks of the region which they have yet to do with details of the peak upon hovering over it. 
* allow posts to be loaded in from strava and the peaks identified automatically. This and the item above would have to be done for this project to become a viable project. 
* I had everything in place to comment on comments, so users could respond to any comment made on their post however the django system I had in place would only take a comment from the first text box on the screen rather than that the user was typing into. I ran out of time to fix this. 
* Block swear words and profanities, though the only way I could think to do this was to create a list of them as an array and then ensure they were not in the comment or post notes when a user submitted. To do this I would have to myself write a list of the swear words and don't think its suitable for a course reviewer to have to read all of these. 

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