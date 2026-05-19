from scapy.all import sniff, IP, TCP, UDP
import joblib
import pandas as pd

# Load model, label encoder and feature columns
model = joblib.load("cicids_model.pkl")
encoder = joblib.load("cicids_label_encoder.pkl")
feature_columns = joblib.load("feature_columns.pkl")

def analyze(packet):
    if IP in packet:
        # Initialize all 78 columns to 0.0
        sample_dict = {col: 0.0 for col in feature_columns}
        
        packet_len = len(packet)
        
        # Map single packet length metrics
        if 'Min Packet Length' in sample_dict:
            sample_dict['Min Packet Length'] = float(packet_len)
        if 'Max Packet Length' in sample_dict:
            sample_dict['Max Packet Length'] = float(packet_len)
        if 'Packet Length Mean' in sample_dict:
            sample_dict['Packet Length Mean'] = float(packet_len)
        if 'Average Packet Size' in sample_dict:
            sample_dict['Average Packet Size'] = float(packet_len)
            
        # Map transport layer details
        if TCP in packet:
            if 'Destination Port' in sample_dict:
                sample_dict['Destination Port'] = float(packet[TCP].dport)
            
            # Extract TCP Flags
            flags = packet[TCP].flags
            if 'SYN Flag Count' in sample_dict and 'S' in flags:
                sample_dict['SYN Flag Count'] = 1.0
            if 'ACK Flag Count' in sample_dict and 'A' in flags:
                sample_dict['ACK Flag Count'] = 1.0
            if 'FIN Flag Count' in sample_dict and 'F' in flags:
                sample_dict['FIN Flag Count'] = 1.0
            if 'RST Flag Count' in sample_dict and 'R' in flags:
                sample_dict['RST Flag Count'] = 1.0
            if 'PSH Flag Count' in sample_dict and 'P' in flags:
                sample_dict['PSH Flag Count'] = 1.0
            if 'URG Flag Count' in sample_dict and 'U' in flags:
                sample_dict['URG Flag Count'] = 1.0
                
        elif UDP in packet:
            if 'Destination Port' in sample_dict:
                sample_dict['Destination Port'] = float(packet[UDP].dport)

        # Convert to DataFrame with columns in the exact order the model expects
        df_sample = pd.DataFrame([sample_dict], columns=feature_columns)
        
        # Predict threat using the trained model
        prediction = model.predict(df_sample)
        
        # Decode the predicted class using the LabelEncoder
        result = encoder.inverse_transform(prediction)[0]
        
        # Human-friendly display
        status = "🔴 Threat" if result != "BENIGN" else "🟢 Normal"
        print(f"[{status}] Traffic type: {result} | Dst Port: {sample_dict.get('Destination Port', 0)} | Len: {packet_len}")

try:
    print("Monitoring Started (Sniffing 10 IP packets)...")
    sniff(filter="ip", prn=analyze, count=10)
except Exception as e:
    print(f"Live sniffing failed ({e}).\nFalling back to offline 'live_capture.pcap' analysis...")
    sniff(offline="live_capture.pcap", filter="ip", prn=analyze, count=10)