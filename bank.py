
import sys
def bankOper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updateBal = totalBal - withdraw

    return totalBal, updateBal
if __name__=="__main__":
    
    initialBal = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])

    totalBal, updatedBal =bankOper(initialBal, deposit, withdraw)

    print("Total Balance:",totalBal)
    print("Updated Balance:",updatedBal)