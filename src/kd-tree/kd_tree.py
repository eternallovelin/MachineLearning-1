import numpy as np

class Node:
	def __init__(self):
		self.location
		self.left
		self.right
class KDTree:
	def __init__(self, node_list, depth):
		self.root_node = []
		self.depth = depth
		self.node_num = len(node_list)
		for i in range(self.node_num):
			self.
		# sort the list
		node_list.sort()
		print(node_list)
		'''
		while True:
			axis = depth % self.node_num
			# caculate the
		'''


if __name__ == '__main__':
	node_list = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
	kd_tree = KDTree(node_list, 2)