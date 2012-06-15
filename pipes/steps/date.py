import logging
import datetime

class Step(object):
#Appends date to input string
#Input:string
#Output:string:MM-DD-YYYY
    def run(self, input):
        logging.info('Appending date to string')        
        today = datetime.datetime.now()
        input['DATE'] = input['original'] + today.strftime(":%m-%d-%Y")
