# Importing the necessary modules
import os
import re
import sys
from InquirerPy import prompt
from prompt_toolkit.validation import Validator, ValidationError

# Creating the contact and phonebook classes
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
# Defining what contacts should be consider equal
    def __eq__(self, other):
        return self.name == other.name

class PhoneBook:
    def __init__(self):
        self.contacts=[]

    def add_contact(self, Contact):
        if Contact not in self.contacts:
            self.contacts.append(Contact)
            print('Contact was successfully added.')
        else:
            print('This contact is already in your phonebook!')

    def delete_contact(self, Contact):
        if Contact in self.contacts:
            self.contacts.remove(Contact)
            print('Contact was successfully deleted.')
        else:
            print('This contact is not in your phonebook!')
# Making the phonebook object iterable
    def __iter__(self):
        return iter(self.contacts)

#Creating a function to validate the input phone numbers(only 11 digit numbers are valid)
class PhoneNumberValidator(Validator):
        
    def validate(self, document):
        match = re.search(r'^\d{11}$', document.text)
        if not match:
            raise ValidationError(
                message='Please enter a valid phone number!(11 digits)',
                cursor_position=len(document.text))  # Move cursor to end

def create_contact(name, number):
    contact = Contact(name, number)
    return contact

# Defining the prompts of the program
options = [
    {
        'type' : 'list',
        'name' : 'user_options',
        'message' : 'What do you wish to do?',
        'choices' : ['Add contact', 'Delete contact', 'Show contacts list', 'Exit program']
    }
]

input_name = [
    {
        'type' : 'input',
        'name' : 'name',
        'message' : 'Please enter the name:'
    }
]
input_number =[
    {
        'type' : 'input',
        'name' : 'number',
        'message' : 'Please enter the number:',
        'validate' : PhoneNumberValidator()
    }
    ]

def main():
    phone_book = PhoneBook() #Instantiating the PhonBook object

    #Creating the CLI
    while True:
        answer = prompt(options)
        user_option = answer.get('user_options')
        os.system('cls || clear') # Used both cls and clear so it would work on other os as well

        if user_option == 'Add contact':
            input_1 = prompt(input_name)
            input_2 = prompt(input_number)
            os.system('cls || clear')
            name = input_1.get('name')
            number = input_2.get('number')
            contact = create_contact(name, number)
            phone_book.add_contact(contact)
        elif user_option == 'Delete contact':
            input_1 = prompt(input_name)
            os.system('cls || clear')
            name = input_1.get('name')
            contact = create_contact(name, 0) # Passed zero as the number of the contact because contact number is not needed for deleting
            phone_book.delete_contact(contact)
        elif user_option == 'Show contacts list':
            print('Contacts:')
            if not phone_book.contacts:
                print('No contacts available.')
            else:
                for contact in phone_book.contacts:
                    print(f'{contact.name}: {contact.number}')
        elif user_option == 'Exit program':
            print('Good bye!')
            sys.exit()


if __name__ == '__main__':
    main()


   



