class Solution:
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:

            if t == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif t == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))   # truncate toward 0

            else:
                stack.append(int(t))

        return stack[0]