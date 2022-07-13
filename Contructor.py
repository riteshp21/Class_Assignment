import logging
logging.basicConfig(filename="contructor.log", level=logging.INFO, format='%(levelname)s %(name)s %(asctime)s %(message)s')

class Ineuron:

    def __init__(self, Data_science):
        self.course = Data_science

    def ineuron_courses(self):

        m = "Press 1 : For Data Science   \n 2 : Development \n 3 : Programming"
        logging.info(m)
        Course_Name = input("Press 1 : For Data Science   \n 2 : Development \n 3 : Programming  \n")
        logging.info("You have entered :%s",Course_Name)
        try:
            if Course_Name == "1":
                logging.info ("You choose Data Science")
            elif Course_Name == "2":
                logging.info("You Choose Development")
            elif Course_Name == "3":
                logging.info("You Choose Programming")

        except Exception as e:
            logging.error("Error has been occured", exc_info=True)


n=Ineuron("Data1")
n.ineuron_courses()
