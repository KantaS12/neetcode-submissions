class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        # Basically let's just add the numbers into the stack and we do a if statement. If it's +, -, *, or / then we do the operation on them by removing the numbers out of the stack and then adding it back and we do it till tokens is ran through.

        # initalize a stack
        stack = []

        for token in tokens:

            # So we need to add the tokens into the stack. However, we want to check if it's a num or the arithmetic operation.

            if token in ("+", "*", "-", "/"):

                second = stack.pop()
                first = stack.pop()

                if token == "*":
                    result = first * second

                elif token == "+":
                    result = first + second

                elif token == "-":
                    result = first - second

                elif token == "/":
                    result = int(first / second)

                else:
                    result = 0

                stack.append(result) # Put back into stack for other calculations

            else:
                stack.append(int(token))

        return stack.pop()