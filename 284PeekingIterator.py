# 不懂~
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = []
        while iterator.hasNext():
            self.iterator.append(iterator.next())
        

    def peek(self):
        return self.iterator[0]
        

    def next(self):
        return self.iterator.pop(0)
        

    def hasNext(self):
        return len(self.iterator) != 0