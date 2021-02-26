import analysis

def test_onePlusOneEqualsTwo():
    result = analysis.addTwoNumbers(1, 1)
    assert (result == 2)

    
def test_twoNegativeNumbers():
    result = analysis.addTwoNumbers(-2, -3)
    assert (result == -5)