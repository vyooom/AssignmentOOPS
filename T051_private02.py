import logging
logging.basicConfig(filename='logTask_051_private02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Private :- Example - 02')

class Ineuron:
    '''Second example of public object.'''

    def __init__(self, rollnumber):
        try:
            if type(rollnumber) == int:
                self.__roll = rollnumber
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')

    def showRoll(self):
        logging.info('The rollnumber is %s'%self.__roll)
        return self.__roll

    def newRoll(self):
        r = self.__roll + 1
        logging.info('The rollnumber of next entrant is %s.'%r)
        return r


abhi = Ineuron(894)
logging.info(abhi._Ineuron__roll)
abhi.showRoll()
abhi.newRoll()
logging.info(abhi._Ineuron__roll+1)

