YATRIGANN - Travel Service Portal
YATRIGANN is a full-stack web application designed for browsing and managing travel services such as flights and hotels. It provides a user-friendly interface for travelers and a comprehensive management dashboard for administrators to perform CRUD operations.

Table of Contents:
Introduction,
Features,
Tech Stack,
Installation,
Configuration,
Usage,
Database Schema.

Introduction:
The goal of this project is to simplify travel planning by centralizing flight and hotel information. Built using the Django framework, it ensures a secure and scalable environment for both users and administrators.

Features:
User Authentication,
Admin Dashboard,
Service Categorization,
Responsive UI,
Database Persistence.

Tech Stack:
Backend: Python 3.13, Django
Frontend: HTML5, CSS3, JavaScript, Bootstrap 5
Database: MySQL
Environment Management: Virtualenv

Installation:
Clone the repository: git clone https://github.com/Vishal0903aggarwal/YATRIGANN.git
Create and activate a virtual environment: python -m venv .venv .venv\Scripts\activate
Install the dependencies: pip install -r requirements.txt

Configuration:
Before running the server, ensure your MySQL database is running and update the settings.py file with your credentials:
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'yatrigann_db', 'USER': 'your_user', 'PASSWORD': 'your_password', 'HOST': 'localhost', 'PORT': '3306', } }
Run migrations to set up the database structure: python manage.py makemigrations python manage.py migrate
Create a superuser to access the admin panel: python manage.py createsuperuser

Usage:
Start the development server: python manage.py runserver
Access the website at: http://127.0.0.1:8000/ Access the management portal at: http://127.0.0.1:8000/bookings/admin-panel/

Future Work:
Integration of payment gateways.
Real-time flight tracking API.
User booking history and PDF ticket generation.
