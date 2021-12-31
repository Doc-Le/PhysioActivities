## Milestone - Final Project 
# Logo

# Intro
Physiotherapy Clinic website 
This idea originally came up at first as I'm a Senior Physiotherapist working in the field over the last 20 years. I understand the importance to have a platform/website that can provide information about the clinician and independence to make a booking/payment.

# Goals

⦁ Create a user-friendly, well-designed website easily understood 
⦁ Create a registration form that stores information about users in a database in an organized fashion. 
⦁ Create a login system so that the user has to log in to make an appointment. 
⦁ Make an appointment form so that the user can submit information about their injury as well as a day and time that suits them and see if the chosen clinician has availability. 
⦁ Create links to social networking sites so the user can find out more about the physiotherapist or write a good review on their page e.g.(Google, Twitter, Facebook) 
⦁ Have information about the location of the physiotherapist. 
⦁ Information about the different types of services the physio offers so that the customer can decide if the physio actually does that service before contacting.

Demo - See live code: https://physioactivities.com 

## Tech used

HTML
CSS
DJANGO
JavaScript
Bootstrap5
MySQL
API
Stripe payment



## Features

The easy navigation bar and at key places throughout the design.
About us page with introductory information.
Meet the team segment that presents each member of the team.
Services page detailing each technique with a client comment.
Make an appointment button that takes the user to log in or sign-up.
User Easy access to the booking system, choose the type of service, clinician, time, and date.
Online payment with a credit card.



## Design 

  * Color Scheme
      The two main colors used are green and white.

  * Typography
    The Roboto font is the main font used throughout the whole portfolio with Sans Serif as the fallback font.
  
  * Imagery
    Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.


## Wireframe


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator - Results (link)
Testing User Stories from User Experience Section


## Further Testing

This app was tested on Google Chrome, Microsoft Edge, and Safari browsers
This app was viewed on a variety of devices such as Desktop, Laptop, IPhone7, IPhone8

## Stripe 

### Accept payments with Stripe Checkout

We built a easy straight forward checkout to provide to the client the best experience.
Once the customer choose the clinician/date/time and is ready to pay, use Stripe.js to redirect them to the URL of your Stripe hosted payment page.

### Stripe demo/mock card

The demo is running in test mode -- use 4242424242424242 as a test card number with any CVC + future expiration date.


## Deployment

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

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Doc-Le/PhysioActivities.git)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Doc-Le/PhysioActivities
```

7. Press Enter. Your local clone will be created.
### Installation and Set-up
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
* All images found []