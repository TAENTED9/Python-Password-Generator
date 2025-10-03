class Alphabet:
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    SYMBOLS = "!@#$%&_"

    def __init__(self, use_upper, use_lower, use_numbers, use_symbols):
        self.pool = ""
        if use_upper:
            self.pool += self.UPPERCASE
        if use_lower:
            self.pool += self.LOWERCASE
        if use_numbers:
            self.pool += self.NUMBERS
        if use_symbols:
            self.pool += self.SYMBOLS

    def get_alphabet(self):
        return self.pool
