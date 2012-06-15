import logging

class Step(object):
#Converts the given input string to uppercase
#Input:string
#Output:STRING
    def run(self, input):
        logging.info('Converting to uppercase')        
        input['UCASE'] = input['original'].upper()
