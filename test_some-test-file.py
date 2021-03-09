# This file starts with test_, thus it will get run by the Azure testing pipeline
def fun(a):
    return a - 1

def test-method():
    assert fun(6) == 5