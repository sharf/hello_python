import logging
import datetime

class Step(object):
#Appends date to input string
#Input:string
#Output:string:MM-DD-YYYY
    def run(self, input):
        try:
          today = datetime.datetime.now()
#Operations performed inside the if block are only valid for input as a dict of str values
          if type(input) is dict and type(input['original']) is str:
            logging.info('Appending date to string')        
            input['DATE'] = input['original'] + today.strftime(":%m-%d-%Y")
          else:
            raise ValueError

        except KeyError:
          input['DATE'] = today.strftime(":%m-%d-%Y")
