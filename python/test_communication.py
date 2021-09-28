from scanviz.communication import Communication

if __name__ == "__main__":
    comms = Communication()
    print(comms.send_recieve("M", "1"))
    print(comms.send_recieve("M", "2"))
    print(comms.send_recieve("M", "3"))
    print(comms.send_recieve("S", "1"))
    print(comms.send_recieve("S", "2"))
    print(comms.send_recieve("S", "3"))
    print(comms.send_recieve("M", "1"))
    print(comms.send_recieve("S", "2"))
    print(comms.send_recieve("M", "3"))
