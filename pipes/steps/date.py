import logging
import datetime

class Step(object):

    def run(self, input):
        logging.info('Appending date to string')        
        today = datetime.datetime.now()
        input['DATE'] = input['original'] + today.strftime(":%m-%d-%Y")
