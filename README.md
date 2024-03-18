# CreamOS HTMX 🐶 Project

This is a Python project that uses Django for web development.  
It is to show the capabilities of HTMX in a Django project.

## Project Structure

- `app/templates/base.html`: This is the base HTML file for the web application. It includes the main navigation and layout for the application.
- `dump.json`: This file contains a dump of data in JSON format. It includes data for various models such as currency, exchange rate, license, advertiser, country, vat, and client.

## Setup

1. Ensure you have Python and pipenv installed on your system.
2. Install the project dependencies using pipenv.

## Running the Project

1. Create a new virtual environment using pipenv.
2. Activate the virtual environment by running `pipenv shell`.
3. Run the migrations using `python manage.py migrate`.
4. Load the data from the dump file using `python manage.py loaddata dump.json`.
5. Start the development server using `python manage.py runserver`.
