import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Define the path for the contacts file
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists.")
        return
    
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email address:")
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", "Contact added successfully.")

# Update the contact list in the main window
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

# View all contact details
def view_contact():
    if not contacts:
        messagebox.showerror("Error", "No contacts available.")
        return

    view_window = tk.Toplevel(root)
    view_window.title("View Contacts")

    view_frame = tk.Frame(view_window)
    view_frame.pack(pady=20)

    contact_details_list = tk.Listbox(view_frame, width=50, height=15)
    contact_details_list.pack(side=tk.LEFT, padx=10)

    scrollbar = tk.Scrollbar(view_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    contact_details_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=contact_details_list.yview)

    for name, info in contacts.items():
        contact_details_list.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    close_button = tk.Button(view_window, text="Close", command=view_window.destroy)
    close_button.pack(pady=10)

# Edit an existing contact
def edit_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showerror("Error", "No contact selected.")
        return
    
    phone = simpledialog.askstring("Input", "Enter new phone number (leave blank to keep current):")
    email = simpledialog.askstring("Input", "Enter new email address (leave blank to keep current):")
    
    if phone:
        contacts[selected_contact]["phone"] = phone
    if email:
        contacts[selected_contact]["email"] = email
    
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", "Contact updated successfully.")

# Delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showerror("Error", "No contact selected.")
        return
    
    del contacts[selected_contact]
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", "Contact deleted successfully.")

# Main GUI setup
contacts = load_contacts()
root = tk.Tk()
root.title("Contact Management System")

frame = tk.Frame(root)
frame.pack(pady=20)

contact_list = tk.Listbox(frame, width=50, height=15)
contact_list.pack(side=tk.LEFT, padx=10)
update_contact_list()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_list.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)

view_button = tk.Button(button_frame, text="View Contacts", command=view_contact)
view_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(button_frame, text="Edit Contact", command=edit_contact)
edit_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
