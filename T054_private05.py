import logging
logging.basicConfig(filename='logTask_054_private05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Private :- Example - 05')

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

'''Changing a private object and using it again in the same class.'''

