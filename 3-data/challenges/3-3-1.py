'''## Challenge 3-3-1

#### Classic use case for concatenation.

[https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json]("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")

Observe the output from the three cells below. The issue with the JSON data is that there are employees under keys by department `"accounting", "sales", "marketing"`

This is the classic use-case for `pd.concat()` as there is no practical way to use `pd.json_normalize()` to get all the employees under each department.

    for each department:
        create a dataframe for that department (e.g. from the json under the department)
        add lineage to the dataframe (e.g. add the department name)
        add the dataframe to a list of departments
    concat the list of departments together one dataframe
    print dataframe

expected output:

    firstName lastName  age        dept
    0      John      Doe   23  accounting
    1      Mary    Smith   32  accounting
    2     Sally    Green   27       sales
    3       Jim   Galley   41       sales
    4       Tom    Brown   28   marketing
'''

