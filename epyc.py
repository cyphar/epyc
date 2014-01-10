#!/usr/bin/env python3

import tokeniser
import parser
#import render

def epyc(content, scope={}):
  return parser.Parser(tokeniser.tokenise(content)).parse().render(scope)

if __name__ == "__main__":
  import render
  string = "\n".join(iter(input, ""))
  print(epyc(string, {}))

# Node Testing
# print(ForNode("a", "[1, 2, 3]", GroupNode([TextNode("hello, a:"), ExprNode("a"), TextNode("!\n")])).render({}))
# print(IfNode("x > 10", TextNode("Statement is TRUE"), TextNode("Statement is FALSE")).render({'x':5}))
# print(render.IncludeNode("test.py").render({}))
