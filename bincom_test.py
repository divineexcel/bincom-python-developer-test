import re
import psycopg2
import os
from dotenv import load_dotenv
from collections import Counter
load_dotenv()


from statistics import mean, median, variance
with open ("python_class_question.html", "r") as file:
    html = file.read()
    print(html)
rows = re.findall(r"<td>(.*?)</td>", html, re.DOTALL)
print(rows)

colors = rows[1::2]


all_colors = []

for i in colors:
    day_colors = i.split(", ")
    all_colors.extend(day_colors)

print(all_colors)
print(len(all_colors))

frequency = Counter(all_colors)
print(frequency)

most_worn = frequency.most_common(1)

print(most_worn)
# Colours are categorical, so I assigned each colour a number
# based on the order in which they first appear in the dataset.
colour_numbers = {
    "GREEN": 1,
    "YELLOW": 2,
    "BROWN": 3,
    "BLUE": 4,
    "PINK": 5,
    "ORANGE": 6,
    "CREAM": 7,
    "RED": 8,
    "WHITE": 9,
    "ARSH": 10,
    "BLEW": 11,
    "BLACK": 12
}

numbers = []

for i in all_colors:
    numbers.append(colour_numbers[i])

print(numbers)
print(len(numbers))

average = mean(numbers)
print("Mean:", average)

mean_colour = min(
    colour_numbers,
    key=lambda colour: abs(colour_numbers[colour] - average)
)

print("Mean colour:", mean_colour)

middle = median(numbers)

print("Median:", middle)

median_colour = min(
    colour_numbers,
    key=lambda colour: abs(colour_numbers[colour] - middle)
)

print("Median colour:", median_colour)

spread = variance(numbers)

print("Variance:", spread)

red_count = frequency["RED"]
total_colours = len(all_colors)

red_probability = red_count / total_colours

print("Probability of RED:", red_probability)


connection = psycopg2.connect(
    dbname="bincom_test",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port="5432"
)

print("Connected to PostgreSQL!")

cursor = connection.cursor()

for colour, count in frequency.items(): cursor.execute( """ INSERT INTO colour_frequency (colour, frequency) VALUES (%s, %s) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency """, (colour, count) )

connection.commit()

print("Colour frequencies saved successfully!")