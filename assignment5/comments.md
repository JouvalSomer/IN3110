# Peer Review Assignment 5

## Taks 5.1 Sending HTTP requests

**Files**
* requesting urls.py
* requesting_urls

### **Changes:**
1. The first thing I did was that I added the url link to the first line of the .txt files, so that one could access them later. <br/> For example in order to get the corresponding base url.
1. The second thing was an assert that checks if the request was successful. If it wasn't it sends out a message to the user.
1. The third thing I did was to clean up the script calls, and changes the params for the last link.

## Taks 5.2 Regex for filtering URLs

**Files**
* filter_urls.py
* filter_urls

### **Changes:**

1. I have added a loop that makes sure there aren't any duplicate links.
1. I've also implemented the base url functionality, so that one doesn't need to find it manually. 

## Taks 5.3 Regular Expressions for finding Dates
**Files**
* collect_dates.py
* collect_dates regex

### **Changes:**

In this task I basically changed the whle script. Otherwise it would be very tedious to find all the bugs. <br/> There were mainly three bugs that I fould. 
* The first one had to do with how you found the months. <br/> By just using the pattern \w{3,9} you misstaikingly collected some words that werent months. <br/> For example the words "and" and "time".

<img src="https://raw.github.uio.no/jmsomer/IN3110-klaudiap/master/assignment5/Example_of_mistake.png?token=AAABND2CANX2YY3BF5GYFDTBTYWHK" alt="drawing" width="400"/>

* The second one was the fact that the months in words were not converted to numbers.<br/> (I'm not sure if we had to do this but it makes fixing bug 3 a lot easyer).

* The third one was the apperence of dobble dates, meaning some dates appeared more than once.

## Taks 5.4 Making your Life easier with Soup for finding dates
**Files**
* time_planner.py
* datetime filter/betting slip empty.md

### **Changes:**

I had nothing to add in this task, and learned some new things:) 

## Taks 5.5 NBA Player Statistics Season 2020/2021 

**Not implemented**