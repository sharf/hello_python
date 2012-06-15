import logging

class Step(object):
#Converts the given input string to uppercase
#Input:string
#Output:STRING
    def run(self, input):
        try:
#Operations performed inside the if block are only valid for input as a dict of str values
          if type(input) is dict and type(input['original']) is str:
            logging.info('Converting to uppercase')        
            input['UCASE'] = input['original'].upper()
          else:
            raise ValueError

        except KeyError:
          input['UCASE'] = ''
