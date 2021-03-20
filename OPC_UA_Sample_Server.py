
from opcua import ua, Server as OPC_UA_Server
import threading
    
class Sampe_Server:
    def __init__(self):
        self.i = 0.1
        self.server = OPC_UA_Server()
        self.server.set_endpoint("opc.tcp://localhost:4840/sampleopcuaserver/")
        uri = "machine.sample1"
        idx = self.server.register_namespace(uri)
        objects = self.server.get_objects_node()
        myobj = objects.add_object(idx, "Machine_Sample_1")
        self.obj = myobj.add_variable(idx, "Sample Double Value", 0.1)
        myobj.add_variable(idx, "Sample String Value", "Sample 1")
        uri = "machine.sample2"
        idx = self.server.register_namespace(uri)
        objects = self.server.get_objects_node()
        myobj = objects.add_object(idx, "Machine Sample")
        myobj.add_variable(idx, "Sample Double Value", 0.1)
        myobj.add_variable(idx, "Sample String Value", "Sample 2")
        self.server.start()
    def Start(self):
        self.event = threading.Timer(1, self.Change_value)
        self.event.deamon = True
        self.event.start()
    def Change_value(self):
        self.i = self.i + 0.1
        if self.i> 10000:
            self.i = 0.0
        self.obj.set_value(self.i)
        self.Start()

import OPC_UA_Sample_Server
if __name__ == "__main__":
    server = Sampe_Server()
    server.Start()