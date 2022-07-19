import logging
logging.basicConfig(filename='logTask_073_protected04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Protected :- Example - 04')

class Ineuron:
    '''Fourth example of protected object.'''

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

    def changeRoll(self):
        self._roll = self._roll * 10
        logging.info('The updated rollnumber is %s'%self._roll)
        return self._roll

abhi = Ineuron(894)
logging.info(abhi._roll)
abhi.showRoll()
abhi.changeRoll()
abhi.showRoll()
abhi._roll = abhi._roll * 100
abhi.showRoll()

'''Change in protected data permanently from the terminal.'''