import logging
logging.basicConfig(filename='logTask_103_polymorph04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Polymorphism :- Example - 04')

class OOPS:
    def intro(self):
        logging.info("Today's class is about OOPS at Ineuron.")

    def duration(self, d):
        a = d*3
        logging.info("The duration of OOPS class is %s days."%a)

class Loop:
    def intro(self):
        logging.info("Today's class is about loops at Ineuron.")

    def duration(self, d):
        a = d * 2
        logging.info("The duration of loops class is %s days."%a)


a = OOPS()
b = Loop()

for i in (a,b):
    i.intro()
    i.duration(2)

