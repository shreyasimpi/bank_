from bank import bankOper

def test_deposit():
    totalBalance , updatedBalance = bankOper(200000, 30000, 0)

    assert totalBalance == 23000
    assert updatedBalance == 23000

def test_withdraw():
    totalBalance, updatedBalance = bankOper(100000, 40000, 10000)
    assert totalBalance == 140000
    assert updatedBalance == 130000

def test_anyamount():
    totalBalance, updatedBalance = bankOper(150000, 0, 15000)
    assert totalBalance == 150000
    assert updatedBalance == 135000