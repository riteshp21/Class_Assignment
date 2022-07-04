import logging

logging.basicConfig(filename="class_string_log.log", level=logging.INFO,
                    format='%(levelname)s %(name)s %(asctime)s %(message)s')

s = "this is My First Python Programming class and i am learning python string and its function"


class test_string:
    # Extract data from index one to index 300 with a jump of 3
    def extract_data(self, s):
        try:
            logging.info("Extract data from string is : %s  ", s[1:300:3])
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

    # try to reverse string without using function

    def reverse_string(self, s):
        try:
            logging.info("Reversed string is : %s  ", s[len(s):0:-1])
        except Exception:
            logging.error("Exception occurred", exc_info=True)

    # try to split a string after conversion of entire string n upper case
    def string_upper_split(self, s):
        try:
            string_upper = s.upper()
            string_split = string_upper.split()
            logging.info("Upper string and splitted is : %s ", string_split)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

    # try to convert whole string into lower case

    def string_lower(self, s):
        try:
            string_lower = s.lower()
            logging.info("Lower case string is : %s ", string_lower)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

    # replace string char by another char taking you own example

    def replace_char(self, s):
        try:
            if "function" in s:
                replace_string = s.replace("function", "class")
                logging.info("replacing function in string with class : %s", replace_string)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)


string1 = test_string()
string1.extract_data(s)
string1.reverse_string(s)
string1.string_upper_split(s)
string1.string_lower(s)
string1.replace_char(s)
