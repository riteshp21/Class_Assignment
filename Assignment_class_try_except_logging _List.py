import logging

logging.basicConfig(filename="class_log.log", level=logging.INFO,
                    format='%(levelname)s %(name)s %(asctime)s %(message)s')

l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6), {"key1": "sudh", 2: 3}]

class Test1:
    logging.info("Actual list is %s",l)

#Reversing List
    def reverse_list(self, m):
        logging.info("reversing list")
        try:
            if len(m) == 0:
                logging.info("list is empty")
            else:
                m.reverse()
                logging.info("Reversed list is %s", m)
                return m
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

#Extracting 234 from List
    def extract_234(self,l):
        try:
            for i in l:
                if i == 234:
                    print("34")
                elif type(i) == tuple or type(i) == list:
                    for element in i:
                        if element == 234:
                            logging.info("234 is inside Set or list")
                else:
                    if type(i) == dict:
                        for key, value in i.items():
                            if value == 234:
                                print("234 is inside dict")
        except Exception as e    :
            logging.error("Error has occured", exc_info = True)


#Extracting list from mail List l

    def list_extraction(self,l):
        try:
            List = []
            for i in l:
                if type(i) == list:
                    List.extend(i)
            logging.info("Extracted list is %s", List)

        except Exception as e:
            logging.error("Error has been occured", exc_info=True)


#Extracting sudh from main list
    def extract_sudh(self,l):
        try:
            for i in l:
                if i == "sudh":
                    print("sudh")
                elif type(i) == tuple or type(i) == list:
                    for element in i:
                        if element == ("sudh"):
                            logging.info("sudh")
                else:
                    if type(i) == dict:
                        for key, value in i.items():
                            if value == "sudh":
                                logging.info(" 'sudh' is extrated from list")
        except Exception as e:
            logging.error("Error has been occured", exc_info=True)
#Extracting key from Dict inside list

    def extract_dict_key(self,l):
        try:
            dict_key = []
            for i in l:
                if type(i) == dict:
                    for key in i.keys():
                        dict_key.append(key)
            logging.info("Extracted key from Dict is %s", dict_key)

        except Exception as e:
            logging.error("Error has been occured", exc_info=True)

    def extract_dict_value(self,l):
        try:
            dict_value = []
            for i in l:
                if type(i) == dict:
                    for key in i.values():
                        dict_value.append(key)
            logging.info("Extracted key from Dict is %s", dict_value)

        except Exception as e:
            logging.error("Error has been occured", exc_info=True)





n=Test1()
n.extract_234(l)
n.reverse_list(l)
n.list_extraction(l)
n.extract_sudh(l)
n.extract_dict_key(l)
n.extract_dict_value(l)