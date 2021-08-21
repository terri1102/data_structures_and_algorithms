employees table

|columns	|types|
|----|----|
|id	|int|
|first_name|	varchar|
|last_name|	varchar|
|salary|	int|
|department_id|	int|
 

departments table

|columns|	types|
|---|---|
|id|	int|
|name|	varchar|
 

Given the tables above, select the top 3 departments with at least ten employees and rank them according to the percentage of their employees making over 100K in salary.

Example output:

|percentage_over_100K|	department name|	number of employees |
|---|---|---|
|.9	|engineering|	25|
|.5|	marketing|	50|
|.12|	sales|	12|
