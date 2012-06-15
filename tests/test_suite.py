from nose.tools import eq_
from pipes.lib.pipeline import Pipeline
import datetime

def test_uppercase():
  input = {'original': 'Hello'}
  pipeline = Pipeline()
  pipeline.run(input)
  eq_(input['UCASE'],'HELLO')

def test_duplicate():
  input = {'original': 'Hello'}
  pipeline = Pipeline()
  pipeline.run(input)
  eq_(input['DUP'], 'Hello Hello')

def test_date():
  input = {'original': 'Hello'}
  pipeline = Pipeline()
  pipeline.run(input)
  now = datetime.datetime.now()
  eq_(input['DATE'], 'Hello'+ now.strftime(":%m-%d-%Y"))
