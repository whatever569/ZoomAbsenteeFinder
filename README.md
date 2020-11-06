# Absentee finder
## Created using:
- Python 3
- Pytesseract
- PIL

## Description:
This is a simple script made to find absentees from a meeting through text recognition; the final project for the CS50 course... it was created after I saw a problem in my online school, where valuable time was being spent on counting the absentees from our Zoom class instead of it being spent on actual learning.

So I used Zoom's feature of it showing a list of current participants, taking a screenshot of the list and then using python tesseract text recognition to... well recognize the text in the screenshot... the recognized text was processed by capatilizing it and removing any non-alphabetical characters from it, that processed text was compared to a list of known names (which was also processed), any missing name from the sequence of letters was then appended to list of absentees that was printed in the console.

## Requirments:
The participants should all conform to a certain way of spelling their name, so to not be always be written as "absent".
