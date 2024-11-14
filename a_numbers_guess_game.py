{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww33400\viewh17760\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\tx12125\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\\\
import statistics\\\
\\\
def start_game():\\\
guesses = [] # Reset guesses for each new game\\\
print("Welcome to the guessing game!")\\\
solution = random.randint(1, 50)\\\
\\\
while True:\\\
try:\\\
guess = int(input("Please enter a number from 1 to 50: "))\\\
if guess < 1 or guess > 50:\\\
print("Please choose a number between 1 and 50.")\\\
continue\\\
except ValueError:\\\
print("Please enter a valid integer.")\\\
continue\\\
\\\
guesses.append(guess)\\\
\\\
if guess > solution:\\\
print("It's lower.")\\\
elif guess < solution:\\\
print("It's higher.")\\\
else:\\\
print("You guessed correctly!")\\\
break\\\
\\\
# Game stats\\\
print(f"It took you \\\{len(guesses)\\\} chances to guess correctly!")\\\
print(f"Mean of guesses: \\\{round(statistics.mean(guesses))\\\}")\\\
print(f"Median of guesses: \\\{statistics.median(guesses)\\\}")\\\
\\\
try:\\\
print(f"Mode of guesses: \\\{statistics.mode(guesses)\\\}")\\\
except statistics.StatisticsError:\\\
print("No single mode.")\\\
\\\
def replay():\\\
while True:\\\
answer = input("Would you like to continue playing? Y/N: ").lower()\\\
if answer == "y":\\\
start_game()\\\
elif answer == "n":\\\
print("Thank you for playing! Goodbye!")\\\
break\\\
else:\\\
print("Please choose Y or N")\\\
\\\
# Start the first game\\\
start_game()\\\
replay()\\\
\}}