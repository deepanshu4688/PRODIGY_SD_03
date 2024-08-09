
# PRODIGY_SD_03
Task-03

PRODIGY INFOTECH

Implement a Simple Contact Management System
Develop a program that allows users to store and manage contact information. The program should provide options to add a new contact by entering their name, phone number, and email address. It should also allow users to view their contact list, edit existing contacts, and delete contacts if needed. The program should store the contacts in memory or in a file for persistent storage.

1. Requirements and Overview

The Contact Management System (CMS) will have the following features:

    Add a new contact with name, phone number, and email address.
    View the entire contact list.
    Edit existing contact details.
    Delete contacts.
    Store contacts either in memory or in a file for persistent storage.

2. Data Structure

    Each contact will be represented as an object or a dictionary with keys for name, phone number, and email.
    The contact list can be an array (list) of these contact objects or dictionaries.

3. Functionalities
a. Add a New Contact

    Input: Name, phone number, and email address.
    Process: Create a new contact object and add it to the contact list.
    Validation: Ensure the phone number and email format are valid.

b. View Contact List

    Output: Display all contacts in a readable format.
    Process: Iterate through the contact list and print each contact's details.

c. Edit Existing Contact

    Input: Contact identifier (e.g., name or index), new name, phone number, or email.
    Process: Find the contact in the list, update the relevant fields with new data.
    Validation: Ensure updated details are valid.

d. Delete Contact

    Input: Contact identifier (e.g., name or index).
    Process: Locate the contact in the list and remove it.

e. Persistent Storage

    File Storage: Save contacts to a file (e.g., JSON, CSV) and load from it on program start.
    Process: Convert contact objects to a storable format and write to file. For reading, parse the file content and recreate contact objects.
