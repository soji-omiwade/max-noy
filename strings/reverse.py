class reverse_iterator:
    def __init__(self, s):
        self.s = s
        self.index = len(s)
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.s[self.index]
    # for i in range(len(self.s)-1, -1, -1):
            # yield self.s[i]
            
class Reverse: 
    def __init__(self, s):
        self.s = s
    def __iter__(self):
        return reverse_iterator(self.s)
# s = 'helo man'    
# t = Reverse(s)
# for x in t:
    # print(x, end='')