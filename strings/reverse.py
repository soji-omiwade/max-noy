class Reverse:
    """reverse a sequence using only the yield
    
        not using a counter, that is!
    """
    def __init__(self, s):
        self.s = s
        self.gen = self.yielder()
    def yielder(self):
        for i in range(len(self.s)):
            yield self.s[len(s) - (i+1)]
    def __iter__(self):
        self.gen = self.yielder()
        return self
    def __next__(self):
        return next(self.gen)

s = 'helo man'  
reverse_generator_object = Reverse(s)
l = []
for x in reverse_generator_object:
    l.append(x)
print(', '.join(l))