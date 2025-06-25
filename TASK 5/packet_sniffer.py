from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def process_packet(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"\n[+] Packet Captured at {timestamp}")
        print(f"    Source IP      : {src_ip}")
        print(f"    Destination IP : {dst_ip}")
        print(f"    Protocol       : {protocol} ({get_protocol_name(protocol)})")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    Payload        : {payload[:50]}...")  # Show first 50 bytes

def get_protocol_name(proto_number):
    return {
        6: "TCP",
        17: "UDP",
        1: "ICMP"
    }.get(proto_number, "OTHER")

def start_sniffing():
    print("[*] Starting packet sniffer (Press Ctrl+C to stop)...\n")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()
