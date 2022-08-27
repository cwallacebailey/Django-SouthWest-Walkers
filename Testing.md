# Testing

### Contents 

* [Manual Testing](#manual-testing)
  * [Devices and Browsers](#devices-and-browsers)
  * [User Story Testing](#testing-user-stories) - To Do
  * [Testing Technologies](#testing-technologies)

* [User Access](#user-access)

* [Site Functions](#functions)
  * [Register](#register)
  * [Log In](#log-in)
  * [Log Out](#log-out)
  * [Add Posts](#add-posts)
  * [Update Posts](#edit-posts)
  * [Delete Posts](#delete-posts)
  * [Create Profile](#create-profile)
  * [Update Profile](#update-profile)
  * [404](#404)
  * [500](#500)

* [Lighthouse](#lighthouse)

* [Automated Testing](#automated-testing)

#### Desktop

1. Chrome
    * All tested and working correctly.

2. Edge
    * All tested and working correctly.

3. Mozilla Firefox
    * All tested and working correctly.

[Back to contents](#contents)

#### Mobile

1. Chrome
    * All tested and working correctly.

2. Edge
    * All tested and working correctly.

3. Mozilla Firefox
    * All tested and working correctly.

[Back to contents](#contents)

* Site was tested on Chrome, Firefox and Edge. IE was ignored as it is no longer used
* The website was tested on multiple device sizes, including:
  * Galaxy S5
  * Pixel 2 XL
  * Iphone 5 SE
  * Iphone 6/7/8
  * Iphone 6/7/8 Plus
  * Iphone X
  * iPad
  * iPad Pro

[Back to contents](#contents)

### Testing tech

* HTML markup validator was used for all HTML code - [W3C HTML Markup Validator](https://validator.w3.org/).
* CSS was validated with [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).
* JavaScript was validated with [JSHint](https://jshint.com/).
* Python was validated using [pep8](http://pep8online.com/)
* Responsive design was tested with [Lighthouse](https://developers.google.com/web/tools/lighthouse)

1. W3C HTML Markup Validator
    * All pages were checked, only one note of unclosed Divs on the update profile page however on inspections these divs are definitely closed. 

2. W3C CSS Validator
    * No errors in the CSS file, see results below: 

![css_validator](static/media/css_validator.png)

3. JSHint
    * [JSHint](https://jshint.com/)
    * The only comments from JSHint are about template literals, the `let` keyword and there are no JavaScript errors in this project.

![jshint_validator_results](static/media/jshint_validator_results.png)

[Back to contents](#contents)

### Lighthouse

#### Desktop Site

Both the desktop and mobile site received the same levels in the report, hence the screenshots are identical. I was happy with the accessibility and the SEO. The performance could be improved by using smaller images and I have added this to future features, by putting in a max size for images this could be sped up however through all the testing the site functions well so I am not alarmed by the amber score. 

![lighthouse report](static/media/lighthouse_report.png)

The best practice alert can be seen below. This references the Jquery script for bootstrap so I have left it in and will take the 86 best practice. 

![lighthouse report](static/media/jquery_best_prac.png)

[Back to contents](#contents)

#### Mobile Site

Both the desktop and mobile site received the same levels in the report, hence the screenshots are identical and notes below are the same as above. 

I was happy with the accessibility and the SEO. The performance could be improved by using smaller images and I have added this to future features, by putting in a max size for images this could be sped up however through all the testing the site functions well so I am not alarmed by the amber score. 

![lighthouse report](static/media/lighthouse_report.png)

The best practice alert can be seen below. This references the Jquery script for bootstrap so I have left it in and will take the 86 best practice. 

![css_validator](static/media/lighthouse_report.png)

[Back to contents](#contents)

#### Automated Testing

I have created a number of automated testing functions, to test views and URLS. The testing coverage is not complete and has to be run with "--debug" added at the end of the command "python3 manage.py test ..." in order to work. This was found with the help of the tutors as unfortunately I could not get any tests to function before adding this to the command. 