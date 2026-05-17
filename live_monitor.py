from scapy.all import sniff, IP, TCP, UDP
import joblib

model = joblib.load("cicids_model.pkl")

threat_map = {
    0:"Normal Traffic",
    1:"DDoS Attack",
    2:"Phishing",
    3:"Ransomware",
    4:"Botnet",
    5:"Trojan"
}

def analyze(packet):

    if IP in packet:

        sample = [[0] * 78]

        sample[0][0] = len(packet)
        sample[0][1] = packet[IP].proto

        if TCP in packet:
            sample[0][2] = packet[TCP].sport
            sample[0][3] = packet[TCP].dport

        elif UDP in packet:
            sample[0][2] = packet[UDP].sport
            sample[0][3] = packet[UDP].dport

        prediction = model.predict(sample)

        result = threat_map.get(
            int(prediction[0]),
            "Unknown"
        )

        print("Traffic:", result)

print("Monitoring Started...")

sniff(prn=analyze,count=10)