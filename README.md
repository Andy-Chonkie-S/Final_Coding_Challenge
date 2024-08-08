# Final_Coding_Challenge
Develop a Python program with the Object-Oriented Programming paradigm, named my_record.py, that can read data from files and perform some operations on some datasets which discuss various sorting algorithms and their attributes.

**Student Name:** Andrew Sevilla

**Student ID:** s2010815T

**Repo Name:** Final_Coding_Challenge
**Short Description:** Last Python Programming Fundamentals Assignment, modifying and displaying various sorting algorithm datasets.

## Overview
This repository contains the code for the Final Coding Challenge of the Python Programming Fundamentals course (COSC2531). The assignment involves developing an application that can read data from files and perform some operations on some datasets which discuss various sorting algorithms and their attributes.

This Python script provides a framework for analyzing and reporting data from various sources. The core functionality is encapsulated within the `Records` class, which handles data ingestion, processing, and output.

It implements a basic taxi booking system with functionalities such as:

* Reading data from different file formats (currently supports CSV and JSON).
* Processing data to extract relevant information and perform calculations.
* Generating reports in various formats (currently supports text-based output).

**Download the full assignment spec:** [COSC2531_FinalCodingChallenge_Sem22023.pdf](COSC2531_FinalCodingChallenge_Sem22023.pdf)



**Key Features:**

## Code Structure

The program relies on several classes:

* `Operations`: Handles the main menu and user interaction.
* `Booking`: Represents a single taxi booking with customer, trip, and cost details.
* `Customer`: Represents a customer object with basic information and potential discount logic (base class).
* `BasicCustomer`: Inherits from `Customer`, representing a standard customer type.
* `EnterpriseCustomer` (not implemented): Could be added to represent a customer with a specific discount structure. (Consider adding this if planned for future development)
* `Location`: Represents a location object with an ID and name.
* `Rate`: Represents a rate type object with an ID and rate value.
* `Service`: Represents a service or package object with an ID, name, and price.
* `Package` (not fully implemented): Inherits from `Service`, potentially representing a service package with a list of included services and a discount mechanism.
* Various custom exception classes handle invalid user input (e.g., `InvalidCharactersException`, `InvalidDistanceException`, etc.).
* `results_file`: Required, specifies the input data file.
* `datasets_file` (optional): Provides dataset metadata.
* `algorithms_file` (optional): Contains algorithm-specific information.


* **Records:** The central class responsible for data ingestion, processing, and reporting.
* **Dataset:** Represents a dataset with ID and value.
* **DatasetInfo:** Contains metadata about a dataset (ID, name, complexity, etc.).
* **Algorithm:** Represents an algorithm with name, dataset list, and other potential attributes.
* **AlgorithmInfo:** (Optional) Contains metadata about an algorithm.

**Data Processing:**

The `Records` class performs the following tasks:

* Reads data from input files.
* Creates `Dataset` and `Algorithm` objects to represent data.
* Calculates statistics (e.g., average, range, number of failures).
* Generates reports in specified formats.

**Output:**

The script produces the following outputs:

* A summary of the data, including number of algorithms and datasets.
* A detailed table of results, showing algorithm performance on different datasets.
* Dataset information, including metadata and calculated statistics.


**Usage:**

1. Save the code as a Python file (e.g., `taxi_booking.py`).
2. Open a terminal window and navigate to the directory containing the file.
3. Run the program using the `python` command:

```
bash
python taxi_booking.py
```

## Dependencies
* Python (version 3.6+)
* `os` module (for file path handling)

## Known Issues

* Data validation and error handling could be improved.
* Algorithm information processing is not fully implemented.

## Additional Notes
* Do not use this code to cheat on your assignment, if similar. Cheating only cheats yourself!
  
