import logging
logging.basicConfig(filename="privatrprotected.log", level=logging.INFO, format='%(levelname)s %(name)s %(asctime)s %(message)s')

class Ineuron:

    def __init__(self,course1,course2):
        self._course1 = "Data Science"
        self.__course2 = "Data Analyst"

    def ineuroncourse(self):

        logging.info(f"Pubic variable accessed Offered Coursers are {self._course1} and {self.__course2}")

    def __ineuroncourse(self):

        logging.info(f"Private variable accessed Offered Coursers are {self._course1} and {self.__course2}")


i=Ineuron("Data Science","Data Analyst")
i._Ineuron__ineuroncourse()
i.ineuroncourse()




