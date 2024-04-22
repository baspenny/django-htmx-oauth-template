# Incubeta - Django <> HTMX 🐶 Starter Template

This is a Python project that uses Django for web development.  
It is to show the capabilities of HTMX in a Django project.  
Styting is done using Bootstrap 5 (for now).

## Project Structure
- `core` contains the Django project files including the settings file
- `app/templates/base.html`: This is the base HTML file for the web application. It includes the main navigation and layout for the application.
- `app/models.py` contains a Profile that is linked to the built-in Django User. You can enrich this model to your specific use case

## Setup

1. Ensure you have Python and pipenv installed on your system.
2. Install the project dependencies using pipenv.
3. Copt the `.env.example` file to `.env` and fill in the required environment variables.
3. Create client credentials for the OAuth2 client and add them to the `.env` file.
4. Determine the authorized domains for the OAuth2 client and add them to the `.env` file under `GOOGLE_OAUTH2_WHITELISTED_DOMAINS`.  
   Leave blank to allow all domains.
    
## Running the Project

1. Create a new virtual environment using pipenv `pipenv install`.
2. Activate the virtual environment by running `pipenv shell`.
3. Create superuser using `python manage.py createsuperuser` and follow the prompts.
3. Run the migrations using `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.
6. Visit the application in your browser at `http://localhost:8000`.

> Please note if you use your Google Credentials and you want to open the admin page, that you elevate your user to `superuser` 
> in the database, so you can access the Django Admin


