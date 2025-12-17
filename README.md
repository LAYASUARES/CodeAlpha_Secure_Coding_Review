# Secure Coding Review — Code Explanation

This project is a deliberately vulnerable Python application created for educational purposes, with the goal of identifying, analyzing, and documenting common security vulnerabilities through manual code review.

The application provides a menu-based interface that allows user interaction with different functionalities, some of which intentionally lack proper input validation and security controls.

---

## Project Structure

The application is divided into multiple files to simulate a real-world modular codebase:

  • main.py – Controls program flow and user interaction
  • database.py – Handles database operations related to users
  • file_handler.py – Manages file reading functionality
  • system_utils.py – Executes system-level commands

```
│── main.py 
│── database.py
│── file_handler.py
│── system_utils.py
│── users.db
└── README.md
```

---

## How the Application Works

**main.py**

This file is the entry point of the application.
It displays a menu, receives user input, and routes execution to the appropriate functions.

The menu provides the following options:

  1. Add a user
  2. Search for a user
  3. Read a file
  4. Run a system command
  5. Exit the application

Each option directly calls a corresponding function from another module.

The application runs in a continuous loop until the user chooses to exit.

---

**database.py**

This module is responsible for user data management using a local SQLite database.

Main functionalities include:

  • Creating a user table (if it does not exist)
  • Inserting user-provided data into the database
  • Searching users based on input values

User input is passed directly into SQL queries, which makes this module suitable for demonstrating input validation and injection risks during a security review.

---

**file_handler.py**

This module contains a function that reads and returns the contents of a file specified by the user.

The function:

  • Accepts a filename as input
  • Attempts to open and read the file
  • Returns the file contents or an error message

There is no validation of file paths, which allows the user to attempt reading files outside the application directory, demonstrating a Path Traversal / Arbitrary File Read vulnerability.

---

**system_utils.py**

This module provides functionality to execute system commands.

The function:

  • Accepts a command as user input
  • Executes the command directly using the operating system
  • Returns the command output

Because the input is not sanitized or restricted, this module demonstrates a Command Injection vulnerability, allowing execution of arbitrary system commands.

---

## Security Perspective

From a security standpoint, this application intentionally violates secure coding principles such as:

  • Input validation
  • Least privilege
  • Safe handling of system resources

These weaknesses make the application suitable for:

  • Manual code review exercises
  • Static analysis demonstrations
  • Security training and educational labs

---

## Disclaimer

This application was created strictly for educational and learning purposes.
It should never be used in production environments.

---

# Conclusion

This project demonstrates how insecure coding practices can introduce serious security risks.
By reviewing and testing this code, it is possible to identify vulnerabilities, understand their impact, and propose remediation strategies aligned with secure coding best practices.

---
 
## How to Run the Application

### 1. Clone or download the project

```bash
git clone <repositorio>
cd Secure_Coding_Review
```

---
👌🤞
