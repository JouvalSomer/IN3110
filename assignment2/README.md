
# README.md Assignment2 

## Task 2.1

### Prerequisites

For the program to run one needs to have Git bash installed, in addition to the file, move.sh, containing the code. 
Downloade link for Git Bash: https://git-scm.com/downloads

### Functionality

The function move in the script move.sh 
1) Checks that there are at least two commandline arguments passed and return an error message to the user if the number is less than two.
2) Checks that the src (source) directory exists and return an error message to the user if the src directory does not exist.
3) Checks that the dst (destination) directory exists and return an error message to the user if the dst directory does not exist
4) If all three statments pass the files are moved from the given src directory to the given dst directory using the command mv. 

### Missing Functionality

The script does not check if its given more than two commandline arguments.

### Usage

To move files from one directory to an other run the program, move.sh, followed by to commandline arguments. The first of wich sould be the source directory, i.e. the path to the folder who's content you want to move, and the second should be the destination directory, i.e. the path to the folder you want to move the contetnt to.

An example:

```bash
./move.sh source_directory destination_directory 
```

## Task 2.2
.
.
.