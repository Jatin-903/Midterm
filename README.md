# Midterm
# Project Documentation for the Calculator  

## Table of Contents  

- [Overview](#overview)  
- [Features](#features)  
- [Architecture](#architecture)  
  - [Design Patterns](#design-patterns)  
  - [Logging Strategy](#logging-strategy)  
- [Setup Instructions](#setup-instructions)  
- [Usage](#usage)  
- [License](#license)  

## Overview  

This Python-based calculator application is designed to perform various mathematical operations. It features a dynamic plugin system that allows for easy expansion by adding new operations without modifying the core code.  

## Features  

- Basic arithmetic operations (addition, subtraction, multiplication, division)  
- Plugin-based architecture for adding new operations dynamically  
- Comprehensive logging to track operations and facilitate debugging  

## Architecture  

### Design Patterns  

The project incorporates several design patterns to enhance maintainability and scalability:  

1. **Strategy Pattern**  
   - Defines a set of interchangeable algorithms (operations), allowing seamless switching between different operations without modifying core functionality.  
   - **Benefit**: Enables adding new operations as plugins without altering existing code, adhering to the Open/Closed Principle.  

2. **Singleton Pattern**  
   - Applied to the logger class, ensuring a single instance of the logger is used throughout the application.  
   - **Benefit**: Centralizes logging, reduces memory usage, and simplifies log management.  

### Logging Strategy  

The application utilizes Python’s built-in logging module to provide operational insights.  

- **Implementation**:  
  - Configured to capture logs at various levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).  
  - Logs are stored in a file to maintain a history of calculations and track issues.  

- **Benefit**:  
  - Enables easy debugging and monitoring, ensuring maintainability and reliability.  

## Setup Instructions  

To set up the project locally, follow these steps:  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/Jatin-903/Midterm
   cd Midterm-Project
   ```  

2. **Create a virtual environment**:  
   ```bash
   python -m venv venv
   ```  

3. **Activate the virtual environment**:  
   - Windows:  
     ```bash
     venv\Scripts\activate
     ```  
   - macOS/Linux:  
     ```bash
     source venv/bin/activate
     ```  

4. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```  

## Usage  

### Basic Operations  
- Supports addition, subtraction, multiplication, and division.  
- Users input numbers and select the desired operation via terminal prompts.  

### Command-Line Interface  
- Displays available operations upon launch.  
- Users follow on-screen instructions to perform calculations.  

### Adding New Operations via Plugins  
- Dynamically loads newly developed plugins at runtime.  
- For example, a power operation plugin can be loaded and used without modifying existing code.  

### Example Usage  
1. Start the application with `python main.py`.  
2. Select 'add' for addition.  
3. Enter `5` and `3` when prompted.  
4. The calculator returns the result: `8`.  

### Error Handling  
- Invalid inputs (e.g., non-numeric values) prompt users to enter valid numbers.  

## Design Patterns Implementation  

This project implements the **Factory Design Pattern** to manage the creation of operation classes (addition, subtraction, multiplication, division). This facilitates scalability when introducing new operations.  

**Reference**: [Factory Design Pattern](https://refactoring.guru/design-patterns/factory-method)  

## Environment Variables Usage  

Environment variables are used for handling sensitive configurations such as API keys and database URLs. The `dotenv` library loads these variables at runtime, enhancing security and maintainability.  

**Reference**: [Environment Variables](https://pypi.org/project/python-dotenv/)  

## Logging  

The application employs Python’s built-in `logging` module to track events and errors. This improves debugging and performance monitoring.  

**Reference**: [Logging in Python](https://docs.python.org/3/library/logging.html)  

## Exception Handling  

The project follows both the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) paradigms:  

- **LBYL**: Ensures checks are performed before executing operations (e.g., verifying that the denominator is nonzero before division).  
- **EAFP**: Uses exception handling to gracefully manage errors without disrupting execution.  

**Reference**: [Exception Handling](https://realpython.com/python-lbyl-vs-eafp/)  

## Video Demonstration
A video demonstration of the calculator has been created to showcase its key features and functionalities.

Video Link: [Calculator Demonstration Video] ## Video Demonstration
A video demonstration of the calculator has been created to showcase its key features and functionalities.

Video Link: [Calculator Demonstration Video] https://youtu.be/PsY-wt1SrB8

## License  

This project is distributed under the MIT License. For details, refer to the [LICENSE](LICENSE) file.