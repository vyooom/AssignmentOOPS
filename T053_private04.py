import logging
logging.basicConfig(filename='logTask_053_private04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Private :- Example - 04')

class Ineuron:
    '''Fourth example of private object.'''

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

    def changeRoll(self):
        self.__roll = self.__roll * 10
        logging.info('The updated rollnumber is %s'%self.__roll)
        return self.__roll

abhi = Ineuron(894)
logging.info(abhi._Ineuron__roll)
abhi.showRoll()
abhi.changeRoll()
abhi.showRoll()
abhi._Ineuron__roll = abhi._Ineuron__roll * 100
abhi.showRoll()

'''Change in private data permanently from the terminal.'''