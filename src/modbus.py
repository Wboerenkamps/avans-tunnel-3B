from pyModbusTCP.client import ModbusClient

class modbus:
    c: ModbusClient

    def __init__(self,ip:str):
        self.port = 502
        self.c = ModbusClient(host=ip, port=self.port, auto_open=True)
        

    def get(self, start_addr, len: int = 1):
        regs = self.c.read_holding_registers(start_addr, len)
        if regs:
            return regs
        else:
            #ToDo add Error handling here
            return None
   
        # data is array of ints for subsequent addresses.
    def set(self, start_addr: int, data):
        return self.c.write_multiple_registers(start_addr, data)
