# Password Encryption and Management Tool

This project provides a simple command-line tool for encrypting and decrypting passwords using the `cryptography` library in Python. The tool also demonstrates how to store and manage encrypted passwords within a pandas DataFrame securely.

## Features

- **Password Encryption:** Encrypts plain-text passwords using the Fernet symmetric encryption.
- **Password Decryption:** Decrypts encrypted passwords back to plain text.
- **Data Management:** Stores passwords, encrypted passwords, and encryption keys in a pandas DataFrame.
- **User Interaction:** Provides a command-line interface for adding and retrieving passwords.

## Requirements

- `Cryptography`
- `pandas`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmed-hesham07/password-encryption-decryption.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-encryption-decryption
   ```
3. Install the required packages:
   ```bash
   pip install cryptography pandas
   ```

## Usage

1. Run the script:
   ```bash
   python password_encryption_decryption.py
   ```

2. Follow the on-screen instructions:
   - **Add Password:** Allows users to input a password, encrypt it, and store it in the DataFrame.
   - **Get Password:** Allows users to retrieve the original password using the encrypted password.
   - **Exit:** Exit the application.

## Notes

- Ensure the encryption key is securely stored and managed. For simplicity, the key is generated within the script and used directly.
- The current implementation uses global variables and a simple command-line interface. For a more robust application, consider adding proper error handling, data validation, and potentially a more sophisticated user interface.
