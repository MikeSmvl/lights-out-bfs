import sys
import json

def getNodeVal(node) -> int:
	"""Function that converts a node to an integer.
	Ex: [[0,0,0],[1,0,1],[0,1,0]] -> 1*0 + 2*0 + 4*0 + 8*1 + 16*0 + 32*1 + 64*0 + 128*1 + 256*0 -> 168

	Args:
			node: The node to be converted to a value.

	Returns:
			The return value. Integer representation of node.
	"""
	val = 0
	base = 1
	for row in range(len(node)):
		for col in range(len(node[0])):
			val += base * node[row][col]
			base = base * 2
	return val


def toggle_bit(bit) -> int:
	"""Function that inverts bits.

	Args:
			bit: The bit to be inverted.

	Returns:
			The return value. 0 if bit was 1 and 1 if bit was 0.
	"""
	return 1 if bit == 0 else 0


def toggle(node, row, col) -> "child":
	"""Function that toggles a node at a certain row and col and returns child.

	Args:
			node: The node to be toggled.
			row, col:	The row and col pair to toggle.

	Returns:
			The child of the node.
	"""
	new_node = []
	for r in node:
		new_node.append([c for c in r])

	new_node[row][col] = toggle_bit(new_node[row][col])
	if row+1 < len(node):
		new_node[row+1][col] = toggle_bit(new_node[row+1][col])
	if row-1 >= 0:
		new_node[row-1][col] = toggle_bit(new_node[row-1][col])
	if col+1 < len(node[0]):
		new_node[row][col+1] = toggle_bit(new_node[row][col+1])
	if col-1 >= 0:
		new_node[row][col-1] = toggle_bit(new_node[row][col-1])

	return new_node


def bfs(start_node, goal_node, max_depth) -> "solution path":
	"""Breadth-first search (BFS) function.

	Args:
			start_node: The beginning node.
			goal_node: The node to try and reach.

	Returns:
			The path (list) taken to reach the node if any.
	"""
	queue = [start_node,[]]
	explored = {}
	level = 0

	# Return empty path if start is equal to goal
	if start_node == goal_node:
		return []

	# Keep exploring while the queue has nodes
	while len(queue) > 0:
		path = queue.pop(0)

		if level == 0:
			node = path
		else:
			# To keep track of levels an empty node gets popped between levels which will cause an exception
			try:
				node = path[-1]
			except Exception:
				node = []
				pass

		if len(node) == 0:
			level += 1
			# Return empty list if max depth was reached
			if max_depth == level:
				return []
			queue.append(node)

		else:
			val = getNodeVal(node)
			if val not in explored:

				# Mark node as explored
				explored[val] = True

				for row in range(len(node)):
					for col in range(len(node)):
						child = toggle(node, row, col)
						new_path = list(path)
						if level == 0:
							new_path = [new_path]
						new_path.append(child)
						queue.append(new_path)
						if child == goal_node:
							level+=1
							return new_path
	# No solution found
	return []

def print_solution(solution_list) -> 'Human Readable Solution':
	"""Function that converts a list in to a readable format

	Args:
			solution_list: The list that the BFS function returned.

	Returns:
			The return value. String readable representation of solution.
	"""
	size = len(solution_list[0][0])
	try:
		print('Starting Node'.center(20, ' '))
		print(''.center(20, '-'))
		for node in solution_list:
				for i in range(size):
					print(str(node[i]).center(20, ' '))
				print(''.center(20, '-'))
		print('Goal Node'.center(20, ' '))
	except Exception as error_msg:
		print("No solution found!")

# Main
def main():
	try:
		max_depth = int(sys.argv[1])
		start_node = json.loads(sys.argv[2])
		goal_node = json.loads(sys.argv[3])
		solution_list = bfs(start_node, goal_node, max_depth)
		if solution_list == []:
			print("No solution found!")
		else:
			print_solution(solution_list)
	except Exception as error_msg:
		print(error_msg)

if __name__== "__main__":
  main()