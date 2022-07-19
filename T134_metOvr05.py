import logging
logging.basicConfig(filename='logTask_134_methodOver05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Method OverRidding :- Example:- 05')

class IneuronFSDS:
    def __init__(self, duration):
        self.duration = duration

    def show(self):
        logging.info('The duration of this course in months: %s'%self.duration)

class Stats(IneuronFSDS):
    def __init__(self, duration):
        super().__init__(duration)
        self.duration = self.duration*10

    def show(self):
        super().show()


a = IneuronFSDS(12)
b = Stats(2)
a.show()
b.show()
