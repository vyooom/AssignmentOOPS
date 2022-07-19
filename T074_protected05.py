import logging
logging.basicConfig(filename='logTask_074_protected05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Protected :- Example - 05')

class Ineuron:
    '''Fifth example protected object.'''

    def __init__(self, id):
        try:
            if type(id) == int:
                self._id = id
            else:
                raise Exception
        except:
            logging.error('Initialization needs a integer.')


    def showId(self):
        logging.info('The current id is %s'%self._id)
        return self._id

    def updateId(self):
        self._id = self._id + 10
        logging.info('The current id is %s'%self._id)
        return self._id



abhi = Ineuron(5)
abhi.showId()
abhi.updateId()
abhi._id = abhi._id -7
abhi.showId()
abhi.updateId()

try:
    logging.info(abhi.id)
except:
    logging.info('Protected objects must be accessed with ._')

'''Changing a protected object and using it again in the same class.'''


