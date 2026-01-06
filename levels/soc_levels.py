import streamlit as st
from .helpers import add_score, sla_timer, mitre_hint

def soc_level_1(mode):
    st.subheader("🚨 SOC Level 1 – Phishing Detection")

    st.write("📧 Employees reported suspicious emails.")

    email_data = {
        "From": "hr-support@micr0soft-secure.com",
        "To": "employee@company.com",
        "Subject": "Urgent Password Reset",
        "Attachment": "invoice.html",
        "IP": "185.203.119.45"
    }

    st.table(email_data)

    if mode == "Fresher":
        st.info("💡 Look for fake domains, urgency, and suspicious attachments.")

    if st.button("🔍 Analyze Email", key="soc1"):
        st.success("Phishing indicators detected!")

        indicators = [
            {"Indicator": "Domain Spoofing", "Value": "micr0soft-secure.com"},
            {"Indicator": "Malicious IP", "Value": "185.203.119.45"},
            {"Indicator": "HTML Attachment", "Value": "invoice.html"}
        ]

        st.table(indicators)

        add_score(10)
        st.session_state.soc_level += 1
def soc_level_2(mode):
    st.subheader("🚨 SOC Level 2 – Containment")
    if st.button("🔒 Reset Credentials", key="soc2"):
        add_score(20)
        st.session_state.soc_level += 1

def soc_level_3(mode):
    st.subheader("🚨 SOC Level 3 – Root Cause & Handover")
    if st.button("📤 Hand-off to VM Team", key="soc3"):
        add_score(30)
        st.session_state.soc_completed = True
        st.session_state.soc_level += 1
