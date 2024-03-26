# Incubeta - Django <> HTMX 🐶 Starter Template

This is a Python project that uses Django for web development.  
It is to show the capabilities of HTMX in a Django project.  
Styting is done using Bootstrap 5 (for now).

## Project Structure

- `app/templates/base.html`: This is the base HTML file for the web application. It includes the main navigation and layout for the application.
- `dump.json`: This file contains a dump of data in JSON format. It includes data for various models such as currency, exchange rate, license, advertiser, country, vat, and client.

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
4. Load the data from the dump file using `python manage.py loaddata dump.json`.
5. Start the development server using `python manage.py runserver`.
6. Visit the application in your browser at `http://localhost:8000`.
