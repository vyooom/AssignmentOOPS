import logging
logging.basicConfig(filename='logTask_082_abstract03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Abstraction :- Example - 03')

class IneuronDB:
    '''The third example of abstraction.'''

    def __init__(self, name = None):
       self.l = list(name) if name is not None else []

    def updateDB(self, *names):
        '''Updating the name of a student in the list.'''
        try:
            for i in names:
                if type(i) == str:
                    # list.append doesn't work in this case
                    # we have to resort to addition
                    self.l += [i]
                else:
                    continue

            logging.info('The updated list of student is %s.'%self.l)
        except:
            logging.error('Please enter a valid string.')

    def showDB(self):
        logging.info('The list of current students in iNeuron is %s'%self.l)
        return self.l


a = IneuronDB()
a.updateDB('abhishek')
a.showDB()

a.updateDB('suman', 'sunny', 'shekhar', 'gaurav', 'jayant')
a.showDB()




