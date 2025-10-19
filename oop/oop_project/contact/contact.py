class Contact:
    def __init__(self,name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
        
    def __display_info(self):
        return f'Name : {self.name}, email {self.email}, phone {self.phone} and address {self.address}'
        
    
    def __str__(self):
        return self.__display_info()
    
    


class ContactBook:
    def __init__(self,contacts = None):
        self.contacts = contacts if contacts is not None else {}
        
        
    def add_contact(self,contact):
        if contact.name in self.contacts:
            print(f'{contact.name} is already available')
        else:
            self.contacts[contact.name] = contact
            
    def show_all_contacts(self):
        if len(self.contacts) != 0:
            for contact in self.contacts.values():
                print(f'{contact}')
        else:
            print('No contact found')
            
    
    def find_by_name(self,name):
           if len(self.contacts) != 0:
                for contact in self.contacts.values():
                    if contact.name.lower() == name.lower():
                        print(f'Your requested name {name} is found')
                        return contact
                return f"Contact '{name}' not found."
        
        
book = ContactBook()
book.add_contact(Contact("Rahim","01711","rahim@mail.com","Dhaka"))
book.add_contact(Contact("Karim","01822","karim@mail.com","Chittagong"))
book.add_contact(Contact("Ali","01624","ali@mail.com","Natore"))

book.show_all_contacts()
print(book.find_by_name("Karimm"))
print(book.find_by_name("Ali"))