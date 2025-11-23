Office management system.

A simple Python-based Office Management System to manage employees and tasks. This system allows admins and employees to perform basic management operations from the command line.

Features

Admin login to manage employees and tasks

Employee login to view tasks and details

Add, view, and delete employee records

Add and view tasks assigned to employees

Save and load data from a JSON file

Basic email and date validation

Tech Stack

Python 3.10+

hashlib for hashing passwords

email_validator for validating employee emails

JSON for storing employee and task data



How to Use

Admin Login

Username: admin

Password: admin123

Options:

Add employee

View employee details

Add tasks for employees

View all tasks

Delete employee

Employee Login

Username: employee

Password: employee123

Options:

View personal details

View assigned tasks

All data is stored in file.json and automatically loaded on program start.

Data Storage

Employee and task data are saved in a JSON file (file.json).

Employee IDs must start with EMP and task IDs must start with TSK.

Deadlines are validated to ensure they are not in the past.