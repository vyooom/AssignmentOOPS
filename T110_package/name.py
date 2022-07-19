class Name():
    def __init__(self, name):
        self.name = name
    def intro(self):
        try:
            if type(self.name) == str:
                a = self.name.title()
                return 'My name is %s.'%a
            else:
                raise ValueError
        except:
            return 'Please enter a valid string.'

