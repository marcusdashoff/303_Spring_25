def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""
    for char in input_text:
        if char in alphabet:
            index = (alphabet.index(char) + shift)
            if index >= len(alphabet):
                index -= len(alphabet)
            encoded_text += alphabet[index]
        else:
            encoded_text += char
    return (alphabet, encoded_text)

def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ""
    for char in input_text:
        if char in alphabet:
            index = (alphabet.index(char) - shift)
            if index < 0:
                index += len(alphabet)
            decoded_text += alphabet[index]
        else:
            decoded_text += char
    return decoded_text

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