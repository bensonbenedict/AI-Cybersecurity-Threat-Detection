from scapy.all import sniff, IP, TCP, UDP

def extract_features(packet):
    if IP in packet:
        packet_length = len(packet)
        protocol = packet[IP].proto

        src_port = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else 0
        dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else 0

        print({
            "packet_length": packet_length,
            "protocol": protocol,
            "src_port": src_port,
            "dst_port": dst_port
        })

sniff(prn=extract_features, count=5)