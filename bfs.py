from collections import deque

class PersonNode(object):

	def __init__(self, data, friends=[]):
		
		self.data = data
		self.friends = set(friends)


	def __repr__(self):
		
		return "<PersonNode %s>" % self.data


class FriendGraph(object):

	def __init__(self):

		self.nodes = {}


	def add_person(self, name):
		"""Add a person to our graph.

        >>> f = FriendGraph()
        >>> f.nodes
        {}

        >>> f.add_person("Dumbledore")
        >>> f.nodes
        {'Dumbledore': <PersonNode Dumbledore>}
        """

		if name not in self.nodes:
			self.nodes[name] = PersonNode(name)


	def set_friends(self, name, friend_names):
		"""Set two people as friends.

        This is reciprocal: so if Romeo is friends with Juliet, she's
        friends with Romeo (our graph is "undirected").

        >>> f = FriendGraph()
        >>> f.add_person("Harry Potter")
        >>> f.add_person("Ron Weasley")
        >>> f.set_friends("Harry Potter", ["Ron Weasley"])

        >>> f.nodes["Harry Potter"].friends
        set([<PersonNode Ron Weasley>])

        >>> f.nodes["Ron Weasley"].friends
        set([<PersonNode Harry Potter>])
        """

		person_node = self.nodes[name]

		for friend in friend_names:
			friend_node = self.nodes[friend]
			person_node.friends.add(friend_node)
			friend_node.friends.add(person_node)


	def find_path(self, person1, person2):
		"""
		>>> f = FriendGraph()
		>>> f.add_person("Frodo")
		>>> f.add_person("Sam")
		>>> f.add_person("Gandalf")
		>>> f.add_person("Merry")
		>>> f.add_person("Pippin")
		>>> f.add_person("Treebeard")
		>>> f.add_person("Sauron")

		>>> f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
		>>> f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
		>>> f.set_friends("Merry", ["Pippin", "Treebeard"])
		>>> f.set_friends("Pippin", ["Treebeard"])

		>>> f.find_path("Frodo", "Gandalf")
		[<PersonNode Frodo>, <PersonNode Gandalf>]
		>>> f.find_path("Frodo", "Treebeard")
		[<PersonNode Frodo>, <PersonNode Pippin>, <PersonNode Treebeard>]
		>>> f.find_path("Treebeard", "Gandalf")
		[<PersonNode Treebeard>, <PersonNode Pippin>, <PersonNode Frodo>, <PersonNode Gandalf>]
		>>> f.find_path("Frodo", "Sauron")
		'No relationship'
		>>> f.find_path("Frodo", "Frodo")
		[<PersonNode Frodo>]
		>>> f.find_path("Frodo", "Harry Potter")
		'No relationship-- not in graph'
		"""

		person1_node = self.nodes.get(person1)
		person2_node = self.nodes.get(person2)

		if not person1_node or not person2_node:
			return "No relationship-- not in graph"

		#Initialize set for nodes that have been seen to avoid repeated 
		#visits to same node
		visited = set()
		#Initialize queue for nodes to visit with a tuple containting an
		#inital node plus its path, which currently is itself
		to_visit = deque([(person1_node, [person1_node])])

		#Start loop that continues until to_visit is empty, 
		#or all nodes have been visited
		while to_visit:
			#Unpack items that have been popped from front of queue; 
			#check if the node matches the 2nd actor
			current_node, path = to_visit.popleft()
			if person2_node == current_node:
				return path
			#If current node is not the node you want, add to visited set
			visited.add(current_node)
			#Iterate over current node's costars; if the costar isn't in 
			#visited set, add it to the to_visit queue. Create new path for
			#2nd item in tuple, using list concatanation so path for each 
			#costar is unique to them
			for friend in current_node.friends:
				if friend not in visited:
					to_visit.append((friend, path + [friend]))

		return "No relationship"


# f = FriendGraph()
# f.add_person("Frodo")
# f.add_person("Sam")
# f.add_person("Gandalf")
# f.add_person("Merry")
# f.add_person("Pippin")
# f.add_person("Treebeard")
# f.add_person("Sauron")

# f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
# f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
# f.set_friends("Merry", ["Pippin", "Treebeard"])
# f.set_friends("Pippin", ["Treebeard"])


if __name__ == '__main__':
	
	import doctest
	doctest.testmod()