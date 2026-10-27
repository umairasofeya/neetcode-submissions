class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # using stack, one stack is to add numbers,
        # when u find an operand, u pop the 2 most recent number
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == "+":
                    result = a + b
                elif tokens[i] == "-":
                    result = a - b
                elif tokens[i] == "*":
                    result = a * b
                elif tokens[i] == "/":
                    result = int(a / b)

                stack.append(result)
        return(stack[0])




            
