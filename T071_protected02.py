import logging
logging.basicConfig(filename='logTask_071_protected02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Protected :- Example - 02')

class Ineuron:
    '''Second example of protected object.'''

    def __init__(self, rollnumber):
        try:
            if type(rollnumber) == int:
                self._roll = rollnumber
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')

    def showRoll(self):
        logging.info('The rollnumber is %s'%self._roll)
        return self._roll

    def newRoll(self):
        r = self._roll + 1
        logging.info('The rollnumber of next entrant is %s.'%r)
        return r


abhi = Ineuron(894)
logging.info(abhi._roll)
abhi.showRoll()
abhi.newRoll()
logging.info(abhi._roll+1)
