# Live Plants

## E-Commerce store for a selling house plants
------------------------------------

![alt text](./docs/forged_nature_responsive.png)

### Live site available [here](https://liveplants-61cae3ad1da7.herokuapp.com/). 


-----

## Table of Contents
--------------------------------------

- [Description](#description)
- [Design](#design)
- [UX](#ux)
- [Agile Development](#agile-development)
- [Web Marketing](#web-marketing)
- [Features](#features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Author Info](#author-info)

------

## Description
---------------------------------------

Live Plant is a user-friendly online store where you can buy plants and manage the product inventory easily.
This fully functional E-Commerce store built in Django using Python, JavaScript, CSS, Bootstrap5, HTML and it incorporates stripe payments.
The site enables user roles, authentication, and Full CRUD for products, allowing interaction with a central dataset securely.

Live Plants site offers a wide selection of high-quality plants suitable for indoor and outdoor environments. With user-friendly navigation and secure payment options, customers can easily browse, select, and purchase their desired plants. We strive to provide excellent customer service and ensure a seamless shopping experience for all plant enthusiasts.

This website is designed as the final project for the Code Institute Diploma in Software Development course. Please note that it does not process real payments or fulfill orders. However, you are welcome to test the payment functionality using the provided card details when prompted.

`Card number: 5555 5555 5555 4444  Exp: any future date eg. 11/26 CVC: any 3 digits eg 123`


[Back to the Top](#table-of-contents)




-------
## Design
-------

### Wireframe mock-ups
---


---
## Database Schema

Several custom models were predicted to be required when building the site. On top of the standard Sculpture/Order models these included a Newsletter signup Model a Message Model and a customer Review model. The database schema was drawn out by hand.

![Database Schema Diagram](./docs/database-schema.jpg)


These colours were:

Grey/Blue: #6f8ca2

Dusty Orange: #ff85436b

Whitesmoke: #f5f5f5

And Bootstraps Text-Muted class for sligtly greyed out text.


[Back to the Top](#table-of-contents)

---

## UX
*  The UX (User Experience) of Live Plants was designed to ensure a friendly and informative website. Users can easily explore and find products of interest, while the visually appealing design enhances the overall delightful and enjoyable online experience..

### The Sites Ideal User
* The ideal user for Live Plants is anyone who has an interest in plants, gardening, or adding greenery to their surroundings. Whether you're a beginner looking to start your plant collection or an experienced gardener seeking new additions, Live Plants caters to users of all levels. The site welcomes plant enthusiasts of various ages and backgrounds, providing a platform to explore and purchase a wide range of plants conveniently.


### Site Goals

* Site owner goals:
- Drive sales and generate revenue by offering a wide range of appealing and high-quality plants.
- Enhance customer satisfaction and loyalty through excellent customer service and a user-friendly website       
  experience.

* User goals:
- Easily find and explore a variety of plants based on their interests and preferences.
- Have a seamless and secure shopping experience, including convenient payment options and reliable product 
  information.

[Back to the Top](#table-of-contents)

## Agile Development

For this project, the Agile methodology was employed, utilizing GitHub as the platform. User Stories were created as issues on GitHub, clearly outlining the purpose of each issue. Each User Story was divided into acceptance criteria and tasks, facilitating a structured approach. Prioritization was accomplished by leveraging GitHub labels, which were color-coded for easy distinction. This Agile approach fostered efficient project planning and execution.

### Epics

1. Sign in/out 
2. Landing page/Frontend Templates 
3. View Products/Admin CRUD functionalikty 
4. Shopping Cart 
5. User Feedback 
6. Payments 
7. User Profile 
8. Contact Artist/Social links 
9. Customer Reviews 
### User Stories

These are the user stories that were completed within the projects first release, by Epic.


- User Sign in or Sign out
	*  User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can avail of the sites full functionality
	*  Receive Welcome Emails - As a user I would like to receive a welcome email upon signing up
    *  Reset password Functionality - As a user I would like to be able to reset my password to keep my account safe
    *  Visibly logged in or out - As a user I would like to know if I am logged in or not

- Landing page
	*  As a User I would like to be brought to the landing page upon first visiting the site so that I can see what options are available to me
    *  As a User from the landing page I should clearly be able to see and navigate the navbar
    *  As a User on the landing page I should be easily able to go straight to the shop and purchase an item

- View Products, Admin CRUD
    *  As a user I should be easily able to see a list of products available.
    *  As a user I should be able to click on any item to see more information about it.
    *  As an Admin I can add products to the database
    *  As an admin I can edit products in the database
    *  As an admin I can delete products from the database

- Shopping Cart
    *  As a user I can easily view the contents of my Cart
    *  As a user I can easily add/edit/delete the contents of my Cart
    *  As a user I can easily identify the total cost of my Cart

- User Feedback/Confirmation
    *  As a user I receive prompt feedback concerning my actib=vity on the site
    *  As a user I can see a order confirmation message
    *  As a user I receive an order confirmation email

- Payment Feature
    *  As a user I can visit a payment screen
    *  As a user I can input my credit/debit card details

- User Profile
    *  As a user I can sign in/create a profile so that I can avail of the sites full functionality ie. leave customer reviews

- Contact site owner/Social links
    *  As a user I can signup to a Newsletter
    *  As a user I can fill out a contact form
    *  As a user I can clearly see contact information
    *  As a user I can easily find social media links and when pressed they take me to the correct site

- Customer Reviews
    *  As a user I can clearly see reviews left by past customers
    *  As a user who is logged in I can easily leave a review

[Back to the Top](#table-of-contents)

---


## Web Marketing

#### **E-Commerce Application Type**
The plant sell website follows a Business to Consumer (B2C) model, enabling direct transactions between the business and individual customers. It offers a wide selection of plants, allowing customers of all backgrounds and preferences to conveniently purchase their desired plants for personal use or gifting purposes.

#### **Marketing Strategy**
As Live Plants is a start-up business with limited marketing budget, there are several effective ways to boost sales and brand visibility. Utilizing Facebook to share engaging content and drive traffic is a primary and straightforward strategy. Paid advertisements can be employed to target specific demographics and enhance brand awareness. Leveraging social media platforms also facilitates customer feedback and improves customer service. Below is an image of the Facebook page, and you can access it [here](https://www.facebook.com/profile.php?id=100094665704253).[page](https://www.facebook.com/profile.php?id=100094558639714)
Another effective method is utilizing Google Ads, which can greatly enhance brand awareness and assist with SEO efforts. Google Ads can also aid in targeting specific long-tail keywords and improve the overall ranking of the website.

Another marketing strategy involves sending regular newsletters to the mailing list obtained through sign-up forms. These newsletters would include links to recent articles, new products, special offers, and promotions. This helps in building brand awareness and fostering a community around the brand.

#### **Search Engine Optimization**

To achieve high search engine rankings, the website implemented various SEO techniques. Additionally, essential files such as robots.txt and sitemap.xml were included to enhance search engine visibility and indexing of the site's content.


#### **Facebook Page**
![Facebook Page](./docs/Facebook-mockup.png)

---


## Features

**Features planned:**
* User Profile - Create an account to leave customer reviews.
* Users can login to their account.
* Users can logout of their account.
* Users can sign up to a Newsletter
* Users can easily contact the site owner by filling in a contact form
* Users can easily see the products available by navigating to the shop page
* Logged in users can leave reviews of past purchases
* Users can add/edit/delete items in a shopping cart
* Users can finalize their purchase by inputting their card details and recieve order confirmation
* Products - Admin can create, read, update and delete their own products.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access an E-Commerce site.


---
#### Home page
A welcoming homepage was built to welcome the user to the site and clearly convey the sites purpose.

![Home Page]()

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require includinglink to Contact and Blog. All produts link has dropdown menu with categories. 

![Nav Bar]()


#### Footer
A common footer is utilised throughout the site and including newsletter signup form from mailchimp.


![footer](./docs/desktop-footer.png)


#### Other Pages/Features
[Shop]()

[clearance]()

[Cart]()

[Checkout]()

[All Products]()

[Newsletter Signup]()

[Register]()

[Sign In]()

[Site Admin]()

[Individual Product Page]()

[Reviews]()


## Future Enhancements
There are several items of functionality that I would like to add in the future. 
The key areas I would like to add to the site in the future are:

* Change the design 
* Add more categories in the shop

AllAuth signup:
The templates for allauth have been changed to suit the style of the site 


[Back to the Top](#table-of-contents)

---

## Testing

### Testing Strategy

For the development of the site, I employed a manual testing approach. In addition to functional and code testing, User Story tests were specifically implemented to verify that the criteria outlined in the user stories mentioned earlier were successfully fulfilled.


#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.


#### Validator Testing
All code files were validated using suitable validators for the specific language.
HTML & CSS code passed the validation.
JavaScript code produced one warning about an undefined variable but this is nothing to worry about as it is defined in another file.
All validation screenshots are included below.

All HTML validation returned the same result so I have included only 1 screenshot here.
## HTML
![HTML Validation]()
## CSS
![CSS Validation]()
## Script JS
![Script JS]()
## Stripe JS
![Stripe JS]()
## Quantity Input JS
![Quantity Input JS]()


#### Lighthouse Testing
Below you can see the results of Googles Lighthouse Testing.

![Lighthouse Testing]()



#### Python/JavaScript Testing
All Custom Python & JavaScript code was manually tested multiple times during and after development.
This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

## Testing 

Please refer to [TESTING.md](./TESTING.md) file for:
* Manual Testing and Results
* Validation of all languages
* Lighthouse scores



[Back to the Top](#table-of-contents)

-----

## Technologies

* Python
* Django
    * Django was used as the main python framework in the development of this project.
* Heroku
    * Was used as the cloud based platform to deploy the site on.
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
    * Custom JavaScript was utilised to allow Users to close site messages and increment/decrement cart items.
* Bootstrap 5
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.
* Stripe
    * Stripe was used to allow the store to accept card payments.

#### Packages Used

* VS Code & Gitpod was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project

#### Resources Used

* The Django documentation was used extensively during development of this project
* The Cloudinary documentation was used.
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


[Back to the Top](#table-of-contents)

----

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Forged Nature](https://rossanthonydesigns.herokuapp.com/)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered RossAnthonyDesigns and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection

* Set up Amazon Web Services' S3 to host our static files and images**
**Create an account** <br/>
* Create an AWS Account by going to [aws.amazon.com](https://aws.amazon.com/) and click on *create an aws account* by filling in your email and a password and choose a username for the account and select *continue*
* On the account type, select *personal*, fill out the required information, and click *create account and continue*
* Enter the credit card number which will be used for billing if the account goes above the free usage limits
* Complete the verification and once you confirm all the required information, your account will be created.
**Create a bucket**
* Once your signed in to your account, find S3 using the search bar, select and navigate to S3 to create a new bucket which will be used to store your static and media files
* Click the *create bucket* button and on the General configuration section, add the name of your bucket. It is a good idea to name the bucket the same as your project to keep your buckets organized and clear
* Select the region closest to you
* On the Object Ownership section, select *ACLs enabled* and a bucket ownership dropdown will appear, select *Bucket owner preferred*
* On the Block Public Access settings for this bucket section, uncheck *Block all public access*, check the *I acknowledge that the current settings might result in this bucket and the objects within becoming public* checkbox to make the bucket public and click *create bucket*
* Click the bucket you created and select the *properties* tab. Scroll down to find the *static web hosting* section and select *enable static web hosting*, tick *host a static website* and add *index.html* and *error.html* to the input fields for **Index document** and **Error document** respectively and click *save*.
* Open the permissions tab and copy the ARN (Amazon Resource Name). Navigate to the bucket policy section, click *edit* and select *policy generator*. From the *Select Type Policy* dropdown options, select S3 bucket policy. We want to allow all principal by adding the `*` to the input and the from the *Actions* dropdown, select *GetObject*.
* Paste the ARN we copied into the ARN (Amazon Resource Name) input field and click *add statement*, then click *generate policy*, copy the Policy from the new popup and paste it into the bucket policy editor and add `/*` at the end of the resource value to allow access to all resources in this policy and finally, click *save*.
* AWS has changed the format of their **cross-origin resource sharing (CORS)** configuration so we need to paste the update code below to the CORS section:
```json
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
* For the **Access control list (ACL)** section, click *edit* and tick *List* for **Everyone (public access)** and accept the warning box. If the edit button is disabled you need to change the **Object Ownership** section above to **ACLs enabled**.

**Create Group, Policies and Users using AWS's Identity and Access Management (IAM) service**<br/>
* Find IAM using the search bar, select and navigate to IAM to create a group, create an access policy to give the group access to the S3 bucket and assign the user to the group so it can use the policy to access the files.
* Start by creating a group by selecting **User Groups** and click *create group*
* Add a name for your group, eg. manage-black-and-white-beauty, then click *create policy* button
* Open the *JSON* tab on the new page and click the *import managed policy* link on the top right side of the page
* Search for S3 and select the pre-built *AmazonS3FullAccess* policy and click *import*
* Edit the policy by pasting the S3 ARN on *resource*, ie:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        }
    ]
}
```
* Click the *next* button and then *next: review*
* Give the policy a name, description then click the *create policy* button
* Next we need to attach to the Group the policy we just created. Go to *User Groups*, select the group and go to the permissions tab, click the *add permissions* button and select *attach policies* from the dropdown.
* Select the Policy you created and click *add permissions*
* We have to create a user for the group. Click *Users* from the left sidebar and then click the *add users* button and add a name for the user, eg. black-and-white-staticfiles-user
* Next tick *programmatic access* from Access Type and click *next: permissions*
* Add user to the group and click *next: tags*, *next: review* and then the *create user* button.
* The download the .csv file which will contain this user's access key and secret access key which we'll use to authenticate them from our Django app.

**10. Connecting Django to S3**
* Install two new packages: **boto3** and **django-storages**
```bash
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
* Add `storages` to the installed apps in **settings.py**
* Also on **settings.py**, add the bucket configuration:
```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
* Open the .csv file we downloaded earlier and go to Heroku app dashboard and add these to Config Vars:
| Key | Value |
| :-- | :-- |
| AWS_ACCESS_KEY_ID | The access key value from the .csv file |
| AWS_SECRET_ACCESS_KEY | The secret access key value from the .csv file |
| USE_AWS | True |
* Remove **COLLECTSTATIC** variable from the Config Vars
* Create **custom_storages.py** file and add:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
* Next, go back to **settings.py** file and tell it that for static file storage, we want to use our storage class we just created and that the location it should save static files us a folder called static. And then do the same thing for media files using the default file storage and media files location settings.
```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
```
* We also need to override and explicitly set the URLs for static and media files using our custom domain and the new locations:
```python
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
* Next, save the **settings.py** file, add all these changes, commit them and then issue a git push which will trigger an automatic deployment to Heroku. With that done if we look at the build log. We can see that all the static files were collected successfully
* To handle the media files, Let's go to s3 and create a new folder called media then click *upload*. Add the product images files, click *next* and under manage public permissions, select *grant public read access to these objects.* Then click *next* through to the end and finally, click *upload*.

11. Setting  up Stripe
* Log in to Stripe, click the *developers* link, and then *API Keys*
* Add them as Config Vars in Heroku
* Now we need to create a new webhook endpoint since the current one is sending webhooks to our gitpod workspace. We can do that by going to webhooks in the developer's menu and clicking *add endpoint*.
* Add the URL for our Heroku app, followed by /checkout/WH and select *receive all events and add endpoint*.
* We can now reveal our webhooks signing secret and add that to our Heroku config variables.


* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: gunicorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
* Log into GitHub or create an account.
* Locate the repository at https://github.com/KSheridan86/project-5-RossAnthonyDesigns .
* At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
* A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/KSheridan86/project-5-RossAnthonyDesigns
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine


[Back to the Top](#table-of-contents)

-----

## Credits

All Images used across the site are original and where created just for this project except for the header/footer background which was sourced from pexels.com.
The Black Icons used across the site were sourced from fontawesome and flaticon.com, attributions below.

- The Anvil Icon, (<a href="https://www.flaticon.com/free-icons/anvil" title="anvil icons">Anvil icons created by Agung Rama - Flaticon</a>) 
- The Back to Top Icon (<a href="https://www.flaticon.com/free-icons/double-arrow" title="double arrow icons">Double arrow icons created by Rahul Kaklotar - Flaticon</a>)
- Error 404 Icon (<a href="https://www.flaticon.com/free-icons/error-404" title="error 404 icons">Error 404 icons created by Freepik - Flaticon</a>)
- Server Error Icon (<a href="https://www.flaticon.com/free-icons/error" title="error icons">Error icons created by Pixel perfect - Flaticon</a>)
- Tick Icon (<a href="https://www.flaticon.com/free-icons/tick" title="tick icons">Tick icons created by kliwir art - Flaticon</a>)
- All other small images including Social media links were sourced from Font Awesome.

I relied heavily on the Code institute course work, particularly the Django walk through projects.
Further research was done by building walk through projects available freely on youtube and Dennis Ivy's Django/Python course on Udemy.

-----

## Acknowledgements

I would like to express my gratitude for the assistance and support provided by my colleagues and mentor. 
Additionally, I cannot overlook the immense help from my wonderful kids, who have been understanding and supportive throughout the day, making my work easier. This achievement would not have been possible without them.

-----


[Back to the Top](#table-of-contents)