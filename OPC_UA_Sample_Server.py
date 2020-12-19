
from opcua import ua, Server as OPC_UA_Server

if __name__ == "__main__":
    server = OPC_UA_Server()
    server.set_endpoint("opc.tcp://localhost:4840/sampleopcuaserver/")
    uri = "plc.sample1"
    idx = server.register_namespace(uri)
    objects = server.get_objects_node()
    myobj = objects.add_object(idx, "PLC_Sample_1")
    myobj.add_variable(idx, "Sample Double Value", 0.1)
    myobj.add_variable(idx, "Sample String Value", "Sample 1")

    uri = "plc.sample2"
    idx = server.register_namespace(uri)
    objects = server.get_objects_node()
    myobj = objects.add_object(idx, "PLC_Sample_2")
    myobj.add_variable(idx, "Sample Double Value", 0.1)
    myobj.add_variable(idx, "Sample String Value", "Sample 2")
    server.start()