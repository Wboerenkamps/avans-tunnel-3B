from modbus import *

MODBUS_MATRIXBOORD_IP = "192.168.10.111"

class Matrix:
    def __init__(self):
        self.Bereikbaar = 0
        self.Stand = 0
        self.Flash = 0
        self.Storing = 0
        self.ModbusInstance = modbus(MODBUS_MATRIXBOORD_IP)
        
        self.SetStand([self.Stand])

    def update(self):
        regs = self.ModbusInstance.get(7010, 5)
        if regs:
            self.Stand = regs[1]
            self.Bereikbaar = regs[2]  
            self.Flash = regs[3]
            self.Storing = regs[4]

    def SetStand(self, value):
       return self.ModbusInstance.set(7000, value)


        
