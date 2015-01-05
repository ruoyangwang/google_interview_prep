class binarytree(object):
	def __init__(self,key,value):
		self.root = treeNode(key,value)
	
	def insert(self, key, value):
		return self.root.insert(key,value)	#return boolean true or false

	
	def get(self, key):
		return self.root.get(key)			#return the value of the key, return -1 if cannot find

	def delete(self,key):
		return self.root.delete(key)			#return boolean true or false
	
	def update(self, key, value):
		return self.root.update(key,value)	#return boolean true or false

	def printTree(self):
			


class treeNode(object):
	def __init__(self,key,value):
		self.key=key
		self.value=value
		self.left=None
		self.right=None
		self.parent=None

	def insert(self, key, value):
		if self.key>key:			#this node should go to left
			if self.left:
				self.left.insert(key,value)
			else:
				self.left=treeNode(key,value)
		else:
			if self.right:
				self.right.insert(key,value)
			else:
				self.right=treeNode(key,value)
		return 
		
		
	def get(self,key):
		if self.key==key:
			return self.value
		
		elif self.key>key:			#should go to left
			if	self.left:
				self.left.get(key)
			else: return -1
		
		else:
			if self.right:
				self.left.get(key)
			else: return -1
		
	def delete(self,key):
		if self.key==key:
			
		if self.key>key:
			self.left.delete(key)
			self.left.lsearch(self.left)
		elif self.right.key==key:
			self.right.rsearch(self.right)
		else:
			self.left.delete(key)
			self.right
		
	def update(self, key, value):
		if self.key==key: self.value=value
		elif self.key>key:
			if self.left: self.left.update(key,value)
			else:
				return False
		else:
			if self.right: self.right.update(key,value)
			else:
				return False

		return True
	
	def lsearch(self, deleteNode):
		if 





			
