#use pytest to test the functions in app.py file
import pytest
from app import add     
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
#define test function to test the subtract function
from app import subtract    
def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
#define test function to test the multiply function
from app import multiply    
def test_multiply():
    assert multiply(4, 6) == 24
    assert multiply(0, 5) == 0
    assert multiply(-1, -1) == 1    

#add main function to run the tests 
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply() 
    print("All tests passed!")