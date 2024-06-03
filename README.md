# dashdevs-task-solution


### Task:
Purpose of the technical specification: Implement an algorithm for searching for an equilibrium index in an array of integers. Description. The equilibrium index in an array is defined as the index at which the sum of the elements on the left is equal to the sum of the elements on the right. In other words, it is an index at which the sum of the array elements before that index is equal to the sum of the elements after it. For example, in the array 1, 7, 3, 6, 5, 6, the equilibrium index is 3 because the sum of the elements to the left of index 3 (1 + 7 + 3 is 11) is equal to the sum of the elements to the right of index 3 (5 + 6 is 11) . If the equilibrium index is not found, the function should return -1.

### Solution

The task was solved using the cli interface and containerized in docker. The task was divided into logical modules in which logic, validation, processing, testing and interface are atomically performed.
The input list was also validated and tests were written in the test.


##### How to install 
Copy solution from github repo:
```bash
git clone git@github.com:yevhenii-nevmyvako/dashdevs-task-solution.git
```

Install requirements & setup the project:
```bash
pip install -e .
```

If you wont install in docker:
go to your project folder and run command:
```bash
docker build -t <name:tag> . 
```

##### How to run without docker
list create from string with integer values.
```bash
find_index '5,6,5'
```
Save result to json file with optional flag -f
```bash
find_index '5,6,5' -f path/to/save_result.json
```

##### How to run with docker
list create from string with integer values.
```bash
docker run <name:tag> find_index '5,6,5'
```

Save result to json file with optional flag -f
```bash
docker run find_index '5,6,5' -f path/to/save_result.json
```


