class order:

    def __init__(self, mynum):
        self.OrderID = int(mynum)
        self.OrderType = "Limit"

    def setOrderID(self, mynum):
        self.OrderID = int(mynum)
        return self
    
    def inc11mod(self, modval):
        self.OrderID  = self.modOrderIDby(self.OrderID, 11, modval)
        return self

    @staticmethod
    def incrementOrderID(mynum, incval):
        return (int(mynum) * int(incval))

    @classmethod
    def modOrderIDby(cls, orderid, inc, val):
        return (cls.incrementOrderID(orderid, inc) % val)
    
y = order(81456834)
print(f"Original::OrderID={y.OrderID},OrderType={y.OrderType}")
y.inc11mod(5)
print(f"AfterMod5::OrderID={y.OrderID},OrderType={y.OrderType}")
 