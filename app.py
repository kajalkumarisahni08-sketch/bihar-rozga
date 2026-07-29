import streamlit as st
import pandas as pd

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(
    page_title="बिहार रोजगार प्राइवेट लिमिटेड",
    page_icon="🏗️",
    layout="wide"
)

# 2. कस्टम CSS (मोबाइल व्यू और हरे रंग के टेक्स्ट/बटन के लिए)
st.markdown("""
    <style>
    /* वाटरमार्क और फुटर छुपाने के लिए */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* मुख्य शीर्षक स्टाइल */
    .main-title {
        background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 25px;
    }
    
    /* कारीगर और टेंडर के लिए खास हरा स्टाइल (मोबाइल में साफ दिखेगा) */
    .green-section-box {
        background-color: #2e7d32 !important;
        color: #ffffff !important;
        padding: 15px;
        border-radius: 10px;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    }
    
    /* हरे रंग के बटन की स्टाइल */
    div.stButton > button {
        background-color: #2e7d32 !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
        padding: 10px;
    }
    div.stButton > button:hover {
        background-color: #1b5e20 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. सेशन स्टेट (डेटा सुरक्षित रखने के लिए)
if "karigar_database" not in st.session_state:
    st.session_state.karigar_database = []

if "tender_database" not in st.session_state:
    st.session_state.tender_database = []

if "admin_password" not in st.session_state:
    st.session_state.admin_password = "96081"

# --- मुख्य हेडर ---
st.markdown("""
    <div class="main-title">
        <h1>🏢 बिहार रोजगार प्राइवेट लिमिटेड कंपनी</h1>
        <p>बिहार लेबर एवं मिस्त्री प्राइवेट पोर्टल - कामगार भाइयों के लिए आधिकारिक डिजिटल मंच</p>
    </div>
""", unsafe_allow_html=True)

# --- सेक्शन 1: हमारे मेहनतकश कामगार और मिस्त्री ---
st.markdown("## 🌟 हमारे कार्य दृश्य (सही कामगार तस्वीरें)")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. राज मिस्त्री (Raj Mistry)")
    st.image(
        "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b7?auto=format&fit=crop&w=800&q=80", 
        caption="कुशल राज मिस्त्री दीवार की चिनाई करते हुए", 
        use_container_width=True
    )
    st.write("घर निर्माण, दीवार चिनाई और प्लास्टर के विशेषज्ञ मिस्त्री।")

with col2:
    st.subheader("2. छत ढलैया का काम")
    st.image(
        "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=800&q=80", 
        caption="मजदूरों की टीम छत की ढलैया करते हुए", 
        use_container_width=True
    )
    st.write("छत ढलैया, कंक्रीट मिक्सिंग और वाइब्रेटर संचालन की पूरी टीम।")

with col3:
    st.subheader("3. लेबर / मजदूर")
    st.image(
        "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80", 
        caption="मेहनतकश निर्माण मजदूर काम करते हुए", 
        use_container_width=True
    )
    st.write("निर्माण कार्य, ईंट ढोने और साइट की सफाई के लिए मेहनती मजदूर।")

st.markdown("---")

# --- सेक्शन 2: कारीगर रजिस्ट्रेशन (हरा रंग - मोबाइल में साफ दिखेगा) ---
st.markdown('<div class="green-section-box">👷 1. लेबर / मिस्त्री / कारीगर रजिस्ट्रेशन फ़ॉर्म</div>', unsafe_allow_html=True)

with st.form("karigar_form"):
    k_name = st.text_input("आपका पूरा नाम:")
    k_phone = st.text_input("मोबाइल नंबर:")
    k_work_type = st.selectbox("आप क्या काम करते हैं?", ["राज मिस्त्री", "छत ढलैया मजदूर", "हेल्पर/लेबर", "सेंटरिंग मिस्त्री", "प्लंबर", "इलेक्ट्रीशियन", "पेंटर"])
    k_address = st.text_area("आपका जिला और पूरा पता:")
    
    submit_karigar = st.form_submit_button("रजिस्ट्रेशन जमा करें")
    
    if submit_karigar:
        if k_name != "" and k_phone != "":
            st.session_state.karigar_database.append({
                "नाम": k_name,
                "मोबाइल": k_phone,
                "काम": k_work_type,
                "पता": k_address
            })
            st.success("✅ आपका रजिस्ट्रेशन सफलतापूर्वक दर्ज हो गया है!")
        else:
            st.warning("⚠️ कृपया अपना नाम और मोबाइल नंबर ज़रूर भरें।")

st.markdown("---")

# --- सेक्शन 3: टेंडर / काम का ठेका पोस्ट करें (हरा रंग - मोबाइल में साफ दिखेगा) ---
st.markdown('<div class="green-section-box">📋 2. नया टेंडर / काम का ठेका पोस्ट करें</div>', unsafe_allow_html=True)

with st.form("tender_form"):
    t_title = st.text_input("काम का नाम (जैसे: 2 कमरा ढलैया, बाउंड्री दीवार आदि):")
    t_owner = st.text_input("ठेकेदार/मालिक का नाम:")
    t_phone = st.text_input("संपर्क नंबर:")
    t_location = st.text_input("काम का स्थान/जिला:")
    t_details = st.text_area("काम की पूरी जानकारी:")
    
    submit_tender = st.form_submit_button("टेंडर पोस्ट करें")
    
    if submit_tender:
        if t_title != "" and t_phone != "":
            st.session_state.tender_database.append({
                "काम": t_title,
                "मालिक": t_owner,
                "संपर्क": t_phone,
                "स्थान": t_location,
                "विवरण": t_details
            })
            st.success("🎉 नया टेंडर सफलतापूर्वक पोस्ट हो गया है!")
        else:
            st.warning("⚠️ कृपया काम का नाम और संपर्क नंबर भरें।")

st.markdown("---")

# --- सेक्शन 4: ओनर गुप्त लॉगिन (एडमिन पैनल) ---
st.sidebar.markdown("### 🔐 ओनर गुप्त लॉगिन")
admin_input = st.sidebar.text_input("गुप्त कोड दर्ज करें:", type="password")
login_btn = st.sidebar.button("अनलिमिटेड मेनू खोलें")

if admin_input == st.session_state.admin_password:
    st.sidebar.success("🔑 ओनर लॉगिन सफल!")
    
    st.markdown("## 📊 ओनर एडमिन डैशबोर्ड")
    
    tab1, tab2 = st.tabs(["रजिस्टर्ड कारीगर सूची", "पोस्ट किए गए टेंडर सूची"])
    
    with tab1:
        st.subheader("रजिस्टर्ड लेबर और मिस्त्री")
        if len(st.session_state.karigar_database) > 0:
            st.dataframe(pd.DataFrame(st.session_state.karigar_database), use_container_width=True)
        else:
            st.info("अभी तक कोई कारीगर पंजीकृत नहीं हुआ है।")
            
    with tab2:
        st.subheader("पोस्ट किए गए टेंडर")
        if len(st.session_state.tender_database) > 0:
            st.dataframe(pd.DataFrame(st.session_state.tender_database), use_container_width=True)
        else:
            st.info("अभी तक कोई टेंडर पोस्ट नहीं किया गया है।")

elif admin_input != "":
    st.sidebar.error("❌ गलत गुप्त कोड! (डिफ़ॉल्ट कोड 96081 है)")