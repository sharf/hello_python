import logging

class Step(object):
#Replicates the given input strings and appends the same to input string
#Input:string
#Output:string string
    def run(self, input):
        REPLICATE_COUNT = 2
        logging.info('Adding duplicate')        
        input['DUP'] = ' '.join(input['original'] for x in xrange(REPLICATE_COUNT))
