import streamlit as st
import pandas as pd

# पेज सेटअप
st.set_page_config(page_title="Bihar Rozgar Private Limited", page_icon="👷‍♂️", layout="wide")

# CSS स्टाइलिंग: रंग, बॉर्डर और बड़ा टेक्स्ट सेट करने के लिए
st.markdown("""
    <style>
    .main {
        background-color: #F8FAFC;
    }
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* ऊपर का शानदार बैनर */
    .govt-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #047857 100%);
        padding: 30px 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    .govt-header h1 {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: bold;
        margin: 0;
    }
    .govt-header p {
        color: #E2E8F0 !important;
        font-size: 18px;
        margin-top: 10px;
        font-weight: 600;
    }
    
    /* पोर्टल मेनू की मुख्य हेडिंग को बहुत बड़ा और हरा करना */
    .menu-main-title {
        color: #047857 !important;
        font-size: 26px !important;
        font-weight: 900 !important;
        margin-bottom: 15px;
    }

    /* रेडियो बटन्स (मेनू विकल्प) को बड़े, बोल्ड और पीले-हरे रंग में दिखाना ताकि दूर से दिखे */
    .stRadio > div {
        background-color: #0F172A;
        padding: 15px;
        border-radius: 12px;
        border: 3px solid #047857;
    }
    .stRadio label {
        color: #FACC15 !important;
        font-size: 22px !important;
        font-weight: 900 !important;
        padding: 8px 18px;
    }
    
    /* सभी फॉर्म्स और सेक्शन की हेडिंग्स को बड़ा और हरा करना */
    h2, h3, .stSubheader {
        color: #047857 !important;
        font-weight: 900 !important;
        font-size: 24px !important;
        border-bottom: 3px solid #047857;
        padding-bottom: 5px;
    }
    
    /* फॉर्म के सभी इनपुट बॉक्स और टेक्स्ट पर चारों तरफ साफ़ हरा बॉर्डर */
    input, textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 2px solid #047857 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }
    
    /* सेलेक्ट बॉक्स (Dropdown) का बॉर्डर और रंग */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #047857 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }
    
    /* सभी लेबल्स को गहरा और साफ़ करना */
    label, .stMarkdown p {
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ऊपर ऑफिशियल बैनर (बिहार रोजगार प्राइवेट लिमिटेड कंपनी)
st.markdown("""
    <div class="govt-header">
        <div style="font-size: 45px; margin-bottom: 8px;">🏢 👷‍♂️ 🧱 🪚 ⚡</div>
        <h1>बिहार रोजगार प्राइवेट लिमिटेड कंपनी</h1>
        <p>बिहार लेबर एवं मिस्त्री प्राइवेट पोर्टल - कामगार भाइयों के लिए आधिकारिक डिजिटल मंच</p>
    </div>
""", unsafe_allow_html=True)

# --- कामगारों की तस्वीरें जोड़ी गई हैं ---
st.markdown("### 🌟 हमारे मेहनतकश कामगार और मिस्त्री भाई (कार्यरत दृश्य):")
col_img1, col_img2, col_img3, col_img4, col_img5 = st.columns(5)

with col_img1:
    st.image("https://images.unsplash.com/photo-1541888946425-d0fbb18f1f4d?w=400&q=80", caption="घर की ढलैया / निर्माण कार्य", use_container_width=True)
with col_img2:
    st.image("https://images.unsplash.com/photo-1590381105924-c72589b9ef3f?w=400&q=80", caption="राजमिस्त्री ईंट जोड़ते हुए", use_container_width=True)
with col_img3:
    st.image("https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=400&q=80", caption="वेल्डर वेल्डिंग करते हुए", use_container_width=True)
with col_img4:
    st.image("https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=400&q=80", caption="कारपेंटर लकड़ी का काम", use_container_width=True)
with col_img5:
    st.image("https://images.unsplash.com/photo-1578874691223-64558a3ca096?w=400&q=80", caption="लेबर सामान/बोरी ढोते हुए", use_container_width=True)

st.markdown("---")

if "labor_database" not in st.session_state:
    st.session_state.labor_database = []

if "tender_database" not in st.session_state:
    st.session_state.tender_database = []

if "admin_password" not in st.session_state:
    st.session_state.admin_password = "1234"

# यहाँ मास्टर सीक्रेट कोड सेट किया गया है (आप इसे बाद में बदल भी सकते हैं)
if "master_secret_code" not in st.session_state:
    st.session_state.master_secret_code = "varun99"  # यह आपका गुप्त कोड है जिसे डालने पर ही एडमिन मेनू दिखेगा

if "show_admin_menus" not in st.session_state:
    st.session_state.show_admin_menus = False

# साइडबार में सीक्रेट कोड डालने का बॉक्स (आम आदमियों को यह नहीं दिखेगा या वे यहाँ तक नहीं पहुँचेंगे)
with st.sidebar:
    st.markdown("### 🔐 ओनर गुप्त लॉगिन")
    secret_input = st.text_input("मास्टर सीक्रेट कोड दर्ज करें:", type="password")
    if st.button("अनलिमिटेड मेनू खोलें"):
        if secret_input == st.session_state.master_secret_code:
            st.session_state.show_admin_menus = True
            st.success("✅ गुप्त मेनू अनलॉक हो गए हैं!")
            st.rerun()
        else:
            st.error("❌ गलत गुप्त कोड!")
            
    if st.session_state.show_admin_menus:
        if st.button("🔒 एडमिन मेनू छुपाएं (Lock Again)"):
            st.session_state.show_admin_menus = False
            st.rerun()

# पोर्टल मेनू की लिस्ट तैयार करना (अगर गुप्त कोड डाला गया होगा तभी एडमिन और पासवर्ड वाले विकल्प दिखेंगे)
menu_options = [
    "📝 1. लेबर मिस्त्री रजिस्ट्रेशन", 
    "📋 2. ठेकेदार टेंडर पोस्ट"
]

if st.session_state.show_admin_menus:
    menu_options.append("🔒 3. एडमिन डैशबोर्ड")
    menu_options.append("🔑 4. पासवर्ड रिसेट")

# पोर्टल मेनू की हेडिंग को बड़े साइज़ और हरे रंग में दिखाना
st.markdown('<p class="menu-main-title">📌 पोर्टल का मुख्य मेनू (यहाँ क्लिक करें):</p>', unsafe_allow_html=True)

# मेनू विकल्प दिखाना
menu = st.radio("", menu_options, horizontal=True, label_visibility="collapsed")

st.markdown("---")

# 1. लेबर / मिस्त्री रजिस्ट्रेशन फॉर्म
if menu == "📝 1. लेबर मिस्त्री रजिस्ट्रेशन":
    st.markdown("## 📝 लेबर मिस्त्री रजिस्ट्रेशन फॉर्म")
    st.info("💡 यहाँ लेबर अपनी सही जानकारी, सेल्फी और आधार कार्ड (JPG, PNG या PDF) अपलोड करेंगे।")
    
    with st.form("complete_labor_form"):
        st.markdown("### 👤 व्यक्तिगत जानकारी (Personal Details)")
        
        name = st.text_input("1. पूरा नाम (Full Name):")
        father_name = st.text_input("2. पिता का नाम (Father's Name):")
        gender = st.selectbox("3. लिंग (Gender):", ["पुरुष (Male)", "महिला (Female)", "अन्य"])
        phone = st.text_input("4. मोबाइल नंबर (Mobile Number):")
        age = st.number_input("5. उम्र (Age):", min_value=18, max_value=70, value=25)
            
        st.markdown("### 🏠 पूरा पता (Address Details)")
        state = st.text_input("6. राज्य (State):", value="बिहार")
        district = st.selectbox("7. जिला (District):", [
            "बिहार शरीफ (Nalanda)", "पटना", "गया", "मुजफ्फरपुर", "भागलपुर", 
            "पूर्णिया", "दरभंगा", "बेगूसराय", "सीतामढ़ी", "मधुबनी", "अन्य"
        ])
        block_anchal = st.text_input("8. ब्लॉक / अंचल (Block / Anchal):")
        panchayat = st.text_input("9. पंचायत (Panchayat):")
        village = st.text_input("10. ग्राम / मोहल्ला (Village / Locality):")
        pincode = st.text_input("11. पिन कोड (PIN Code):")

        st.markdown("### 🛠️ हुनर और मिस्त्री का प्रकार (Skills)")
        skill_category = st.selectbox("12. स्त्री / मिस्त्री का प्रकार (Skill Category):", [
            "राजमिस्त्री (Mason)", 
            "कारपेंटर (Carpenter)", 
            "वेल्डर / बिल्डर (Welder / Builder)", 
            "सेंटिंग मिस्त्री (Centering Master)", 
            "इलेक्ट्रीशियन (Electrician)", 
            "पेंटर (Painter)", 
            "प्लंबर (Plumber)", 
            "बेलदार / सादा लेबर (General Helper)", 
            "टाईल्स मिस्त्री (Tiles Master)",
            "अन्य कारीगर"
        ])
        experience_years = st.text_input("13. कितने साल का अनुभव है? (जैसे: 5 साल):")

        st.markdown("### 📸 फोटो और दस्तावेज अपलोड (JPG, PNG और PDF)")
        selfie_photo = st.file_uploader("अपनी स्पष्ट सेल्फी फोटो अपलोड करें (JPG/PNG):", type=["jpg", "png", "jpeg"])
        aadhaar_photo = st.file_uploader("आधार कार्ड का फोटो या पीडीएफ अपलोड करें (JPG, PNG, PDF):", type=["jpg", "png", "jpeg", "pdf"])

        submit_registration = st.form_submit_button("रजिस्टर करें (Submit Details)")

        if submit_registration:
            if name and phone and village and district:
                full_address = f"राज्य: {state}, जिला: {district}, ब्लॉक/अंचल: {block_anchal}, पंचायत: {panchayat}, ग्राम: {village}, पिन: {pincode}"
                worker_id = f"BL-{len(st.session_state.labor_database) + 1001}"
                
                labor_record = {
                    "लेबर आईडी": worker_id,
                    "नाम": name,
                    "पिता का नाम": father_name,
                    "लिंग": gender,
                    "मोबाइल": phone,
                    "उम्र": age,
                    "पता": full_address,
                    "हुनर/प्रकार": skill_category,
                    "अनुभव": experience_years,
                    "सेल्फी_फाइल": selfie_photo,
                    "आधार_फाइल": aadhaar_photo,
                    "स्थिति": "घर पर उपलब्ध (Free)"
                }
                st.session_state.labor_database.append(labor_record)
                st.success(f"🎉 बधाई हो {name}! आपका रजिस्ट्रेशन हो गया है। आपकी आईडी है: *{worker_id}*")
            else:
                st.warning("कृपया नाम, मोबाइल नंबर, ग्राम और जिला ज़रूर भरें।")

# 2. ठेकेदार / काम देने वाले का टेंडर और काम पोस्ट करने का फॉर्म
elif menu == "📋 2. ठेकेदार टेंडर पोस्ट":
    st.markdown("## 📋 ठेकेदार टेंडर पोस्ट फॉर्म")
    
    if "temp_requirements" not in st.session_state:
        st.session_state.temp_requirements = []

    hirer_name = st.text_input("ठेकेदार या कंपनी का नाम:", key="h_name")
    hirer_phone = st.text_input("मोबाइल नंबर:", key="h_phone")
    work_title = st.text_input("काम का विवरण (जैसे: मकान निर्माण, दरवाजा खिड़की फिटिंग, ढलाई):", key="w_title")
    work_location = st.text_input("काम की सटीक लोकेशन (पता और जिला):", key="w_loc")

    st.markdown("---")
    st.markdown("### ➕ अपनी आवश्यकता के अनुसार मिस्त्री या लेबर जोड़ें (Add to List)")
    
    with st.form("add_requirement_form"):
        col_type, col_count = st.columns(2)
        with col_type:
            selected_category = st.selectbox("मिस्त्री या लेबर का प्रकार चुनें:", [
                "राजमिस्त्री (Mason)",
                "कारपेंटर (Carpenter)",
                "वेल्डर / बिल्डर (Welder / Builder)",
                "सेंटिंग मिस्त्री (Centering Master)",
                "इलेक्ट्रीशियन (Electrician)",
                "पेंटर (Painter)",
                "प्लंबर (Plumber)",
                "बिल्डिंग मिस्त्री का हेल्पर",
                "कारपेंटर का हेल्पर",
                "घर/सामान्य काम वाला हेल्पर",
                "महिला लेबर / स्त्री"
            ])
        with col_count:
            req_count = st.number_input("कितनी संख्या चाहिए?", min_value=1, value=1)
            
        add_btn = st.form_submit_button("सूची में जोड़ें (Add Item)")
        if add_btn:
            st.session_state.temp_requirements.append({"प्रकार": selected_category, "संख्या": req_count})
            st.success(f"{req_count} '{selected_category}' सूची में जोड़ दिया गया है!")

    if st.session_state.temp_requirements:
        st.markdown("#### 📋 चुनी गई लिस्ट (आपके द्वारा जोड़े गए मिस्त्री और लेबर):")
        df_temp = pd.DataFrame(st.session_state.temp_requirements)
        st.dataframe(df_temp, use_container_width=True)
        
        if st.button("🗑️ पूरी लिस्ट साफ़ करें (Reset List)"):
            st.session_state.temp_requirements = []
            st.rerun()

    st.markdown("---")
    
    with st.form("final_tender_form"):
        daily_wages = st.text_input("दैनिक मजदूरी राशि (रुपये प्रतिदिन प्रति लेबर):")
        food_arrangement = st.selectbox("खाने की सुविधा:", [
            "हाँ, एक टाइम का खाना फ्री दिया जाएगा", 
            "नहीं (केवल नकद मजदूरी)"
        ])
        
        st.info("📜 *कंपनी का नियम (एग्रीमेंट):\n1. टेंडर लेने वाले को कम से कम **10 दिन* तक लेबर से काम कराना होगा。\n2. काम शुरू होने से पहले *20% एडवांस राशि* जमा करनी होगी।")
        agree_terms = st.checkbox("मैं 10 दिन के काम और 20% एडवांस भुगतान के नियम से सहमत हूँ।")
        
        publish_tender = st.form_submit_button("🚀 फाइनल टेंडर / काम पब्लिश करें")
        
        if publish_tender:
            if hirer_name and work_location and daily_wages and st.session_state.temp_requirements:
                if agree_terms:
                    tender_id = f"TND-{len(st.session_state.tender_database) + 501}"
                    summary_text = ", ".join([f"{item['प्रकार']}: {item['संख्या']}" for item in st.session_state.temp_requirements])
                    
                    tender_record = {
                        "टेंडर आईडी": tender_id,
                        "ठेकेदार/कंपनी": hirer_name,
                        "मोबाइल": hirer_phone,
                        "काम": work_title,
                        "लोकेशन": work_location,
                        "आवश्यकता सूची": summary_text,
                        "मजदूरी": daily_wages,
                        "खाना": food_arrangement,
                        "शर्ते": "10 दिन काम + 20% एडवांस अनिवार्य"
                    }
                    st.session_state.tender_database.append(tender_record)
                    st.session_state.temp_requirements = []
                    st.success(f"🎉 टेंडर सफलतापर्वक जारी कर दिया गया है! टेंडर आईडी: *{tender_id}*")
                else:
                    st.warning("⚠️ कृपया 10 दिन और 20% एडवांस वाले एग्रीमेंट बॉक्स पर टिक (Select) करें।")
            else:
                st.warning("कृपया नाम, लोकेशन, मजदूरी राशि और कम से कम एक मिस्त्री/लेबर सूची में ज़रूर जोड़ें।")

# 3. एडमिन डैशबोर्ड (यह तभी दिखेगा जब गुप्त कोड डाला जाएगा)
elif menu == "🔒 3. एडमिन डैशबोर्ड":
    st.markdown("## 🔒 एडमिन डैशबोर्ड")
    
    admin_password = st.text_input("गुप्त एडमिन पासवर्ड दर्ज करें (Enter Admin Password):", type="password", key="admin_pass_box")
    
    if admin_password == st.session_state.admin_password:
        st.success("🔓 पासवर्ड सही है! अब आप सभी लेबरों के बड़े साइज़ में फोटो, आधार कार्ड और एक्टिव टेंडर देख सकते हैं:")
        
        sub_tab1, sub_tab2 = st.tabs(["👷‍♂️ रजिस्टर्ड लेबर (बड़ा फोटो और आधार देखें)", "📄 एक्टिव टेंडर सूची"])
        
        with sub_tab1:
            if st.session_state.labor_database:
                st.write(f"कुल रजिस्टर्ड लेबर: {len(st.session_state.labor_database)}")
                
                for idx, labor in enumerate(st.session_state.labor_database):
                    with st.expander(f"📌 आईडी: {labor['लेबर आईडी']} | नाम: {labor['नाम']} | हुनर: {labor['हुनर/प्रकार']}"):
                        col_info, col_img1 = st.columns([1.5, 2])
                        
                        with col_info:
                            st.markdown(f"*पिता का नाम:* {labor['पिता का नाम']}")
                            st.markdown(f"*मोबाइल नंबर:* {labor['मोबाइल']}")
                            st.markdown(f"*लिंग / उम्र:* {labor['लिंग']} / {labor['उम्र']} वर्ष")
                            st.markdown(f"*पूरा पता:* {labor['पता']}")
                            st.markdown(f"*अनुभव:* {labor['अनुभव']}")
                            st.markdown(f"*स्थिति:* {labor['स्थिति']}")
                            
                        with col_img1:
                            c1, c2 = st.columns(2)
                            with c1:
                                st.markdown("#### 📸 सेल्फी फोटो")
                                if labor["सेल्फी_फाइल"] is not None:
                                    st.image(labor["सेल्फी_फाइल"], caption="सेल्फी", width=220)
                                else:
                                    st.info("सेल्फी नहीं है")
                            with c2:
                                st.markdown("#### 🆔 आधार कार्ड / डॉक्यूमेंट")
                                if labor["आधार_फाइल"] is not None:
                                    if labor["आधार_फाइल"].type in ["image/jpeg", "image/png", "image/jpg"]:
                                        st.image(labor["आधार_फाइल"], caption="आधार (साफ़ देखें)", width=280)
                                    else:
                                        st.write("📄 पीडीएफ फाइल अपलोड की गई है।")
                                        st.download_button(
                                            label="डाउनलोड / देखें पीडीएफ",
                                            data=labor["आधार_फाइल"],
                                            file_name=f"Aadhaar_{labor['लेबर आईडी']}.pdf",
                                            mime="application/pdf",
                                            key=f"dl_{idx}"
                                        )
                                else:
                                    st.info("आधार कार्ड नहीं है")
                    st.markdown("---")
            else:
                st.info("अभी तक कोई लेबर रजिस्टर्ड नहीं है।")
                
        with sub_tab2:
            if st.session_state.tender_database:
                st.dataframe(pd.DataFrame(st.session_state.tender_database), use_container_width=True)
            else:
                st.info("अभी तक कोई टेंडर पोस्ट नहीं किया गया है।")
                
    elif admin_password == "":
        st.warning("🔒 कृपया अंदर की गोपनीय जानकारी देखने के लिए एडमिन पासवर्ड दर्ज करें। (डिफ़ॉल्ट पासवर्ड: *1234* है)")
    else:
        st.error("❌ गलत पासवर्ड! यह डेटा पूरी तरह सुरक्षित है।")

# 4. पासवर्ड रिसेट करने का विकल्प (यह भी तभी दिखेगा जब गुप्त कोड डाला जाएगा)
elif menu == "🔑 4. पासवर्ड रिसेट":
    st.markdown("## 🔑 पासवर्ड रिसेट")
    
    with st.form("reset_form"):
        old_pass = st.text_input("पुराना पासवर्ड दर्ज करें:", type="password")
        new_pass = st.text_input("नया पासवर्ड दर्ज करें:", type="password")
        confirm_pass = st.text_input("नया पासवर्ड दोबारा दर्ज करें:", type="password")
        
        reset_btn = st.form_submit_button("पासवर्ड बदलें")
        
        if reset_btn:
            if old_pass == st.session_state.admin_password:
                if new_pass and new_pass == confirm_pass:
                    st.session_state.admin_password = new_pass
                    st.success("🎉 एडमिन पासवर्ड सफलतापूर्वक बदल दिया गया है! अब नए पासवर्ड का उपयोग करें।")
                else:
                    st.warning("⚠️ नया पासवर्ड खाली नहीं होना चाहिए और दोनों नए पासवर्ड मेल खाने चाहिए।")
            else:
                st.error("❌ पुराना पासवर्ड गलत है!")st.markdown(
"## 👷 बिहार के मेहनतकश कामगार")

workers = [
    {
        "title": "🌾 खेत में काम करने वाले मजदूर",
        "image": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=800&q=80",
        "desc": "खेती, बुवाई और कटाई का कार्य"
    },
    {
        "title": "🏠 घर निर्माण मजदूर",
        "image": "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b7?auto=format&fit=crop&w=800&q=80",
        "desc": "घर बनाने और निर्माण कार्य"
    },
    {
        "title": "🪚 बढ़ई (Carpenter)",
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=800&q=80",
        "desc": "लकड़ी का फर्नीचर और दरवाजा बनाने का काम"
    },
    {
        "title": "⚡ वेल्डर (Welder)",
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=800&q=80",
        "desc": "लोहे की वेल्डिंग और फैब्रिकेशन"
    },
    {
        "title": "🪣 बालू ढोने वाले मजदूर",
        "image": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=800&q=80",
        "desc": "बालू, ईंट और सीमेंट ढुलाई"
    },
]

cols = st.columns(2)

for i, worker in enumerate(workers):
    with cols[i % 2]:
        st.subheader(worker["title"])
        st.image(worker["image"], use_container_width=True)
        st.write(worker["desc"])