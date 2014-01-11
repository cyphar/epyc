#!/usr/bin/env python3

import sys
import epyc

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(epyc.render(sys.argv[1]))
    else:
        string = "\n".join(iter(input, ""))
        print(epyc._render(string, {"a": [1, 2, 3]}))

# Node Testing
    #import render
    #print(render.ForNode("a", "[1, 2, 3]", render.GroupNode([render.TextNode("hello, a:"), render.ExprNode("a"), render.TextNode("!\n")])).render({}))
    #print(render.IfNode("x > 10", render.TextNode("Statement is TRUE"), render.TextNode("Statement is FALSE")).render({'x':5}))
    #print(render.ForNode("a", "range(100)", render.GroupNode([render.IfNode("a % 3 == 0", render.TextNode("Fizz"), render.TextNode("Buzz"))])).render())
