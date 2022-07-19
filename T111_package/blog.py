class blogIneuron():
    def __init__(self, counter = 0):
        self.counter = counter

    def updateBlog(self, count):
        '''Method to update the number of blogs.'''
        self.counter += count

    def showBlog(self):
        return self.counter
