import pandas as pd
import streamlit as st
import joblib

# Page setup
st.set_page_config(
    page_title="AI Cybersecurity Threat Detection",
    layout="wide"
)

# Title
st.title("AI Cybersecurity Threat Detection Dashboard")

st.write(
    "This dashboard shows model-based threat prediction and packet analysis."
)

# Load model
model = joblib.load("cicids_model.pkl")

# Heading
st.subheader("Threat Prediction Test")

st.subheader("Live Packet Inputs")

# Input fields
packet_length = st.number_input(
    "Packet Length",
    value=1494
)

protocol = st.number_input(
    "Protocol",
    value=6
)

src_port = st.number_input(
    "Source Port",
    value=65218
)

dst_port = st.number_input(
    "Destination Port",
    value=443
)

# Create 34-feature input
sample = [[0] * 78]

# Fill first features with real values
sample[0][0] = packet_length
sample[0][1] = protocol
sample[0][2] = src_port
sample[0][3] = dst_port

# Prediction
if st.button("Predict Threat"):

    prediction = model.predict(sample)

    threat_map = {
        0: "Normal Traffic",
        1: "DDoS Attack",
        2: "Phishing",
        3: "Ransomware",
        4: "Botnet",
        5: "Trojan"
    }

    result = threat_map.get(
        int(prediction[0]),
        "Unknown Threat"
    )

    if result == "Normal Traffic":
        st.success("🟢 Safe Traffic Detected")

    else:
        st.error(
            f"🚨 Threat Detected: {result}"
        )

        import pandas as pd

st.subheader("Upload CICIDS CSV for Accurate Prediction")

uploaded_file = st.file_uploader(
    "Upload CICIDS CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    data.columns = data.columns.str.strip()

    if "Label" in data.columns:
        data = data.drop("Label", axis=1)

    data = data.replace([float("inf"), float("-inf")], 0)
    data = data.fillna(0)

    encoder = joblib.load("cicids_label_encoder.pkl")

    feature_columns = joblib.load("feature_columns.pkl")

    data = data[feature_columns]

    predictions = model.predict(data)

    decoded = encoder.inverse_transform(predictions)

    st.write("Sample Attack Predictions:")
    attack_rows = decoded[decoded != "Normal"]
    st.write(attack_rows[:20])
    st.write("Prediction Summary:")
    st.write(pd.Series(decoded).value_counts())