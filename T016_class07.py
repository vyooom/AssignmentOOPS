import logging
logging.basicConfig(filename='logTask_016_class07',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 07')

class IneuronPeriod:
    '''Defining internship period in months'''
    def __init__(self):
        self.period = 0
        logging.info('The period of the internship is %s months.'%self.period)

    def updateDuration(self, period):
        self.period = period
        logging.info('The updated period of internship is %s months.'%self.period)

    def intro(self):
        logging.info('Your internship is of %s months.'%self.period)
        return 'Your internship is of %s months.'%self.period


abhi = IneuronPeriod()
abhi.intro()
abhi.updateDuration(6)
abhi.intro()


