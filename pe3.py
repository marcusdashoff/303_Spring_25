import string
import datetime

def encode(input_text, shift):
    begin_position = ord('a')
    encoded_text = ""
    for char in input_text:
        if char.lower() in string.ascii_lowercase:
           new_position = (ord(char.lower()) - begin_position + shift) % 26 + begin_position
           encoded_text += chr(new_position)
        else:
            encoded_text += char
    return (list(string.ascii_lowercase),encoded_text)

def decode(input_text, shift):
    return encode(input_text, -shift)[1]

class BankAccount:
    def __init__(self, name = 'Rainy', id = '1234', created_date = datetime.date.today(), balance = 0):
        if not isinstance(created_date, datetime.date): 
            raise TypeError('wrong date type') 
        if created_date > datetime.date.today():
            raise ValueError('creation date cannot be futyre date of today') 
        self.name = name
        self.id = id
        self.created_date = created_date
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
        print(self.balance)
        
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        print(self.balance)
        
    def view_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        return super().withdraw(amount) if self.balance - amount >= 0 and (datetime.date.today() - self.created_date).days >= 180 else None

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 0:
            amount += 30 
        return super().withdraw(amount)
    