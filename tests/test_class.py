from testing.classes import Pet, Cat , Dog
import pytest
"""
Test Class
"""
"""

def test_petCounter(data):
    assert Pet.petCount() == 4

def test_catHair(data):
    assert data[0].hair == True
    assert data[1].hair == False

def test_dogAge(data):
    assert data[2].age == 10
    assert data[3].age == 19

@pytest.fixture
def data():
    cat1 = Cat('Cat1',4,True)
    cat2 = Cat('Cat2',5,False)
    dog1 = Dog('Dog1',10)
    dog2 = Dog('Dog2',19)
    return[cat1,cat2,dog1,dog2]

"""
"""
End Test Class
"""