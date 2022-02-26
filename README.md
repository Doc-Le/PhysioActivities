# Milestone 4 - Final Project 

Demo - See live: https://physioactivities.herokuapp.com

<div align="center">
  
  ![PhysioAct](https://user-images.githubusercontent.com/76841050/155844125-75cb60e1-134e-4e2e-b2b9-59685902ee0c.gif)
  
</div>

## Intro
#

This idea originally came up at first as I've been working in the field for 19 years. I understand the importance to have a website that can provide information about who is providing the treatment, and also the independence to make a booking and payment. 
#

## User Experience (UX)

### User stories

<div align="center">
  
  
  
</div>

, https://user-images.githubusercontent.com/76841050/155841738-632ae234-7bf0-4937-9686-c4d8e61d44bb.mp4


#### First Time Visitor Goals

* As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about what the clinic and the clinician have to offer.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
* As a First Time Visitor, I want to look for information to understand what each treatment technique has to offer. 
* As a First Time Visitor, I  also want to locate his social media links to see their followings on social media to determine how trusted and known the company is.
*  As a First Time Visitor, I want to easily schedule an appointment and pay. 

### Returning Visitor Goals

* As a Returning Visitor, I want to find information about what the clinic has to offer.
* As a Returning Visitor, I want to find information about what kind of service is provided.
* As a Returning Visitor, I want to find information and reviews about the clinicians.
* As a Returning Visitor, I want to find information about the type of techniques.
* As a Returning Visitor, I want to find easy access for bookings and payments.

## Goals
#

 * Create a user-friendly, well-designed website easily understood 
 * Create a registration form that stores information about users in a database in an organized fashion. 
 * Create a login system so that the user has to log in to make an appointment. 
 * Make an appointment form so that the user can submit information about their injury as well as a day and time that suits them  and see if the chosen clinician has availability. 
 * Create links to social networking sites so the user can find out more about the physiotherapist or write a good review on their page e.g.(Google, Twitter, Facebook) 
 * Have information about the location of the physiotherapist. 
 * Information about the different types of services the physio offers so that the customer can decide if the physio actually does that service before contacting.


  ## Current features 

-   Responsive on all device sizes

-   Accessible 

-   Easy to navigate (Single use learning)

-   Interactive elements

-   Social Links 

-   Ability to contact the clinic via contact page.

-   Able to search treatments and clinicians available.

-   Can search future location or details.

-   Logged in users can their previous and future appointments.

-   Logged in user can save their addresses and default address, pre-fills Checkout form

-   Admin user can add, edit and delete any event.

-   Confirmation email on registration and on successful purchase.

## Design 
#

  * Color Scheme
     The two main colors used are green and white.
     Picked these colors idea from a healthy three that symbolized heath. These colors create a set feel of the site.

  * Typography
    Used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site.
    The Poppins font is the main font used throughout the whole website.
  
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
2. [Django](https://www.djangoproject.com/)
    - Framework for building applications.
3. [CSS3](http://www.css3.com/)
    * CSS3 was used for Implementation of main HTML CSS that imports all CSS files in the main CSS folder 
4. [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the IDE terminal to commit to git and push to GitHub
5. [GitHub](https://github.com/Doc-Le/PhysioActivities.git)
    * GitHub is used to store the project after being pushed from Git 
6. [Heroku](https://dashboard.heroku.com)
    * For deploying the application 
7. [Stellar.js v0.6.2 ](http://markdalgleish.com/projects/stellar.js)
    
8. [jQuery](https://jquery.com/)
    - Required for some of the bootstrap elements such as collapsibles, modal and tooltips.

9.  [Owl Carousel v2.2.1] ( Copyright 2013-2017 David Deutsch)
    
10. [SmoothScroll](Copyright 2013 http://DWUser.com)

11. [WOW - v1.0.2 - 2014-10-28](Copyright (c) 2014 Matthieu Aussaguel; Licensed MIT)

12. [Postgres](https://www.postgresql.org/)
    - Database used for our data
13. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    - Used to generate secret key
            
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
  | `STRIPE_PUBLIC_KEY`  | Generate public key on Stripe portal |
  | `STRIPE_SECRET_KEY`  | Generate secret key on Stripe portal |
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
