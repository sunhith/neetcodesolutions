class Solution:
    def opp(self, val1, val2, operation):
        match operation:
            case "+": return val1 + val2
            case "-": return val1 - val2
            case "*": return val1 * val2
            case "/": return int(val1 / val2)
    
    def is_int(self, s):
        try:
            int(s)
            return True
        except Exception as error:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if self.is_int(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(self.opp(val1, val2, tokens[i]))
        return stack[0]

        