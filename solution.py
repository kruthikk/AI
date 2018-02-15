assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
	"""
	Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    
	"""
	for unit in unitlist:
		twinboxes = [box for box in unit if len(values[box])==2]
		if len(twinboxes) == 1:
			continue
		twinboxvalues = {}
		for twin in twinboxes:
			twinboxvalues[twin] = values[twin]
		
		#get count of twin values
		count={}
		lst =list(twinboxvalues.values())
		for item in lst:
			count[item] = lst.count(item)
		#get naked twin values
		
		nakedtwinitems = {k:v for (k,v) in count.items() if v == 2}
		for item in nakedtwinitems:
			#iterate through unit values and replace item in value with ''
			for box in unit:
				if (values[box] != item and len(values[box])>1 ):
					if(item[0] in values[box]):
						assign_value(values, box, values[box].replace(item[0],''))
					if(item[1] in values[box]):
						assign_value(values, box, values[box].replace(item[1],''))
	
	return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    candidatevalues=[]
    defval = '123456789'
    for c in grid:
        if c == '.':
            candidatevalues.append(defval)
        elif c in defval:
            candidatevalues.append(c)
    assert len(candidatevalues) == 81
    
    return dict(zip(boxes,candidatevalues))

def display(values):
	"""
	Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
	"""
	    
	width = 1+max(len(values[s]) for s in boxes)
	line = '+'.join(['-'*(width*3)]*3)
	for r in rows:
		print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
						for c in cols))
		if r in 'CF': print(line)
	return

def eliminate(values):
	"""
	Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
	"""
	
	# Get all singleval squares     
	singlevalsqrkey = [sq for sq in values.keys() if len(values[sq]) == 1]
	
	#foreach singleval sq, get peers and remove from peer sq val the sq val 
	for sqkey in singlevalsqrkey:
		sqkeypeers = peers[sqkey]
		for peer in sqkeypeers:
			assign_value(values, peer, values[peer].replace(values[sqkey],''))
	return values
    

def only_choice(values):
	"""
	Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
	"""
	
	for unit in unitlist:
		for digit in '123456789':
			dplaces = [box for box in unit if digit in values[box]]
			if len(dplaces) == 1:
				assign_value(values, dplaces[0], digit)
	return values

def reduce_puzzle(values):
	stalled = False
	while not stalled:
		# Check how many boxes have a determined value
		solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
		# Your code here: Use the Eliminate Strategy
		stg1 = eliminate(values)
		# Your code here: Use the Only Choice Strategy
		stg2 = only_choice(stg1)
		values=stg2
		# naked twin strategy
		values = naked_twins(values)
		# Check how many boxes have a determined value, to compare
		solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
		# If no new values were added, stop the loop.
		stalled = solved_values_before == solved_values_after
		# Sanity check, return False if there is a box with zero available values:
		if len([box for box in values.keys() if len(values[box]) == 0]):
			return False
	return values
    

def search(values):
	"""
	Using depth-first search and propagation, create a search tree and solve the sudoku.
	"""
	
	# First, reduce the puzzle using the previous function
	values=reduce_puzzle(values)
	if values == False:
		return False
	if(all(len(values[s])==1 for s in boxes)):
		return values
    # Choose one of the unfilled squares with the fewest possibilities
	min_boxes = min((len(values[box]), box) for box in boxes if len(values[box])> 1)
	for i in values[min_boxes[1]]:
		can = values.copy()
		can[min_boxes[1]] = i
		# Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
		attempt = search(can)
		if(attempt):
			return attempt

def solve(grid):
	"""
	Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
	"""
	values=grid_values(grid)
	values = search(values)
	return values

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diag_units =[]
diag_units.append([m+n for m,n in zip(rows,cols)])
diag_units.append([m+n for m,n in zip(rows,list(reversed(cols)))])

unitlist = row_units + column_units + square_units + diag_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

	
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
