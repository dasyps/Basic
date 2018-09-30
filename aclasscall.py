from copy import deepcopy

class order:

    def __init__(self, mynum):
        self.OrderID = int(mynum)
        self.OrderType = "Limit"

    def setOrderID(self, mynum):
        self.OrderID = int(mynum)
        return self
    
    def inc11mod5(self):
        self.OrderID  = self.modOrderIDby(self.OrderID, 11, 5)
        return self

    @staticmethod
    def incrementOrderID(mynum, incval):
        return (int(mynum) * int(incval))

    @classmethod
    def modOrderIDby(cls, orderid, inc, val):
        return (cls.incrementOrderID(orderid, inc) % val)
    
y = order(10)
print(f"{y.OrderID}:{y.OrderType}")
y.inc11mod5()
print(f"{y.OrderID}:{y.OrderType}")


 