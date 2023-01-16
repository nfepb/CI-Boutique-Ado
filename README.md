![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

This is the Code Institute student template for Gitpod. 

# Questions to ask when building eCommerce website:

1. Which ecommerce app types apply to this website? 
    * **B2C** focus, **Products** are being sold by the organisation, requires **Single Payment**
2. With the ecommerce types in mind, what kind of features might be included within the business website? 
    * Easy payment gateway
    * Authentification system 
        * for creating an account
        * for logging in / out
        * seeing previous purchases
    * Search and filter functionalities
    * Clear product descriptions
    * Ratings or reviews
    * Shopping cart and payment system
3. What tables of data would your database need, and what data might be included in these tables? 
    * **User**
        * username
        * email
        * password
    * **Product**
        * name
        * image
        * price
        * description
        * rating
        * category
    * **Order**
        * User [FK User]
        * total
        * full_name
        * address
    * **OrderItem**
        * Order [FK Order]
        * Product [FK Product]
        * quantity

# User Stories 

[User Stories Boutique Ado 1/3]! (assets/images/user-stories-boutique-ado-1.png)
[User Stories Boutique Ado 2/3]! (assets/images/user-stories-boutique-ado-2.png)
[User Stories Boutique Ado 3/3]! (assets/images/user-stories-boutique-ado-3.png)

## Order of user stories:

1. Registration & User Accounts
2. Viewing & navigation (navbar)
3. Mock product and images data with JSON files + images
4. Admin views for product and category management
5. Creates product app, adds urls, new templates for products and structure with style in products.html.
6. Story #2: view product details
    * Create product_detail view in app
7. View & filter categories + stories # 14 & 15 for the search queries
    * Adds filter to Views
    * Adds category filtering in url in html
    * Adds view in all_products def.
    * Adds sorting for price, rating, etc in main-nav. Adds views
8. Create bag app
    * Add url file
    * Add view
    * Add templates & bag folders & bag html
    * Add app to installed apps + to urls.py of project
    * update bag.html
    * Adds form to product_detail
    * display total cost on navbar icon
    * Adds size to product model and displays on details + bag pages
    * Adds update & remove links on bag page
    * Adds subtotal calculation
9. Adds Totast and Django message to communicate with the user
    * Adds toast folder in templates/includes
    * Updates CSS
    * Adds if logic to base.html
    * Updates views for when messages should be displayed
    * Adds checkout preview
10. Checkout Page - User Story 19 --> 22 using Stripe and sending confirmation email.
    * Create Order model
    * Adds models to admin views
    * Create the order form
    * Add logic that will calculate total each time an items is added or removed.
    * Create checkout app
    * create form and view
    * create html based on bag
    * create separate static/css folder with css file for checkout page
    * install django-crispy-forms
    * Adds crispy forms to installed apps & builtins for load on every template
11. Integration with Stripe
    * Add JS Script to base.html
    * Add stripe variables to views.py
    * Create js file and style cards
    * Install stripe package
    * Style elements & adds variables to settings
    * Export STRIPE_PUBLIC_KEY & STRIPE_SECRET_KEY with `export STRIPE_PUBLIC_KEY=XXXXXX` --> put in env.py file
    * Adds checkout method to checkout/views.py. Verify in Stripe events that payment intents are "success"
    * Create checkout_success.html page
    * Add webhooks to handle events
    * Create code to create any necessary database objects in the webhook handler
    * Handle checkbox "save my info"
    * Deal with cache and introduce dealy to have clean DB and avoid mistakes/errors
    * Updates Order model for unique identification when going over webhook_handler cache loop --> allows user to order the same order and not being created.
12. Profile App - User Stories 10 - personalized user profile
    * Installs Django Country picklist with `pip3 install django-countries==7.2.1`
    * Creates profiles app with `python3 manage.py startapp profiles` & add to settings installed apps
    * Create user model & relationship to other objects (order)
    * Updates urls 
    * Creates the views for userprofile
    * Creates html & css files.
    * Modifies allauth/base & allauth/account/base templates
    * Updates CSS
    * Fix superuser login by creating an associated profile
    * Creates forms.py from checkout/forms.py
    * update views.py with form info
    * add js for countryfield
    * Update order history display on profile.html
    * Adds confirmation email in webhook handler because this is where we know where the payment took place.
    * `export STRIPE_WH_KEY="" ` + check site URL to make sure the url is the same as webhook URL Stripe: `https://8000-nfepb-ciboutiqueado-e69p4pes8p1.ws-eu82.gitpod.io/checkout/wh/`
13. Provide additional functionalities to our users & superusers
    * Create forms.py in products app.
    * Create html page to add_product
    * Add success & fail messages for product add and profile update
    * Add noimage in toast_success.html & templates/toast/toast_success & bag
    * Create edit_product.html, update views & url to allow modification of product listing
    * Add URL in products/url to allow deletion of products & link for action on product_details page & product templates.
    * Updates security to avoid users to post of edit products without propoer accreditation
        * imports login_required decorator in product & profile views
    * Creates CustomClearableFileInput widget in products for better UI when uploading a product image.
    * Improves UI for image field in edit product pages.
14. Deployment
    * Create an external database. For this we’ll use ElephantSQL, as the Heroku add-ons are not available on the Student Pack.
        1. start by creating a database and connecting it to a new app on Heroku. We will also connect it to our Gitpod workspace temporarily so we can make migrations.
        2. log in to ElephantSQL.com
        3. Click on 'Create New Instance'
        4. Select plan
        5. Define project name.
        6. Select plan Tiny Turtle (Free)
        7. Select the region for deployment.
        8. Click on 'Review'.
        9. Check details and click on 'Create instance'.
        10. From the ElephantSQL dashboard, click on the database instance for the project.
        11. Copy the database URL.
    * Create an app on Heroku, as we have done for previous projects.
        1. Click on 'New' to create a new app.
        2. Define the name for the app & select the region the closest.
        3. In the app's settings, add the config vars:
            - `DATABASE_URL`: the value is the URL instance link from ElephantSQL.
        4. Prepare the local project for migration.
            - In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to the external database: `pip3 install dj_database_url==0.5.0 psycopg2`
            - Update the requirements.txt file with the newly installed packages: `pip freeze > requirements.txt`
            - In your settings.py file, import dj_database_url underneath the import for os: 
                ` import os
                import dj_database_url`
        5. In the DATABASES section and update it to: 
            <code># DATABASES = {
                #     'default': {
                #         'ENGINE': 'django.db.backends.sqlite3',
                #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                #     }
                # }
                    
                DATABASES = {
                    'default': dj_database_url.parse('your-database-url-here')
                }
            </code>
            so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated.
            /!\ DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations. We will remove it in a moment.
        6. In the terminal, run the showmigrations command to confirm you are connected to the external database:<br>
            `python3 manage.py showmigrations`
        7. Migrate your database models to your new database<br>
            `python3 manage.py migrate`
            - Load in the fixtures. Please note the order is very important here. We need to load categories first<br>
            `python3 manage.py loaddata categories`
            - Then products, as the products require a category to be set<br>
            `python3 manage.py loaddata products`
            - Create a superuser for the new database<br>
            `python3 manage.py createsuperuser`
        8. Finally, to prevent exposing our database when we push to GitHub, we will delete it again from our settings.py - we’ll set it up again using an environment variable in the next video - and reconnect to our local sqlite database. For now, your DATABASE setting in the settings.py file should look like this
        <code>
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }</code>
        9. Let’s confirm that the data in your database on ElephantSQL has been created. On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”.
        10. Click the Table queries button, select auth_user.
        11. When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database.
    * Deploy to Heroku
        1. Modify DATABASE_URL in settings.py based on where the app is ran:<br>
        <code>if 'DATABASE_URL' is os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
            </code>
                2. Install gunicorn to act as webserver: `pip3 install gunicorn` & freeze in requirements file with `pip3 freeze >requirement.txt`.
                3. Create Profile to tell Heroku to create a web dynoand add: `web: gunicorn boutique_ado.wsgi:application` to run Gunicorn and will run our Django app.
                4. Login to Heroku with `heroku login -i`
                5. Initialize heroku git remote with `heroku git:remote -a [yourgitreponame]`
                5. Disable collectstatic for deployment to Heroku: `heroku config: set DISABLE_COLLECTSTATIC=1 --app [name-of-your-app-in-heroku]`
                6. In settings.py, add `'localhost'` & `'[location-of-your-app-in-heroku]'`.
    * Set up hosting for our static and media files with AWS (Amazon Web Services). Specifically, we will use S3 (“Simple Storage Service”) for this.
    

# Deployment
Django `startproject boutique_ado` steps
Copy Allauth files in directory templates with command `cp -r /workspace/.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth`
Deleting OpenId & tests files with templates because not handled in this project. This sets them back to their Allauth defaults.
Manually create a project level base.html template directory, out of which all templates will be based on.
Uses the boilerplate from the Bootstrap website in the base.html. 


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
