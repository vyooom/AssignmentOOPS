class courseIneuron():
    def __init__(self, counter = 0):
        self.counter = counter

    def updateCourse(self, count):
        '''Method to update the number of blogs.'''
        self.counter += count

    def showCourse(self):
        return self.counter
