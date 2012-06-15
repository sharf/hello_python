from nose.tools import eq_
from pipes.lib.pipeline import Pipeline

def test_uppercase():
  input = {'original': 'Hello'}
  pipeline = Pipeline()
  pipeline.run(input)
  eq_(input['UCASE'],'HELLO')
