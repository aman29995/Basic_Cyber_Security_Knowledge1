import streamlit as st
from .helpers import add_score

def vm_level_1(mode):
    st.subheader("🛡️ VM Level 1 – Vulnerability Scan Results")

    scan_results = [
        {"Asset": "Web-Server-01", "CVE": "CVE-2023-23397", "CVSS": 9.8, "Status": "Unpatched"},
        {"Asset": "DB-Server-02", "CVE": "CVE-2022-41040", "CVSS": 7.5, "Status": "Unpatched"}
    ]

    st.table(scan_results)

    if mode == "Fresher":
        st.info("💡 Always prioritize the highest CVSS score first.")

    if st.button("🛠️ Deploy Emergency Patch", key="vm1"):
        st.success("Critical vulnerability patched successfully.")

        st.code("""
Patch applied to Web-Server-01
Service restarted
Verification scan passed
        """)

        add_score(20)
        st.session_state.vm_level += 1

def vm_level_2(mode):
    st.subheader("🛡️ VM Level 2 – Risk Mitigation")
    if st.button("⚖️ Temporary Mitigation", key="vm2"):
        add_score(20)
        st.session_state.vm_level += 1

def vm_level_3(mode):
    st.subheader("🛡️ VM Level 3 – Executive Report")

    report = {
        "Total Assets": 25,
        "Critical Vulns Fixed": 5,
        "High Vulns Fixed": 8,
        "Risk Reduction": "72%",
        "SLA Compliance": "Yes"
    }

    st.table(report)

    if st.button("📄 Submit Executive Report", key="vm3"):
        st.success("Report submitted to leadership.")
        add_score(30)
        st.session_state.vm_completed = True
        st.balloons()
