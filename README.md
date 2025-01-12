# ElGamalCryptosystem

## DESCRIPTION
This is a Python-based graphical user interface (GUI) application that implements the ElGamal Cryptosystem for encrypting and decrypting messages. The application allows you to generate random prime numbers, primitive roots, and exponents, as well as manually enter these values. It also offers the option to divide the message into blocks of one or two characters for encryption.

## FEATURES
Random Value Generation: Automatically generates prime numbers, primitive roots, and exponents for encryption/decryption.

Manual Entry: Allows users to manually input prime numbers, primitive roots, and exponents.

Block Division: Option to divide the message into blocks of one or two characters.

Message Encryption: Encrypts messages based on the provided values.

Message Decryption: Decrypts messages using the encrypted blocks and the generated keys.

User Interface: Simple GUI for user interaction, built with tkinter.

Reset and Exit Options: Reset all input fields or exit the application easily.

## REQUERIMENTS
Python 3.x

tkinter (included with standard Python installation)

random module (included with standard Python installation)

PyInstaller (for creating an executable)

## INSTALLATION
1. Clone the repository: git clone [https://github.com/j-espinoza19/elgamal-cryptosystem.git](https://github.com/j-espinoza19/ElGamalCryptosystem) cd elgamal-cryptosystem
2. Run the Application: python elgamal_gui.py

## USING
Open the Application: Run the script elgamal_gui.py to open the GUI application.

Block Division Size: Choose the block division size by selecting either "Single Block" or "Double Blocks".

Generate Random Values: Click on "Generate Random" to auto-fill the fields with random prime number, primitive root, and exponent.

Manual Entry: Fill in the fields "Prime p:", "Root g:", and "Exponent e:" manually and click on "Enter Manually" to validate and use these values.

Encrypt Message: Enter the message you want to encrypt in the "Message" field and click "Encrypt". The encrypted message will be displayed in the "Encrypted Message" field.

Decrypt Message: Enter the encrypted message in the "Encrypted Message" field and click "Decrypt". The decrypted message will be displayed in the "Decrypted Message" field.

Show Values: Click "Show Values" to display the values of x, p, g, k, and i used during encryption.

Reset: Click "Reset" to clear all input fields and messages.

Exit: Click "Exit" to close the application.

## CODE STRUCTURE
The code is separated into two main parts:

elgamal_functions.py: This file contains all the functions used in the program.

elgamal_gui.py: This file contains the graphical user interface (GUI) and uses the functions imported from elgamal_functions.py.

## AUTHORS
Arnau Cano Torra & Josueth Espinoza Bravo

UPC-EPSEM students. Industrial and automatic electronic engineering

## CONTACT
arnau.cano@estudiantat.upc.edu

josueth.rafael.espinoza@estudiantat.upc.edu
