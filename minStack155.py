class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, element):
        self.stack.append(element)
        if not self.minimum or element <= self.minimum[-1]:
            self.minimum.append(element)
        else:
            self.minimum.append(self.minimum[-1])
    
    def pop(self):
        last = self.stack[-1]
        self.stack = self.stack[:-1]
        self.minimum = self.minimum[:-1]
        return last
    
    def peek(self):
        return self.stack[-1]
    
    def minimum_value(self):
        return self.minimum[-1]