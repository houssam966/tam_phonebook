# Django Phonebook App

This is a simple phonebook application built using the Django web framework. The app allows users to add contact names and associate them with multiple phone numbers. Users can also view a list of all contacts and view the details of individual contacts.

## Prerequisites

To run this application, you will need the following software installed on your system:

- Python 3.9 or later
- pip package manager
- Docker (optional, if you want to run the app in a container)

## Installation

1. Clone this repository to your local machine:

    `git clone https://github.com/houssam966/tam_phonebook.git`

2. Change into the project directory:

    `cd tam_phonebook`

3. (Optional) If you're using Docker, build and run the Docker container:

    `docker-compose up --build`

This will build the Docker image and start the container. You can access the Django phonebook app at `http://localhost:8000/phonebook/`. Any changes you make to the code will be automatically reflected in the running container.

4. (Alternative) If you're not using Docker, install the dependencies:

    `pip install -r requirements.txt`

5. Apply the database migrations:

    `python manage.py migrate`

6. Start the development server:

    `python manage.py runserver`

## Usage

Run the Django phonebook app and then:

1. Open your web browser and go to `http://localhost:8000/phonebook/`.

2. To add a new contact, click the "Add Contact" button or navigate to `http://localhost:8000/phonebook/add_contact/` and enter the contact name and phone numbers.

3. To view a list of all contacts, click the "Contacts" button or navigate to `http://localhost:8000/phonebook/`.

4. To view the details of an individual contact, click the contact's name in the contact list.

## DB SCHEMA


```
Table: "phonebook_contact"
 ----------
| id | name | 
 ----------
 ```

```
 Table: "phonebook_phonenumber"
  ---------------------
| id, number, contact_id | 
  ---------------------

  ```

 contact_id is a foreign key that references the id of a phonebook_contact. This schema allows multiple phone numbers for each contact.