class RollNext:
    def __init__(self, roll):
        self.roll = roll
    def Roll(self):
        try:
            rollnext = self.roll + 1
            return 'The next roll number is %s'%rollnext
        except:
            return 'Please enter a valid integer as roll number.'
