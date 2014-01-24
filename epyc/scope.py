# Scope Class
# Used to allow for global and local variable separation.
class Scope(dict):
	'''
	A dict-like scoping object, resolving global and local variables.
	It chiefly allows for global and local scope separation.
	'''
	def __init__(self, items=None, parent=None):
		self.items = items or {}
		self.parent = parent

	def __repr__(self):
		return "Scope(items={!r}, parent={!r})".format(self.items, self.parent)

	def __str__(self):
		return "Scope(items={!r}, parent={!r})".format(self.items, self.parent)

	def __getitem__(self, key):
		if key in self.items:
			return self.items[key]

		if self.parent:
			return self.parent[key]

		raise KeyError("no such variable in current scope")

	def __setitem__(self, key, value):
		if self.parent and key in self.parent:
			self.parent[key] = value
		else:
			self.items[key] = value

	def __contains__(self, key):
		if key in self.items:
			return True

		if self.parent:
			return key in self.parent

		return False

	def __len__(self):
		size = len(self.items)

		if self.parent:
			size += len(self.parent)

		return size

	def __bool__(self):
		return True
