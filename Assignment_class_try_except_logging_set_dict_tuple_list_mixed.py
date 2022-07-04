import logging

logging.basicConfig(filename="class_test_mixed.log", level=logging.INFO,
                    format='%(levelname)s %(name)s %(asctime)s %(message)s')

lst = [[1,2,3,4], (2,3,4,5,6),(3,4,5,6), set([23,4,5,6,7,45,6]) ,{"k1":"sudh", "k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]

class test_mixed:
    # Extract all list entities
    def extract_list(self, lst):

        try:
            list_extract = []
            for i in lst:

                if type(i) == list:
                    list_extract.append(i)
            logging.info("Extracted list is %s", list_extract)

        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

    # Extract all dict entities
    def extract_dict(self, lst):

        try:
            dict_extract = {}
            for i in lst:

                if type(i) == dict:
                    for key, value in i.items():
                        dict_extract[key]=value

            logging.info("Extracted list is %s", dict_extract)

        except Exception as e:
            logging.error("Exception occurred", exc_info=True)


    # Extract all tuple entities
    def extract_tuple(self, lst):

        try:
            tuple_extract = ()
            for i in lst:
                if type(i) == tuple:
                    tuple_extract += i
            logging.info("Extracted tuple is %s", tuple_extract)

        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

    # Extract all numerical  data
    def extract_num(self, lst):
        try:
            number_extract = []

            for i in lst:
                if type(i) == int:
                    number_extract.append(i)
                if type(i) == tuple or type(i)== set or type(i)==list:
                    for num in i:
                        if type(num)== int:
                            number_extract.append(num)
                elif type(i) == dict:
                    for key,value in i.items():

                        if type(key)==int:
                            number_extract.append(key)
                        if type(value)==int:
                            number_extract.append(value)

            logging.info("Extracted number is %s", number_extract)
            logging.info("Sum of all number is %s",sum(number_extract))
            logging.info("Odd numbers are : %s", list(filter(lambda x : x%2 != 0, number_extract)))

        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
    #Find "ineuron" in list:
    def find_ineuron(self,lst):
        try:
            for x in lst:
                if "ineuron" in x:
                    logging.info('"Ineuron" found in : %s', lst)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)



list1=test_mixed()
list1.extract_list(lst)
list1.extract_dict(lst)
list1.extract_tuple(lst)
list1.extract_num(lst)
list1.find_ineuron(lst)