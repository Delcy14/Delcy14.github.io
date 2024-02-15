import pandas as pd

# Function to initialize the contacts DataFrame
def initialize_contacts():
    return pd.DataFrame(columns=['Name', 'Address', 'Phone', 'Email'])

# Function to save contacts to a CSV file
def save_contacts(contacts_df):
    contacts_df.to_csv('contacts.csv', index=False)

# Function to load contacts from a CSV file
def load_contacts():
    try:
        return pd.read_csv('contacts.csv')
    except FileNotFoundError:
        return initialize_contacts()

# Function to add a new contact
def add_contact(contacts_df, name, address, phone, email):
    new_contact = pd.DataFrame([[name, address, phone, email]], columns=['Name', 'Address', 'Phone', 'Email'])
    contacts_df = pd.concat([contacts_df, new_contact], ignore_index=True)
    save_contacts(contacts_df)
    return contacts_df

# Function to display all contacts
def display_contacts(contacts_df):
    print(contacts_df)

# Function to update a contact
def update_contact(contacts_df, contact_index, new_name, new_address, new_phone, new_email):
    contacts_df.at[contact_index, 'Name'] = new_name
    contacts_df.at[contact_index, 'Address'] = new_address
    contacts_df.at[contact_index, 'Phone'] = new_phone
    contacts_df.at[contact_index, 'Email'] = new_email
    save_contacts(contacts_df)
    return contacts_df

# Function to delete a contact
def delete_contact(contacts_df, contact_index):
    contacts_df = contacts_df.drop(index=contact_index)
    save_contacts(contacts_df)
    return contacts_df

# Example usage
contacts_df = load_contacts()

# Add contacts
contacts_df = add_contact(contacts_df, 'John Doe', '123 Main St', '555-1234', 'john@example.com')
contacts_df = add_contact(contacts_df, 'Jane Smith', '456 Oak St', '555-5678', 'jane@example.com')

print("Contacts before update:")
display_contacts(contacts_df)

# Update a contact
contacts_df = update_contact(contacts_df, 0, 'John Updated', '456 Updated St', '555-9876', 'john.updated@example.com')

print("\nContacts after update:")
display_contacts(contacts_df)

# Delete a contact
contacts_df = delete_contact(contacts_df, 1)

print("\nContacts after delete:")
display_contacts(contacts_df)
