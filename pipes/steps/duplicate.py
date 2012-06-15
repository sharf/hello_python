import logging

class Step(object):
#Replicates the given input strings and appends the same to input string
#Input:string
#Output:string string
    def run(self, input):
        try:
#Operations performed inside the if block are only valid for input as a dict of str values
          if type(input) is dict and type(input['original']) is str:
            REPLICATE_COUNT = 2
            logging.info('Adding duplicate')        
            input['DUP'] = ' '.join(input['original'] for x in xrange(REPLICATE_COUNT))
        except KeyError:
          input['DUP'] = '' 
