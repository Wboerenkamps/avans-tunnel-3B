from modbus import *

MODBUS_PLC_IP = "192.168.10.1"
MODBUS_AFSLUITBOOM_IP = MODBUS_PLC_IP
class Afsluitboom:
    def __init__(self):
        
        self.Bereikbaar = 0
        self.Stand = 0
        self.Flash = 0
        self.Storing = 0
        self.Beweging = 0
        self.Obstakel = 0

        self.ModbusInstance = modbus(MODBUS_AFSLUITBOOM_IP)

        self.SetStand([self.Stand])

        

    def update(self):
        regs = self.ModbusInstance.get(1006, 6) 
        if regs:
            self.Stand = regs[1]
            self.Bereikbaar = regs[2]  
            self.Beweging = regs[3]
            self.Obstakel = regs[4]
            self.Storing = regs[5]

    def SetStand(self, value):
        if self.Bereikbaar:
            return self.ModbusInstance.set(1006, value)


        
