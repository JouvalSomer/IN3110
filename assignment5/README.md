# README.md Assignment4

## Prerequisites
Install all prerequisites using the requirements.txt file.
Put requirements.txt in the directory where the command will be executed. If it is in another directory, specify its path like path/to/requirements.txt and run for example the command:
```
pip install -r requirements.txt
```

## Functionality

### Task 5.1
In this task the function get_html takes a url and some optional arguments, params and output, and returns the url and its html content.

There is also generated a folder, requesting_urls, containing three files each containing the function output from the example websites.
Example websits:
- https://en.wikipedia.org/wiki/Studio_Ghibli
- https://en.wikipedia.org/wiki/Star_Wars
- https://en.wikipedia.org/w/index.php

### Task 5.2
In this task the function find_urls takes a html string and returns all valid URLs within that string. Then the function find_articles takes a html string, uses the find_urls function to get a lit of urls, loops through those, and select the urls that are wikipedia articles.

There is also generated a folder filter_urls containing six files each containing a list of the urls and articles returned for each of the three example websites.
Example websites:
- https://en.wikipedia.org/wiki/Nobel_Prize
- https://en.wikipedia.org/wiki/Bundesliga
- https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup

### Task 5.3
The function find_dates takes a string of html, uses regex to pars the string to find all dates of the form DMY, MDY, YMD and ISO. Then it formats them as YYYY/MM/DD, and returns them. The find_dates uses task 5.1 to get the html.
Example websites:
- https://en.wikipedia.org/wiki/J._K._Rowling
- https://en.wikipedia.org/wiki/Richard_Feynman
- https://en.wikipedia.org/wiki/Hans_Rosling

### Task 5.4
In this task the function extract_events extracts date, venue and discipline from the given competitions. 
Then the function create_betting_slip saves a markdown format betting slip to the location './datetime_filter/< save_as >.md'. There save_as is the file name.
The extract_events function uses task 5.1 to get the html.

### Task 5.5.1
In this task the function extract_teams extracts the team names and urls from the NBA Playoff 'Bracket' section table.

### Task 5.5.2
And in this task the function extract_players extracts players that played for a specific team in the NBA playoffs.

## Usage


```
```


## Note from writer
> In taks 5.5 I experiensed some issues with the cells_text. It seems that the .get_text(strip=True) function does not work properly, and thus my cells_text has a lot of extra caracters. I have consolted the groop teacers and the course teachers but thay havent been able to figure out whats wrong. Due to this problem I've had to use regex to pars cells_text and get the wanted info, insted of just using indexing.

