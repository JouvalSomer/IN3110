#! /bin/bash

# Creates the timer_logfile
[ ! -d $HOME/.local ] && mkdir $HOME/.local{
[ ! -d $HOME/.local/share ] && mkdir $HOME/.local/share/
[ ! -f $HOME/.local/share/.timer_logfile ] && touch $HOME/.local/share/.timer_logfile} 

# Creats a variable LOGFILE with the path to timer_logfile
LOGFILE=$HOME/.local/share/.timer_logfile 

# Variable 'now' stores the current date and time
now=`date`

# Stores the name of the task
label_name=${@:2}

# Stores the first word in the last line as a variable 
first_word_last_line=$(tail -n1 $LOGFILE | cut -d' ' -f1)

# Tests and starts tracking if a new task can be track, and sends out an error message if not
if [ "$first_word_last_line" == "END" ] || [ "$first_word_last_line" == "" ]; then
    [ "$1" == "start" ] && echo -e "START $now\nLABEL $label_name" >> $LOGFILE && "$label_name is now being \ tracked."
    [ "$1" == "status" ] && echo "You are not tracking a task."
    [ "$1" == "stop" ] && echo "No task is tracked and thus cant me stoped."
fi
# Tests and ends a task if it's being tracked, and sends out an error message if not
if [ "$first_word_last_line" == "LABEL" ]; then
    label_name=$(tail -n1 $LOGFILE | cut -d' ' -f2-20)
    [ "$1" == "start" ] && echo "$label_name is currently being tracked."
    [ "$1" == "status" ] && echo "The tracked tast is "$label_name"."
    [ "$1" == "stop" ] && echo -e "END $now\n" >> $LOGFILE && echo "$label_name is lo longer tracked."
fi

# Instructions to the user if they don't provide one of the three commandline arguments, start, stop or status
[ "$1" != "start" ] && [ "$1" != "status" ] && [ "$1" != "stop" ] && echo "Pleace enter one of the three commandline arguments, start, stop or status. See the README file for more info. "

