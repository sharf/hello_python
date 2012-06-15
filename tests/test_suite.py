from nose.tools import eq_
from pipes.lib.pipeline import Pipeline
import datetime

class TestSuite:
  def test_uppercase(self):
    input = {'original': 'Hello'}
    pipeline = Pipeline()
    pipeline.run(input)
    eq_(input['UCASE'],'HELLO')

  def test_duplicate(self):
    input = {'original': 'Hello'}
    pipeline = Pipeline()
    pipeline.run(input)
    eq_(input['DUP'], 'Hello Hello')

  def test_date(self):
    input = {'original': 'Hello'}
    pipeline = Pipeline()
    pipeline.run(input)
    now = datetime.datetime.now()
    eq_(input['DATE'], 'Hello'+ now.strftime(":%m-%d-%Y"))
