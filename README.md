### Date created
Project:  2021-02-14
README:   2021-03-16

### Project Title
EXPLORE US BIKESHARE DATA

### Description
This project uncovers bike share usage patterns in Chicago, New York City, and Washington by computing a variety of descriptive statistics.
The code provides the following information:

  #1 Popular times of travel (i.e., occurs most often in the start time)

      most common month
      most common day of week
      most common hour of day

  #2 Popular stations and trip

      most common start station
      most common end station
      most common trip from start to end (i.e., most frequent combination of start station and end station)

  #3 Trip duration

      total travel time
      average travel time

  #4 User info

      counts of each user type
      counts of each gender (only available for NYC and Chicago)
      earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Files used
Code file:
    bikeshare.py

City dataset files:
    chicago.csv
    new_york_city.csv
    washington.csv


### Credits
- Programming for Data Science with Python Udacity Nanodegree Program documentation

- pandas documentation:
https://pandas.pydata.org/pandas-docs/stable/reference/index.html

- to extract the existing months and days from data, and convert them into a list:
https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-a-list/

- to_string(): to remove Name and dtype from value_counts() output:
https://stackoverflow.com/questions/53025207/how-do-i-remove-name-and-dtype-from-pandas-output
