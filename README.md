# Python Password Generator

A simple, interactive command-line password generator written in Python.

This project can:

- Generate strong, random passwords
- Check password strength and provide feedback
- Save generated passwords to a file for future reference
- Provide quick security tips

## Project structure

    Python-Password-Generator/
    ├── Alphabet.py        # Character sets (uppercase, lowercase, numbers, symbols)
    ├── Password.py        # Password object with strength evaluation
    ├── Generator.py       # Main logic: generate, check, save passwords
    ├── Main.py            # Entry point (runs the menu loop)
    ├── Generator-Test.py  # Unit test (may also appear under tests/)
    └── README.md          # Project documentation

## Features

- Uppercase letters (A–Z)
- Lowercase letters (a–z)
- Numbers (0–9)
- Symbols (e.g. !@#$...)

- Password strength evaluation with feedback
- Save generated passwords to your Desktop with a timestamp
- Easy-to-use menu interface

## How to run

1. Clone this repository:

```bash
    git clone https://github.com/TAENTED9/Python-Password-Generator.git
    cd Python-Password-Generator
```

2. Run the program:

```bash
    python Main.py
```

If you use Windows PowerShell and have multiple Python versions installed, you may need `python3` or the full path to your interpreter.

## Menu options

Menu options displayed by the program:

- Enter 1 — Password Generator
- Enter 2 — Password Strength Check
- Enter 3 — Useful Information
- Enter 4 — Quit

## Example usage

Generate a password:

```bash
    Choice: 1
    Do you want lowercase letters (e.g. "abcd...")? Yes
    Do you want uppercase letters (e.g. "ABCD...")? Yes
    Do you want numbers (e.g. "1234...")? Yes
    Do you want symbols (e.g. "!@#$...")? Yes
    Enter password length: 20

    Your generated password -> Ab7$k9@Q2...
    Generated password saved successfully to Desktop!
```

Check password strength:

```bash
    Choice: 2
    Enter your password: Secret123

    Weak password. Please improve it:
    - Add at least 2 symbols (e.g. !@#...)
```

## Running tests

Unit tests use Python's `unittest` framework. If tests are in a `tests/` folder, run:

```bash
python -m unittest discover tests
```

If a single test file is present (for example `Generator-Test.py`), run it directly:

```bash
python Generator-Test.py
```

## Useful information

Password security tips:

- Use at least 8 characters (more is better)
- Mix uppercase, lowercase, numbers, and symbols
- Don't reuse passwords across different accounts
- Avoid names, birthdays, dictionary words, or common sequences

## License

MIT License — feel free to use, modify, and share.
