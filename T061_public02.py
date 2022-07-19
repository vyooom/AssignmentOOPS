import logging
logging.basicConfig(filename='logTask_061_public02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Public :- Example - 02')

class Ineuron:
    '''Second example of public object.'''

    def __init__(self, rollnumber):
        try:
            if type(rollnumber) == int:
                self.roll = rollnumber
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')

    def showRoll(self):
        logging.info('The rollnumber is %s'%self.roll)
        return self.roll

    def newRoll(self):
        r = self.roll + 1
        logging.info('The rollnumber of next entrant is %s.'%r)
        return r


abhi = Ineuron(894)
logging.info(abhi.roll)
abhi.showRoll()
abhi.newRoll()
logging.info(abhi.roll+1)
