#!/usr/bin/env python3

import tokeniser
import parser

def render(fname, scope={}):
    with open(fname) as f:
        content = f.read()
    return _render(content, scope)

def _render(content, scope={}):
    return parser.Parser(tokeniser.tokenise(content)).parse().render(scope)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            string = f.read()
    else:
        string = "\n".join(iter(input, ""))

    print(_render(string, {"a": [1, 2, 3]}))

# Node Testing
    #import render
    #print(render.ForNode("a", "[1, 2, 3]", render.GroupNode([render.TextNode("hello, a:"), render.ExprNode("a"), render.TextNode("!\n")])).render({}))
    #print(render.IfNode("x > 10", render.TextNode("Statement is TRUE"), render.TextNode("Statement is FALSE")).render({'x':5}))
    #print(render.ForNode("a", "range(100)", render.GroupNode([render.IfNode("a % 3 == 0", render.TextNode("Fizz"), render.TextNode("Buzz"))])).render())
