import logging
logging.basicConfig(filename="Inheritance.log", level=logging.INFO, format = "%(levelname)s %(name)s %(asctime)s %(message)s")

#multilevel inheritance
class IneuronCourse:

    def __init__(self):
        self.course1 = input("Please choose course 1: DATA SCIENCE n\ 2 : Web Development")

    def course_instructor(self):
        try:
            if self.course1 == "1":
                logging.info(f"Course Instructor for DATA SCIENCE is Sudhansu")
            elif self.course1 == "2":
                logging.info(f"Course Instructor for Web Development is Hitesh")
        except Exception as e:
            logging.error("Error hase been occured ", exc_info=True)


class IneuronSyllabus(IneuronCourse):

    def datascience_syllabus(self):
        logging.info("Python,Stats,Machine learning,Deep learning,Computer vision,Natural language processing")

    def web_development_syllabus(self):
        logging.info("JavaScript, HTML,CSS")

class Ineuron(IneuronSyllabus):

    def Ineuron_affiliate(self):

        logging.info("Attain financial freedom by under-line joining our affiliate program")

#multiple inheritance

class internship:
    def register_internship(self):
        name1 =input("Enter your name")
        password1 = input("Enter your password")
        try:
            logging.info("User name is %s:",name1)
            logging.info("User password is %s:",password1)
        except Exception as e:
            logging.error("Some thing went wrong", exc_info=True)

class blog:

    def ineuron_blog(self):

        logging.info("Go to Ineuron Blog")
        return "Go to Ineuron Blog"


class Ineuron1(internship,blog):
    logging.info("We are in Ineuron combined class")


i=Ineuron()
#i.course_instructor()
#i.datascience_syllabus()
#i.Ineuron_affiliate()

#i1= Ineuron1()
#i1.register_internship()
#i1.ineuron_blog()




