# Code Lab: Developing a Python Data Analysis Script with Pandas

In this lab, you'll build a data analysis script that reads a CSV file containing sales data, performs analysis, and creates visualizations to extract business insights. The lab walks learners through building a data analysis script step-by-step, with each task focusing on a specific action.

## Getting Started

### Prerequisites

- Basic knowledge of Python syntax and functions
- Familiarity with simple data structures like lists and dictionaries
- Understanding of programming concepts like loops and conditionals
- No prior experience with pandas or data visualization is required

## File Tree Structure

```
workspace/
├── src/
│   ├── main/
│   │   └── python/
│   │   	├── sales_analysis.py
│   │   	└── test_sales_analysis.py
│   └── unittests/
│   	├── task_1.1_unittest.py
│   	├── task_1.2_unittest.py
│   	├── task_1.3_unittest.py
│   	├── task_2.1_unittest.py
│   	├── task_2.2_unittest.py
│   	├── task_3.1_unittest.py
│   	├── task_3.2_unittest.py
│   	├── task_3.3_unittest.py
│   	├── task_4.1_unittest.py
│   	├── task_4.2_unittest.py
│   	├── task_4.3_unittest.py
│   	├── task_5.1_unittest.py
│   	├── task_5.2_unittest.py
│   	└── task_5.3_unittest.py
└── resources/
	└── sales_data.csv

```

## Files Required for the Lab

- **`sales_analysis.py`** - This is the main file where learners will implement their data analysis functions
- **`sales_data.csv`** - The sample sales data file that learners will analyze
- **`test_sales_analysis.py`** - Contains unit tests to validate learners' implementations

When learners start working on tasks, they'll primarily be editing the `sales_analysis.py` file, implementing the various functions defined in the Code Lab instructions. They'll also be able to run their code to see the output in the terminal and validate their implementations against the provided tests.

### Setup Instructions

This lab can be run on any environment - Windows (command prompt), Linux or MacOS terminal. Here I've provided the setup instructions for both Windows and Unix-based systems with Python installed:

1. Make sure you have Python 3.8+ installed
2. Install required packages:
   ```bash
   pip install pandas matplotlib numpy
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/AngelSayani/Code-Lab-Developing-a-Python-Data-Analysis-Script-with-Pandas.git
   cd Code-Lab-Developing-a-Python-Data-Analysis-Script-with-Pandas
   ```
4. Run the main script:
   ```bash
   python src/main/python/sales_analysis.py
   ```

5. Run the test script to validate:
   ```bash
   python src/main/python/test_sales_analysis.py
   ```

6. To run a unit test for any specific task, run the following command and append with corresponding task number:
   Example: To run unit test for task 1.1 and task 5.2:
 ```bash 
   python src/main/unittests/task1.1_unittest.py
   python src/main/unittests/task5.2_unittest.py
```
---

## File Contents

These files provide a complete foundation for the lab:

- **`sales_data.csv`** contains realistic sales data with dates, products, categories, sales amounts, and quantities.
- **`sales_analysis.py`** is the template file where learners will add their code, with commented placeholders for each task.
- **`test_sales_analysis.py`** contains unit tests to verify that the learners have correctly implemented the `load_data` and `clean_data` functions.

The test file creates a temporary CSV file for testing and checks that:
- The data loading function properly reads CSV data into a DataFrame
- The data cleaning function removes rows with missing values
- The cleaning function correctly converts dates to datetime objects
- The cleaning function adds a Month column as required

## Unit Testing

The "Unit Test for Data Loading Function" section is specifically designed to test the data loading and cleaning functions that the learner will implement.

In the context of the Code Lab:

- **Purpose**: This unit test validates that the learner has correctly implemented certain functions in their code.
- **How it's used**: The test checks if the learner's implementation of the `load_data` and `clean_data` functions works correctly. It verifies that:
  - The CSV data is loaded properly
  - The DataFrame structure is correct
  - The data cleaning operation handles missing values
  - Date formatting and new column creation work as expected
- **Where it belongs**: The content of this test should be placed in the `test_sales_analysis.py` file.
- **Running the test**: In the lab environment, there would likely be a validation step where this test is run automatically to check the learner's work. The learner can also run the test themselves using a command like:
  ```
  python src/main/python/test_sales_analysis.py
  ```



