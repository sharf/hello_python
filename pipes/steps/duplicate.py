import logging

class Step(object):

    def run(self, input):
        REPLICATE_COUNT = 2
        logging.info('Converting to uppercase')        
        input['DUP'] = ' '.join(input['original'] for x in xrange(REPLICATE_COUNT))
