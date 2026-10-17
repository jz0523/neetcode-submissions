class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            pos = position[i]
            s = speed[i]
            car = (pos, s)
            cars.append(car)
        
        cars.sort(reverse=True)

        for i in range(len(cars)):
            car = cars[i]
            if stack and ((target - car[0]) / car[1]) <= ((target - stack[-1][0]) / stack[-1][1]):
                continue
            else:
                stack.append(car)
            
        return len(stack)

