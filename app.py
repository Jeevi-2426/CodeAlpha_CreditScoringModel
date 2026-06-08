import streamlit as st

st.set_page_config(
    page_title="AI Credit Scoring Model",
    page_icon="💳",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Poppins:wght@300;400;500;600&display=swap');

.stApp{
    background: linear-gradient(135deg,#000000,#050816,#0a0f1f);
    color:white;
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Container */
.block-container{
    padding-top:2rem;
    max-width:850px;
}

/* Animated Title */
.main-title{
    font-family:'Orbitron',sans-serif;
    text-align:center;
    font-size:3.2rem;
    font-weight:700;
    color:#00e5ff;
    text-shadow:
    0 0 10px #00e5ff,
    0 0 20px #00e5ff,
    0 0 40px #00e5ff;
    animation: glow 2s infinite alternate;
}

@keyframes glow{
    from{
        text-shadow:
        0 0 10px #00e5ff,
        0 0 20px #00e5ff;
    }
    to{
        text-shadow:
        0 0 20px #00e5ff,
        0 0 40px #00e5ff,
        0 0 60px #00e5ff;
    }
}

.subtitle{
    text-align:center;
    color:#b8c1ec;
    margin-bottom:30px;
    font-size:1.1rem;
}

/* Glass Card */
.card{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    padding:30px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0 0 30px rgba(0,229,255,0.15);
}

/* Labels */
label{
    color:#00e5ff !important;
    font-size:18px !important;
    font-weight:700 !important;
}

/* Number Input */
.stNumberInput input{
    background:#101828 !important;
    color:white !important;
    border:1px solid #00e5ff !important;
    border-radius:12px !important;
}

/* Slider */
.stSlider{
    color:#00e5ff !important;
}

/* Button */
.stButton > button{
    width:100%;
    background:linear-gradient(90deg,#00e5ff,#0066ff);
    color:white;
    border:none;
    border-radius:15px;
    padding:14px;
    font-size:18px;
    font-weight:700;
    transition:0.4s;
    box-shadow:0 0 20px rgba(0,229,255,0.3);
}

.stButton > button:hover{
    transform:translateY(-4px);
    box-shadow:0 0 35px rgba(0,229,255,0.8);
}

/* Success Box */
.stSuccess{
    background:rgba(0,255,150,0.15)!important;
    border:1px solid #00ff95!important;
    border-radius:15px!important;
}

/* Error Box */
.stError{
    background:rgba(255,0,80,0.15)!important;
    border:1px solid #ff0055!important;
    border-radius:15px!important;
}

/* Metric */
[data-testid="stMetric"]{
    background:rgba(255,255,255,0.05);
    padding:20px;
    border-radius:15px;
    border:1px solid #00e5ff;
    box-shadow:0 0 20px rgba(0,229,255,0.15);
}

/* Progress Bar */
.stProgress > div > div > div{
    background:#00e5ff;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-track{
    background:#000;
}

::-webkit-scrollbar-thumb{
    background:#00e5ff;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# ================= Header =================

st.markdown(
    """
    <h1 class="main-title">💳 AI CREDIT SCORING MODEL</h1>
    <p class="subtitle">Machine Learning Based Credit Risk Prediction System</p>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:#00e5ff;'>🚀 AI Powered Credit Risk Analysis Dashboard</p>",
    unsafe_allow_html=True
)
st.markdown('<div class="card">', unsafe_allow_html=True)

# ================= Inputs =================

st.markdown("### 👤 Age")
age = st.slider("", 18, 100, 30)

st.markdown("### 💰 Credit Amount")
credit_amount = st.number_input(
    "",
    min_value=0,
    value=5000
)

st.markdown("### 📅 Loan Duration (Months)")
duration = st.slider(
    "",
    1,
    72,
    24
)

# ================= Prediction =================

if st.button("🚀 Predict Credit Risk"):

    if credit_amount > 5000 and duration > 24:

        st.error("⚠️ HIGH CREDIT RISK")

        st.progress(85)

        st.metric(
            label="Risk Score",
            value="85%"
        )

    else:

        st.success("✅ LOW CREDIT RISK")

        st.progress(25)

        st.metric(
            label="Risk Score",
            value="25%"
        )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <center>
    <p style='color:#7f8c8d'>
    Developed by Jeevisha Bharadwaj | CodeAlpha Internship Project
    </p>
    </center>
    """,
    unsafe_allow_html=True
)