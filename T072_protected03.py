import logging
logging.basicConfig(filename='logTask_072_protected03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Protected :- Example - 03')

class Ineuron:
    '''Third example of protected object.'''

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
logging.info('The change in public data from terminal updated roll: %s'%(abhi._roll+1))
abhi.showRoll()
