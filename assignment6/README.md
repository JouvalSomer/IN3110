# README.md for Assignment 6
### Web Programming and Data Analysis 

## Prerequisites
Install all prerequisites using the requirements.txt file.
Put the requirements.txt file in the wanted directory (where the command will be executed). If you want it in another directory, specify its path like path/to/requirements.txt.
Example:
```
pip install -r requirements.txt
```

## Functionality

### Task 6.1
In this task the script webvisualization_plots.py is run. The script contains three functions get_data_from_csv, plot_reported_cases_per_million and main.

- The get_data_from_csv function creates a pandas dataframe from the .csv file with the chosen (optional) countries.
- The function plot_reported_cases_per_million plots the data of reported covid-19 cases per million using altair.
- The function main is called when the file is run as a script and creates a chart and displays it on a web server.

Example run:
```
python webvisualization_plots.py
```

### Task 6.2
In this task a FastAPI app is made which uses the script webvisualization plots.py from task
6.1 to generate a plot of ”Daily new confirmed COVID-19 cases per million people” by date and display it on the web page.

Example run:
```
python webvisualization.py
```


