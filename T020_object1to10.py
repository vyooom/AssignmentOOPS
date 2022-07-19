import logging
logging.basicConfig(filename='logTask_020_objects',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Objects :- Examples')

class Ineuron:
    '''Initializing a class of Ineuron with a variable intro'''

    def __init__(self, course):
        self.intro = 'This is a class of ' + course + ' at iNeuron.'

    def show(self):
        return self.intro


obj1 = Ineuron('fsds')
obj2 = Ineuron('stats')
obj3 = Ineuron('javascript')
obj4 = Ineuron('Data Structures')
obj5 = Ineuron('Data Analyst')
obj6 = Ineuron('C++')
obj7 = Ineuron('SQL')
obj8 = Ineuron('Nodejs')
obj9 = Ineuron('Blockchain')
obj10 = Ineuron('Web Development')

counter = 1
for i in (obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10):
    logging.info('Course number: %s'%counter)
    logging.info(i.show())
    counter += 1
    



