# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *In a unit, if there are only two boxes with the same two possible values, then these two possible values can only belong to either of these two boxes and they cannot be in possible values of other boxes in the unit.
 So we eliminate these values from other boxes. This is a constraint which updates the peers in the unit. These updates can cause further updates to peers of the updated boxes.
 This constraint is applied to all units which helps in determining the best value for a box.
 With this additional constraint applied, the complete board can be solved faster.  *

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *In a diagonal sudoku problem, there are two additional units along the diagonal. These units have same constraint as units in normal sudoku.
	The same below constraints are applied repeatedly to get the complete board with valid values.
		If a square has only one possible value, then eliminate that value from the box's peers - Elimiate strategy
		If a unit has only one possible place for a value, then put the value there - Only choice strategy
		In a unit, if there are only two boxes with the same two possible values, then eliminate these values from other boxes of the unit - naked twin.
		*

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

