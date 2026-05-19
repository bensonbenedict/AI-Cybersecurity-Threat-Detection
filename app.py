import streamlit as st
import joblib
import pandas as pd
from ui_styles import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="AI Cyber Threat Intelligence",
    layout="wide"
)

# Apply premium animated cosmic styles
apply_custom_css()

# Header Section
st.title("AI Cybersecurity Threat Intelligence Dashboard")
st.markdown("##### Real-time network intrusion analysis & threat profiling using ML models.")

# Load models and assets
@st.cache_resource
def load_assets():
    model = joblib.load("cicids_model.pkl")
    encoder = joblib.load("cicids_label_encoder.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    return model, encoder, feature_columns

model, encoder, feature_columns = load_assets()

st.markdown("<br>", unsafe_allow_html=True)

# Main Application Tabs
tab_live, tab_batch = st.tabs(["Live Threat Predictor", "Batch CSV Traffic Analyzer"])

# ==================== TAB 1: LIVE THREAT PREDICTOR ====================
with tab_live:
    TEMPLATES = {
        "Custom (All Zeros)": {},
        "Normal Traffic (BENIGN)": {
            'Destination Port': 3268.0, 'Flow Duration': 112740690.0, 'Total Fwd Packets': 32.0, 'Total Backward Packets': 16.0, 
            'Total Length of Fwd Packets': 6448.0, 'Total Length of Bwd Packets': 1152.0, 'Fwd Packet Length Max': 403.0, 
            'Fwd Packet Length Mean': 201.5, 'Fwd Packet Length Std': 204.7, 'Bwd Packet Length Max': 72.0, 
            'Bwd Packet Length Min': 72.0, 'Bwd Packet Length Mean': 72.0, 'Flow Bytes/s': 67.4, 'Flow Packets/s': 0.42, 
            'Flow IAT Mean': 2398738.0, 'Flow IAT Std': 5798697.0, 'Flow IAT Max': 16400000.0, 'Flow IAT Min': 3.0, 
            'Fwd IAT Total': 113000000.0, 'Fwd IAT Mean': 3636796.0, 'Fwd IAT Std': 6848760.0, 'Fwd IAT Max': 16400000.0, 
            'Fwd IAT Min': 3.0, 'Bwd IAT Total': 113000000.0, 'Bwd IAT Mean': 7516023.0, 'Bwd IAT Std': 8323384.0, 
            'Bwd IAT Max': 16400000.0, 'Bwd IAT Min': 3.0, 'Fwd PSH Flags': 1.0, 'Fwd Header Length': 1024.0, 
            'Bwd Header Length': 512.0, 'Fwd Packets/s': 0.28, 'Bwd Packets/s': 0.14, 'Max Packet Length': 403.0, 
            'Packet Length Mean': 163.3, 'Packet Length Std': 178.9, 'Packet Length Variance': 32016.5, 'SYN Flag Count': 1.0, 
            'ACK Flag Count': 1.0, 'Average Packet Size': 166.7, 'Avg Fwd Segment Size': 201.5, 'Avg Bwd Segment Size': 72.0, 
            'Fwd Header Length.1': 1024.0, 'Subflow Fwd Packets': 32.0, 'Subflow Fwd Bytes': 6448.0, 'Subflow Bwd Packets': 16.0, 
            'Subflow Bwd Bytes': 1152.0, 'Init_Win_bytes_forward': 377.0, 'Init_Win_bytes_backward': 2079.0, 
            'act_data_pkt_fwd': 15.0, 'min_seg_size_forward': 32.0
        },
        "DDoS Attack": {
            'Destination Port': 80.0, 'Flow Duration': 1293792.0, 'Total Fwd Packets': 3.0, 'Total Backward Packets': 7.0, 
            'Total Length of Fwd Packets': 26.0, 'Total Length of Bwd Packets': 11607.0, 'Fwd Packet Length Max': 20.0, 
            'Fwd Packet Length Mean': 8.6, 'Fwd Packet Length Std': 10.2, 'Bwd Packet Length Max': 5840.0, 
            'Bwd Packet Length Mean': 1658.1, 'Bwd Packet Length Std': 2137.2, 'Flow Bytes/s': 8991.3, 'Flow Packets/s': 7.7, 
            'Flow IAT Mean': 143754.6, 'Flow IAT Std': 430865.8, 'Flow IAT Max': 1292730.0, 'Flow IAT Min': 2.0, 
            'Fwd IAT Total': 747.0, 'Fwd IAT Mean': 373.5, 'Fwd IAT Std': 523.9, 'Fwd IAT Max': 744.0, 'Fwd IAT Min': 3.0, 
            'Bwd IAT Total': 1293746.0, 'Bwd IAT Mean': 215624.3, 'Bwd IAT Std': 527671.9, 'Bwd IAT Max': 1292730.0, 
            'Bwd IAT Min': 2.0, 'Fwd Header Length': 72.0, 'Bwd Header Length': 152.0, 'Fwd Packets/s': 2.3, 'Bwd Packets/s': 5.4, 
            'Max Packet Length': 5840.0, 'Packet Length Mean': 1057.5, 'Packet Length Std': 1853.4, 'Packet Length Variance': 3435230.6, 
            'PSH Flag Count': 1.0, 'Down/Up Ratio': 2.0, 'Average Packet Size': 1163.3, 'Avg Fwd Segment Size': 8.6, 
            'Avg Bwd Segment Size': 1658.1, 'Fwd Header Length.1': 72.0, 'Subflow Fwd Packets': 3.0, 'Subflow Fwd Bytes': 26.0, 
            'Subflow Bwd Packets': 7.0, 'Subflow Bwd Bytes': 11607.0, 'Init_Win_bytes_forward': 8192.0, 
            'Init_Win_bytes_backward': 229.0, 'act_data_pkt_fwd': 2.0, 'min_seg_size_forward': 20.0
        },
        "PortScan Attack": {
            'Destination Port': 80.0, 'Flow Duration': 671.0, 'Total Fwd Packets': 2.0, 'Total Backward Packets': 1.0, 
            'Total Length of Fwd Packets': 8.0, 'Total Length of Bwd Packets': 2.0, 'Fwd Packet Length Max': 6.0, 
            'Fwd Packet Length Min': 2.0, 'Fwd Packet Length Mean': 4.0, 'Fwd Packet Length Std': 2.828427125, 
            'Bwd Packet Length Max': 2.0, 'Bwd Packet Length Min': 2.0, 'Bwd Packet Length Mean': 2.0, 'Bwd Packet Length Std': 0.0, 
            'Flow Bytes/s': 14903.12966, 'Flow Packets/s': 4470.938897, 'Flow IAT Mean': 335.5, 'Flow IAT Std': 296.2777413, 
            'Flow IAT Max': 545.0, 'Flow IAT Min': 126.0, 'Fwd IAT Total': 671.0, 'Fwd IAT Mean': 671.0, 'Fwd IAT Std': 0.0, 
            'Fwd IAT Max': 671.0, 'Fwd IAT Min': 671.0, 'Bwd IAT Total': 0.0, 'Bwd IAT Mean': 0.0, 'Bwd IAT Std': 0.0, 
            'Bwd IAT Max': 0.0, 'Bwd IAT Min': 0.0, 'Fwd PSH Flags': 0.0, 'Bwd PSH Flags': 0.0, 'Fwd URG Flags': 0.0, 
            'Bwd URG Flags': 0.0, 'Fwd Header Length': 44.0, 'Bwd Header Length': 24.0, 'Fwd Packets/s': 2980.625931, 
            'Bwd Packets/s': 1490.312966, 'Min Packet Length': 2.0, 'Max Packet Length': 6.0, 'Packet Length Mean': 3.0, 
            'Packet Length Std': 2.0, 'Packet Length Variance': 4.0, 'FIN Flag Count': 0.0, 'SYN Flag Count': 0.0, 
            'RST Flag Count': 0.0, 'PSH Flag Count': 1.0, 'ACK Flag Count': 0.0, 'URG Flag Count': 0.0, 'CWE Flag Count': 0.0, 
            'ECE Flag Count': 0.0, 'Down/Up Ratio': 0.0, 'Average Packet Size': 4.0, 'Avg Fwd Segment Size': 4.0, 
            'Avg Bwd Segment Size': 2.0, 'Fwd Header Length.1': 44.0, 'Fwd Avg Bytes/Bulk': 0.0, 'Fwd Avg Packets/Bulk': 0.0, 
            'Fwd Avg Bulk Rate': 0.0, 'Bwd Avg Bytes/Bulk': 0.0, 'Bwd Avg Packets/Bulk': 0.0, 'Bwd Avg Bulk Rate': 0.0, 
            'Subflow Fwd Packets': 2.0, 'Subflow Fwd Bytes': 8.0, 'Subflow Bwd Packets': 1.0, 'Subflow Bwd Bytes': 2.0, 
            'Init_Win_bytes_forward': 1024.0, 'Init_Win_bytes_backward': 29200.0, 'act_data_pkt_fwd': 1.0, 'min_seg_size_forward': 20.0, 
            'Active Mean': 0.0, 'Active Std': 0.0, 'Active Max': 0.0, 'Active Min': 0.0, 'Idle Mean': 0.0, 'Idle Std': 0.0, 
            'Idle Max': 0.0, 'Idle Min': 0.0
        },
        "Botnet Attack": {
            'Destination Port': 8080.0, 'Flow Duration': 134812.0, 'Total Fwd Packets': 4.0, 'Total Backward Packets': 3.0, 
            'Total Length of Fwd Packets': 206.0, 'Total Length of Bwd Packets': 134.0, 'Fwd Packet Length Max': 194.0, 
            'Fwd Packet Length Min': 0.0, 'Fwd Packet Length Mean': 51.5, 'Fwd Packet Length Std': 95.04209594, 
            'Bwd Packet Length Max': 128.0, 'Bwd Packet Length Min': 0.0, 'Bwd Packet Length Mean': 44.66666667, 
            'Bwd Packet Length Std': 72.23111056, 'Flow Bytes/s': 2522.03068, 'Flow Packets/s': 51.92416105, 
            'Flow IAT Mean': 22468.66667, 'Flow IAT Std': 53230.91125, 'Flow IAT Max': 131123.0, 'Flow IAT Min': 123.0, 
            'Fwd IAT Total': 134812.0, 'Fwd IAT Mean': 44937.33333, 'Fwd IAT Std': 76126.81717, 'Fwd IAT Max': 132841.0, 
            'Fwd IAT Min': 949.0, 'Bwd IAT Total': 132783.0, 'Bwd IAT Mean': 66391.5, 'Bwd IAT Std': 91544.16521, 
            'Bwd IAT Max': 131123.0, 'Bwd IAT Min': 1660.0, 'Fwd PSH Flags': 0.0, 'Bwd PSH Flags': 0.0, 'Fwd URG Flags': 0.0, 
            'Bwd URG Flags': 0.0, 'Fwd Header Length': 92.0, 'Bwd Header Length': 72.0, 'Fwd Packets/s': 29.67094917, 
            'Bwd Packets/s': 22.25321188, 'Min Packet Length': 0.0, 'Max Packet Length': 194.0, 'Packet Length Mean': 42.5, 
            'Packet Length Std': 75.2880184, 'Packet Length Variance': 5668.285714, 'FIN Flag Count': 0.0, 'SYN Flag Count': 0.0, 
            'RST Flag Count': 0.0, 'PSH Flag Count': 1.0, 'ACK Flag Count': 0.0, 'URG Flag Count': 0.0, 'CWE Flag Count': 0.0, 
            'ECE Flag Count': 0.0, 'Down/Up Ratio': 0.0, 'Average Packet Size': 48.57142857, 'Avg Fwd Segment Size': 51.5, 
            'Avg Bwd Segment Size': 44.66666667, 'Fwd Header Length.1': 92.0, 'Fwd Avg Bytes/Bulk': 0.0, 'Fwd Avg Packets/Bulk': 0.0, 
            'Fwd Avg Bulk Rate': 0.0, 'Bwd Avg Bytes/Bulk': 0.0, 'Bwd Avg Packets/Bulk': 0.0, 'Bwd Avg Bulk Rate': 0.0, 
            'Subflow Fwd Packets': 4.0, 'Subflow Fwd Bytes': 206.0, 'Subflow Bwd Packets': 3.0, 'Subflow Bwd Bytes': 134.0, 
            'Init_Win_bytes_forward': 8192.0, 'Init_Win_bytes_backward': 237.0, 'act_data_pkt_fwd': 3.0, 'min_seg_size_forward': 20.0, 
            'Active Mean': 0.0, 'Active Std': 0.0, 'Active Max': 0.0, 'Active Min': 0.0, 'Idle Mean': 0.0, 'Idle Std': 0.0, 
            'Idle Max': 0.0, 'Idle Min': 0.0
        }
    }

    # Session state initialization for the full 78 features
    if "inputs" not in st.session_state:
        st.session_state.inputs = {col: 0.0 for col in feature_columns}
        for feat in feature_columns:
            st.session_state[f"input_{feat}"] = 0.0

    # Callback when template changes
    def apply_template():
        t_name = st.session_state.template_select
        t_data = TEMPLATES[t_name]
        for col in feature_columns:
            val = float(t_data.get(col, 0.0))
            st.session_state.inputs[col] = val
            st.session_state[f"input_{col}"] = val

    # Template selector
    st.selectbox("Load Threat Template Profile:", list(TEMPLATES.keys()), key="template_select", on_change=apply_template)

    st.markdown("### Interactive Network Parameters (All 78 Features)")

    # Render all 78 features in a 4-column grid
    with st.container():
        cols = st.columns(4)
        for idx, feat in enumerate(feature_columns):
            col = cols[idx % 4]
            with col:
                key_name = f"input_{feat}"
                if key_name not in st.session_state:
                    st.session_state[key_name] = float(TEMPLATES[st.session_state.template_select].get(feat, 0.0))
                
                val = st.number_input(feat, key=key_name, format="%.4f")
                st.session_state.inputs[feat] = val

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Predict Threat Status", use_container_width=True, key="btn_live_predict"):
        ordered_sample = [st.session_state.inputs[col] for col in feature_columns]
        
        st.markdown("<br>", unsafe_allow_html=True)
        if all(v == 0.0 for v in ordered_sample):
            st.error("Error: Invalid network profile (all feature values are zero). Please select a template or enter valid parameters.")
        else:
            with st.spinner("Analyzing threat profile..."):
                df_sample = pd.DataFrame([ordered_sample], columns=feature_columns)
                prediction = model.predict(df_sample)
                result = encoder.inverse_transform(prediction)[0]
                
                if result == "BENIGN":
                    st.success(f"Normal Traffic Profile Detected ({result})")
                else:
                    st.error(f"Threat Detected: {result}")

# ==================== TAB 2: BATCH CSV TRAFFIC ANALYZER ====================
with tab_batch:
    st.markdown("### Upload CICIDS Capture File")
    st.markdown("Analyze bulk network captures for anomalous behavior using the same AI engine.")
    
    uploaded_file = st.file_uploader("Choose a CSV log file", type=["csv"], key="batch_file_uploader")

    if uploaded_file is not None:
        with st.spinner("Parsing packet sequence metrics..."):
            data = pd.read_csv(uploaded_file)
            data.columns = data.columns.str.strip()

            # Remove label if present
            if "Label" in data.columns:
                data = data.drop("Label", axis=1)

            # Preprocess
            data = data.replace([float("inf"), float("-inf")], 0)
            data = data.fillna(0)
            
            # Align features using the feature_columns list
            for col in feature_columns:
                if col not in data.columns:
                    data[col] = 0.0
            data = data[feature_columns]

            # Run predictions
            predictions = model.predict(data)
            decoded = encoder.inverse_transform(predictions)

            st.markdown("### Capture Traffic Breakdown Summary")
            summary_df = pd.Series(decoded).value_counts().reset_index()
            summary_df.columns = ["Traffic Type", "Count"]
            st.dataframe(summary_df, use_container_width=True)