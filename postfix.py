#!/usr/bin/python
import sys
a = input('Enter expression:').split()
if len(a) < 3:
    sys.exit('Incorrect Input')
else:
    def find(a):
        stack = []
        for b in a:
            if b.isdigit():
                stack.append(int(b))
                continue
            y = stack.pop()
            x = stack.pop()
            z = {
                '*': lambda x,y: x * y,
                '+': lambda x,y: x + y,
                '-': lambda x,y: x - y,
                }[b](x, y)
            stack.append(z)
        return stack.pop() 
    print 'Result: =', find(a)


