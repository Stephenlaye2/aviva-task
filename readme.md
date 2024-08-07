## Task 
1. Python is used to transform the input data into the desired outputs. 
2. Unit testing implemented

## How to Run the Code
* clone the code to your system
* Make sure Python is installed. Python ```version 3.9.0``` is recommended, but any Python3 version should be fine.
* If pandas module is not found, use pip to install pandas
* open gitbash; cd into the ***avivaProject*** directory and run the code with python. For example  ```python c:/Users/steph/project/aviva-tasks/avivaProject/src/main/transformation.py```
* To run the test, you need to do same thing. For example ``` python c:/Users/steph/project/aviva-tasks/avivaProject/tests/main/test_transformation.py```
* The input is being read from ```src/resources/input/input_data.json```
* The output is available in ```src/resources/output/petitions_output.csv```

**Run Image**
![alt text](avivaProject/src/resources/img/aviva-task-gitbash-run.png "output")

## Input Data 
The input data is a JSON file containing a set of government petitions. For each petition, we have the label (the title of the petition), the abstract (the main text of the petition), and the number of signatures. 

## Output
The output (you can find it in ***src/resources/output*** folder)is of csv format, containing the following 21 columns: 
1. petition_id: a unique identifier for each petition (this is not present in the input 
data and needs to be created) 
2. One column for each of the 20 most common words across all petitions, only 
counting words of 5 or more letters, storing the count of each word for each 
petition. 
For example, if “should” is one of the 20 most common (5+ letter) words, one column 
should be titled should. If the first petition includes the word “should” three 
times, and the second petition does not mention “should”, then the should
column should read 3 for the first petition and 0 for the second petition.
