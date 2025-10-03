import unittest
from Password import Password
from Alphabet import Alphabet
from Generator import Generator


class GeneratorTest(unittest.TestCase):

    def setUp(self):
        # Set up test objects (like in your Java code)
        self.password = Password("Secret")
        self.firstAlphabet = Alphabet(True, False, False, False)
        self.secondAlphabet = Alphabet(False, True, True, True)
        self.generator = Generator(True, False, False, False)

    # Test case 1: Password string value
    def test1_password_to_string(self):
        self.assertEqual(str(self.password), "Secret")

    # Test case 2: firstAlphabet contains only uppercase letters
    def test2_first_alphabet_uppercase(self):
        self.assertEqual(self.firstAlphabet.get_alphabet(), Alphabet.UPPERCASE_LETTERS)

    # Test case 3: secondAlphabet contains lowercase + numbers + symbols
    def test3_second_alphabet_combined(self):
        expected = Alphabet.LOWERCASE_LETTERS + Alphabet.NUMBERS + Alphabet.SYMBOLS
        self.assertEqual(self.secondAlphabet.get_alphabet(), expected)

    # Test case 4: generator's alphabet contains only uppercase
    def test4_generator_uppercase_only(self):
        self.assertEqual(self.generator.alphabet.get_alphabet(), Alphabet.UPPERCASE_LETTERS)

    # Test case 5: length of generator's alphabet is 26
    def test5_alphabet_length(self):
        self.assertEqual(len(self.generator.alphabet.get_alphabet()), 26)


if __name__ == "__main__":
    unittest.main()
