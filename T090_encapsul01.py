import logging
logging.basicConfig(filename='logTask_090_encapsul01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Encapsulation :- Example - 01')

'''Encapsulation was dealt in public private & protected.
We will use these modules only.'''


class Ineuron:
    '''Fifth example public object.'''

    def __init__(self, id):
        try:
            if type(id) == int:
                self.id = id
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')


    def showId(self):
        logging.info('The current id is %s'%self.id)
        return self.id

    def updateId(self):
        self.id = self.id + 10
        logging.info('The current id is %s'%self.id)
        return self.id



abhi = Ineuron(5)
abhi.showId()
abhi.updateId()
abhi.id = abhi.id -7
abhi.showId()
abhi.updateId()

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

class Ineuron:
    '''Third example of public object.'''

    def __init__(self, rollnumber):
        try:
            if type(rollnumber) == int:
                self.__roll = rollnumber
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')


    def showRoll(self):
        logging.info('The rollnumber is %s' % self.__roll)
        return self.__roll

    def changeRoll(self):
        self.__roll = self.__roll * 10
        logging.info('The updated rollnumber is %s' % self.__roll)
        return self.__roll

abhi = Ineuron(894)
logging.info(abhi._Ineuron__roll)
abhi.showRoll()
abhi.changeRoll()
abhi.showRoll()
logging.info('The change in public data from terminal updated roll: %s'%(abhi._Ineuron__roll+1))
abhi.showRoll()

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


class Ineuron:
    '''Fifth example public object.'''

    def __init__(self, id):
        try:
            if type(id) == int:
                self.__id = id
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')


    def showId(self):
        logging.info('The current id is %s'%self.__id)
        return self.__id

    def updateId(self):
        self.__id = self.__id + 10
        logging.info('The current id is %s'%self.__id)
        return self.__id



abhi = Ineuron(5)
abhi.showId()
abhi.updateId()
abhi._Ineuron__id = abhi._Ineuron__id -7
abhi.showId()
abhi.updateId()

try:
    logging.info(abhi.__id)
except:
    logging.info('Private objects must be accessed with ._<class name>__ ')

    