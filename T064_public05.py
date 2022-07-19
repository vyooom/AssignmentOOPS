import logging
logging.basicConfig(filename='logTask_064_public05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Public :- Example - 05')

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

'''Changing a public object and using it again in the same class.'''

