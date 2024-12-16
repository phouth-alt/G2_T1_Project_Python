# G2_T1_Project_Python
# User Authentication system
# Introduction
The User Authentication System is a Python-based application designed to handle user registration, login, password reset, and recovery functionalities. It ensures secure access management through encrypted passwords, password strength validation, and OTP-based recovery mechanisms.

## Features
1.Login: Allows users to securely log in using their credentials.
2.Register: New users can register by providing a username, password, and phone number.
3.Reset Password: Enables users to reset their password after verifying their identity.
4.Forget Password: Recover accounts using an OTP sent to the registered phone number.
5.Password Encryption: Ensures passwords are securely stored using encryption.
6.Password Strength Validation: Validates that passwords meet complexity requirements.
6.OTP Generation: Provides secure alphanumeric OTP for authentication during recovery.

## Prerequisites
-Python 3.7+: Ensure Python is installed on your system.
-Modules/Functions used in the system:
    -register: Handles user registration.
    -reset_pass: Manages password reset.
    -login: Validates user credentials.
    -recover_password: Handles account recovery.
    -generateOTP: Generates secure OTPs.
    -update_password: Updates user passwords in the database.
    -encrypt_password: Encrypts passwords before storage.
    -pass_strength: Checks the strength of new passwords.

## Installation 
1. Clone the repository:
```bash
git clone https://github.com/phouth-alt/G2_T1_Project_Python.git
```
2.Navigate to the project directory:
```bash
cd G2_T1_Project_Python
```
3.Install any required dependencies (if applicable):
```bash
pip install os
pip install secrets
pip install string
pip install re
pip install hashlib
```

## Usage
1. Run the program
```bash
python main.py
```
2. Follow the on-screen menu to perform the desired operations:

-Login: Enter your username and password.

-Register: Provide your username, password, and phone number.

-Reset Password: Enter your current credentials and set a new password.

-Forget Password: Use your phone number to recover your account.


## Security Measures

1. Password Encryption:
-All passwords are encrypted before storage to prevent unauthorized access.
2.Password Strength Enforcement:
-Ensures new passwords meet complexity requirements to enhance security.
3.OTP Recovery:
-Uses secure, alphanumeric OTPs for password recovery.
4. Input Validation:
-Validates user inputs (e.g., phone numbers, usernames) to prevent injection attacks.

### Future Improvements
-Integrate with a database for better scalability.
-Implement email-based OTPs for account recovery.
-Add rate-limiting to prevent brute force attacks.
-Introduce logging for audit trails and error monitoring.

### Contributing
Contributions are welcome! Please follow these steps:
1.Fork the repository.
2.Create a feature branch:
```bash
git checkout -b feature-name
```
4.Commit your changes and push to your fork.
4Open a pull request.

### Contact
For any questions or issues, please contact:
Your Name: your.email@example.com
[GitHub Repository](https://github.com/phouth-alt/G2_T1_Project_Python.git)