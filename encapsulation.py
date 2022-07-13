
import logging
logging.basicConfig(filename="encapsulation.log", level=logging.INFO, format = "%(levelname)s %(name)s %(asctime)s %(message)s")

class ineuron:

    def __init__(self, course):

        self.__course = course

    def ineuron_course(self):

        try:
            logging.info("Ineuron Course : %s", self.__course)

        except Exception as e:
            logging.error("Error has been occured ", exc_info=True)


i = ineuron('Data Science')
i.ineuron_course()
#print(i._ineuron__course)

