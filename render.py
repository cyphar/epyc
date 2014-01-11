#!/usr/bin/env python3

import html
from epyc import epyc

def sanitise(string):
	return html.escape(string)

class ParseError(Exception):
	pass

# Node Classes
# Used in the parsing and evaluation to define the syntax tree.
class Node:
	"Node meta-class."
	def __init__(self, children, content):
		self.children = children
		self.content = content

	def render(self):
		raise NotImplementedError("node meta-class cannot be evaluated")


class GroupNode(Node):
	def __init__(self, children):
		super().__init__(children, None)

	def render(self, scope={}):
		"Render all children in group."
		ret = ""

		for child in self.children:
			render = child.render(scope)
			if render is None:
				render = ""
			ret += str(render)
		return ret


class TextNode(Node):
	def __init__(self, content):
		super().__init__([], content)

	def render(self, scope={}):
		"Render sanitised content"
		return self.content


class IncludeNode(Node):
	def __init__(self, path):
		self.path = path

	def render(self, scope={}):
		"Return rendered content from file at path"
		with open(self.path) as f:
			content = f.read()
			content = epyc(content, scope)
		return content

class ForNode(Node):
	def __init__(self, identifier, expression, block):
		self.identifier = identifier
		self.expression = expression
		self.block = block

	def render(self, scope={}):
		ret = ''

		for item in eval(self.expression, {}, scope):
			scope[self.identifier] = item
			ret += self.block.render(scope) or ''
		return ret


class ExprNode(Node):
	def __init__(self, content):
		super().__init__([], content)

	def render(self, scope={}):
		"Return evaluated content or None"
		try:
			return eval(self.content, {}, scope)
		except:
			return None


class IfNode(Node):
	def __init__(self, condition, ifnode, elsenode = None):
		self.ifnode = ifnode
		self.elsenode = elsenode
		self.condition = condition

	def render(self, scope={}):
		if eval(self.condition, {}, scope):
			return self.ifnode.render()
		elif self.elsenode:
			return self.elsenode.render()
