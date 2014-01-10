#!/usr/bin/env python3

from tokeniser import tokenise
from parser import Parser

if __name__ == "__main__":
	string = "\n".join(iter(input, ""))
	print(Parser(tokenise(string)).parse().render())

# Node Testing
# print(ForNode("a", "[1, 2, 3]", GroupNode([TextNode("hello, a:"), ExprNode("a"), TextNode("!\n")])).render({}))
# print(IfNode("x > 10", TextNode("Statement is TRUE"), TextNode("Statement is FALSE")).render({'x':5}))
