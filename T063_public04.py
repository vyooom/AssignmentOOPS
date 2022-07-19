import logging
logging.basicConfig(filename='logTask_063_public04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Public :- Example - 04')

class Ineuron:
    '''Fourth example of public object.'''

    def __init__(self, rollnumber):
        try:
            if type(rollnumber) == int:
                self.roll = rollnumber
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')


    def showRoll(self):
        logging.info('The rollnumber is %s' % self.roll)
        return self.roll

    def changeRoll(self):
        self.roll = self.roll * 10
        logging.info('The updated rollnumber is %s' % self.roll)
        return self.roll

abhi = Ineuron(894)
logging.info(abhi.roll)
abhi.showRoll()
abhi.changeRoll()
abhi.showRoll()
abhi.roll = abhi.roll * 100
abhi.showRoll()

'''Change in public data permanently from the terminal.'''