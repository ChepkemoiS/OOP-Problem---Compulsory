# Competitive Eating Competition

Welcome to the Competitive Eating Competition!

## Overview

This project is a tool for judging a competitive eating competition. It helps create a scoreboard based on the points earned by participants for consuming different types of food.

## Features

- Calculate scores for participants based on the amount of chicken wings, hamburgers, and hotdogs consumed.
- Sort participants by their scores.
- Display the scoreboard with participants' names and scores.

## Installation

To use this tool, simply download or clone the repository to your local machine.

## Usage

1. Prepare a list of participants with details of the food they consumed.
2. Pass the list to the function `create_scoreboard(participants)`.
3. The function will return a sorted scoreboard with participants' names and scores.

## Example

```python
participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

scoreboard = create_scoreboard(participants)
print(scoreboard)
