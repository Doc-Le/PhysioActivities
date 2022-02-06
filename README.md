# Milestone 4 - Final Project 

Demo - See live: https://physioactivities.herokuapp.com

## Logo
#

![Alt](static\images\logo-225x45.png "PhysioActivities")
#

## Intro
#

This idea originally came up at first as I'm a Senior Physiotherapist working in the field over the last 20 years. I understand the importance to have a platform/website that can provide information about the clinician and independence to make a booking/payment.
#

## User Experience (UX)

### User stories

#### First Time Visitor Goals

* As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about what the clinic and the clinician have to offer.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
* As a First Time Visitor, I want to look for information to understand what each treatment technique has to offer. 
* As a First Time Visitor, I  also want to locate his social media links to see their followings on social media to determine how trusted and known the company is.
*  As a First Time Visitor, I want to easily schedule an appointment and pay. 

### Returning Visitor Goals

* As a Returning Visitor, I want to find information about what the clinic has to offer.
* As a Returning Visitor, I want to find the best way to get in contact with him.
* As a Returning Visitor, I want to find community links.


## Goals
#

 * Create a user-friendly, well-designed website easily understood 
 * Create a registration form that stores information about users in a database in an organized fashion. 
 * Create a login system so that the user has to log in to make an appointment. 
 * Make an appointment form so that the user can submit information about their injury as well as a day and time that suits them   and see if the chosen clinician has availability. 
 * Create links to social networking sites so the user can find out more about the physiotherapist or write a good review on their page e.g.(Google, Twitter, Facebook) 
 * Have information about the location of the physiotherapist. 
 * Information about the different types of services the physio offers so that the customer can decide if the physio actually does that service before contacting.

## Design 
#

  * Color Scheme
     The two main colors used are green and white.

  * Typography
    The Roboto font is the main font used throughout the whole portfolio with Sans Serif as the fallback font.
  
  * Imagery
    Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.

#
## Wireframe
#


## Tech used
#

* HTML
* CSS
* DJANGO
* JavaScript
* Bootstrap5
* MySQL
* API
* Stripe payment
#

## Frameworks, Libraries & database
#
1. [Bootstrap 5.0.1](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    * Bootstrap was used Stores CSS Bootstrap library files
2. [AwS3](https://eu-west-1.console.aws.amazon.com/)
    * jsDoc was used as format to Stores JavaScript Bootstrap library 
3. [CSS3](http://www.css3.com/)
    * CSS3 was used for Implementation of main HTML CSS that imports all CSS files in the main CSS folder 
4. [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the IDE terminal to commit to git and push to GitHub
5. [GitHub](https://github.com/Doc-Le/PhysioActivities.git)
    * GitHub is used to store the project after being pushed from Git 
6. [Heroku](https://dashboard.heroku.com)
    * GitHub is used to store the project after being pushed from Git  
7. [Stellar.js v0.6.2 ](http://markdalgleish.com/projects/stellar.js)
    
8. [Sticky Plugin v1.0.3 for jQuery](http://stickyjs.com/)
    
9. [Owl Carousel v2.2.1] ( Copyright 2013-2017 David Deutsch)
    
10. [SmoothScroll](Copyright 2013 http://DWUser.com)

10. [/*! WOW - v1.0.2 - 2014-10-28](Copyright (c) 2014 Matthieu Aussaguel; Licensed MIT)
            
#
## Features
#
The easy navigation bar and at key places throughout the design.
About us page with introductory information.
Meet the team segment that presents each member of the team.
Services page detailing each technique with a client comment.
Make an appointment button that takes the user to log in or sign-up.
User Easy access to the booking system, choose the type of service, clinician, time, and date.
Online payment with a credit card.
#


## Testing
#
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator - Results (link)
Testing User Stories from User Experience Section

#
## Further Testing
#
This app was tested on Google Chrome, Microsoft Edge, and Safari browsers
This app was viewed on a variety of devices such as Desktop, Laptop, IPhone7, IPhone8
#
## Stripe 
#
### Accept payments with Stripe Checkout

We built a easy straight forward checkout to provide to the client the best experience.
Once the customer choose the clinician/date/time and is ready to pay, use Stripe.js to redirect them to the URL of your Stripe hosted payment page.

### Stripe demo/mock card

The demo is running in test mode -- use 4242424242424242 as a test card number with any CVC + future expiration date.

#
## Deployment
#
The project was deployed to GitHub Pages using the following steps:

* Log in to GitHub and locate the GitHub Repository
* At the top of the Repository (not top of the page), locate the Settings Button on the menu
* Scroll down the Setting page until you locate the GitHub Pages Section
* Under Source, click the dropdown called “None” and select “Master Branch”
* The Page will automatically refresh
* Scroll back down through the page to locate the now published site Link in the GitHub Pages section

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone, Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Downloading a ZIP file of the code, or Clone this repository using by command:
```#!/bin/sh
$ git clone https://github.com/Doc-Le/PhysioActivities.git
```
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
```#!/bin/sh
$ pip install virtualenv
$ virtualenv venv
```
Windows
```#!/bin/sh
$ source venv/Scripts/activate
```
Linux / Mac
```#!/bin/sh
$ source venv/bin/activate
```
* Note that you can exit the virtual environment by running the command:
```#!/bin/sh
$ deactivate
```
* **Step 4** : Download the all dependencies in the requirements.txt by running the command:
```#!/bin/sh
$ pip install -r requirements.txt
```

* **Step 5** : Make Django database models migrations by running the command:
```#!/bin/sh
$ python manage.py makemigrations
```

* **Step 6** : Migrate Django database models by running the command:
```#!/bin/sh
$ python manage.py migrate
```
* **Step 7** : Update environment variables on `settings` file
  | Variable  | Description |
  | --- | --- |
  | `SECRET_KEY`  | Django secret key |
  | `STRIPE_PUBLIC_KEY`  | todo... |
  | `STRIPE_SECRET_KEY`  | todo... |
  | `EMAIL_HOST_PASS`  | Email host 2-way auhtentication password when sending Django SMTP emails |
  | `EMAIL_HOST_USER`  | Email host user used when sending Django SMTP emails |
  | `HOST_DOMAIN`  | Local host domain that is usually default Django **`http://127.0.0.1:8000`** |

* **Step 8** : Run server by running the command:
```#!/bin/sh
$ python manage.py runserver
```

## Content

All content was written by the developer


## Media

* Logo custom made by the developer with Adobe Illustrator
* All images found [Image: wutzkoh / stock.adobe.com]