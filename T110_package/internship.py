class Internship:
    def __init__(self, n):
        self.n = n
    def intern(self):
        try:
            if type(self.n) == int:
                return 'My internship count is:  %s.'%self.n
            else:
                raise ValueError
        except:
            return 'Please enter a valid integer.'

