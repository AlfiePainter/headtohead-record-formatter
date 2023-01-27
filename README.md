# headtohead-record-formatter
For the Sports Reference Engineering Internship Application Prompt

Given a JSON file, I read it as a nested dictionary. The goal is to create a 2D array that works as a matrix. 
To do this, I create an empty list for future list insertion.
I create a nested for loop that creates an empty list for each team and then inserts every head-to-head wins into that list, 
before adding that list to the 2D list for all records. 
After the loop, add a list of the teams at the top and bottom of the 2D list to match the formatting of Sports Reference tables
