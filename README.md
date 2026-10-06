# Bincom Python Basic Developer Test

This project contains my solution to the Bincom Python Basic Developer Test.

## Project Description

The program extracts the weekly shirt colour data from the provided HTML file and uses Python to analyse the data.

It also stores the colour frequencies in a PostgreSQL database.

## Main Questions

The program solves the following:

1. Mean colour
2. Most frequently worn colour
3. Median colour
4. Variance
5. Probability of RED
6. Saving colour frequencies to PostgreSQL

## Results

- Mean colour: PINK
- Most worn colour: BLUE
- Median colour: BLUE
- Variance: 7.6215
- Probability of RED: 9.47%

### Note on Mean, Median and Variance

Colours are categorical data and do not naturally have numerical values.

For the purpose of answering the test questions, I assigned numerical values to the colours based on their order of first appearance in the provided data. The mean, median and variance were then calculated using those numerical values.

The original colour names were preserved, including `ARSH` and `BLEW`, as they appeared in the provided HTML data.

## Bonus Questions

The bonus file contains solutions for:

- Recursive search
- Generating a random 4-digit binary number and converting it to base 10
- Sum of the first 50 Fibonacci numbers

## Technologies Used

- Python
- Regular Expressions
- PostgreSQL
- psycopg2
- python-dotenv

## Project Files

- `bincom_test.py` - Main solution for the test
- `bonus_questions.py` - Bonus questions
- `python_class_question.html` - Provided colour data
- `requirements.txt` - Python dependencies
- `.gitignore` - Files excluded from GitHub
- `.env` - Local database credentials; not uploaded to GitHub

## How to Run

Create and activate a Python virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt