import string

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
    name = "Rainy"
    id = "1234"
    created_date = datetime.date.today()
    balance: int = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
    def view_balance(self):
        return self.balance