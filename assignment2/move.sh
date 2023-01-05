#! /bin/bash

function move {
    src_=$1
    dst_=$2
    
    #Checking if there are enough commandline arguments (at least two arguments).
    [ $# -lt 2 ] && echo """You don't have enough commandline arguments. There has to be at least two arguments.
    Plece enter the source directory followed by the destination directory."""
    
    #Checking if the directories exist.
    [ ! -d $src_ ] && echo "The source directory does not exists."

    [ ! -d $dst_ ] && echo "The destination directory does not exists."

    #Moving the files from the source directory to the destination directory.
    mv $src_/* $dst_
}

move $@


