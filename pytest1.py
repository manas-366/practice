import pytest
@pytest.fixture
def Setup():
    print('Setup Function')

def test1(Setup):
    print('Run Again')

def fun4():
    return 2+10

@pytest.mark.run(order=1)
def test2():
    print("doesn't run setup function")    
    a=fun4()
    assert a==12
    print('okay')

def test3(Setup):
    print('run again after setup function')