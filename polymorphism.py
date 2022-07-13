import logging
logging.basicConfig(filename="polymorphism.log", level=logging.INFO, format="%(levelname)s %(name)s %(asctime)s %(message)s")



class ineuron:

    def ineuron_course(self):
        pass
        logging.info("Ineuron courses are Data Science, Data Analyst, Web Development ")


class DataScience:

    def mentor(self):
        return "Data Science mentor : Sudhansu, Krish, Sunny"

class WebDevelopment:

    def mentor(self):
        return "Web Development mentor : Hitesh , Surya , Shubham "

def ineuron_team(name):
    try:
        logging.info(name.mentor())
    except Exception as e:
        logging.error("Error has been occured", exc_info=True)



name1 = DataScience()
name2 = WebDevelopment()
ineuron_team(name1)
ineuron_team(name2)












