# py_Journal
Journal app written with python-tk

Simple journaling app adapted from Henry Smith's Journal available [here](https://github.com/HenrySmith3/Journal). Additionally, brought in check boxes taken from Mind Journal Jotter available [here](https://www.mindjournals.com/).

Running the app loads today's date with blank text and check boxes. If there was a main task in the previous day's file, that is loaded as the previous day's main task. Idea being that one can review the main task from the previous day and discuss what progress was made.

Date field is a label which can be modified by clicking the forward or backward arrows (to the right and left of the date respectively). One arrow ">" meaning to move one day and two arrows ">>" to move one week.

Data is stored in a text file for each day. The text is stored in the form of a python dictionary with keys for nonempty fields and values for the text (or 1 if the checkbox is checked).

Text and check-boxes are saved when the date is switched or when the user clicks the Save button.
