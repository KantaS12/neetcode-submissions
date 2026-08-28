class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []

        # if temperatures length == 1 return array with 0
        if len(temperatures) == 1:
            return [0]

        for i in range(0, len(temperatures)):

            # While the stack (temperature is bigger than whatever is in stack)
            while (stack and temperatures[i] > temperatures[stack[-1]]):
                index = stack.pop()
                result[index] = i - index

            # count up
            stack.append(i)

        return result


