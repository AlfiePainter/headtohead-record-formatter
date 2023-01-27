#Program to format head-to-head records JSON file in the style of sports
#reference websites using a 2d list
#Alfie Painter Sports Reference Engineering Internship Application Prompt

import json

#open and make JSON file a dictionary
records_data = open('head-to-head-records.json')
records = json.load(records_data)
records_list = [] #empty list to store records as 2d list

for i in records:
    team_wins = [] #empty list to store each teams' wins
    for j in records[i]:
        team_wins.append(records[i][j]["W"])
    #insert "--" where the team's head-to-head in the table would be itself
    team_wins.insert(list(records.keys()).index(i), "--")
    team_wins.insert(0, i)
    records_list.append(team_wins)

#add the teams at the top and bottom of the list
top_of_list = list(records.keys())
top_of_list.insert(0, "Tm")
records_list.insert(0, top_of_list)
records_list.append(top_of_list)

#print the 2d list for display purposes
for i in records_list:
    print(i)
