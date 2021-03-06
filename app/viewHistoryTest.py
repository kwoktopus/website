from .exceptions import *
from .models import *
import pytest
from . import db
# include the . before the directory

ian = User.query.filter_by(email = 'ian@gmail.com').first()
#provider is ian

# all of these tests should probably be in a class for test_view_patient_history
# each of these probably needs more than just a single test

def test_has_permission(): # has permission because they have an appointment with patient
    hao = User.query.filter_by(email = 'hao@gmail.com').first()
    assert(checkViewHistory(ian, hao) == True)

def test_no_current_app_with_patient(): # no permission because if provider doesn't have an appointment with patient
    jack = User.query.filter_by(email = 'jack@gmail.com').first()    
    assert(checkViewHistory(ian, jack) == False)
    

def test_not_a_provider(): # patients can't view patietn history
    hao = User.query.filter_by(email = 'hao@gmail.com').first()    
    tom = User.query.filter_by(email = 'tom@gmail.com').first() 
    assert(checkViewHistory(tom, hao) == False)

def xd(): # need to start everything with test_
    assert(False)

#unconmment this and it will fail 
#def test_fail():
#    assert(False)    


# check exceptions.py and routes 

# run in virtual env
# pip3 install pytest <<<< if you're virtual env doesn't have it
# pytest viewHistoryTest.py

