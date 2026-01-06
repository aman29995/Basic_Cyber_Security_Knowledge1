import streamlit as st
from .helpers import add_score

def vm_level_1(mode):
    st.subheader("🛡️ VM Level 1 – Emergency Patch")
    if st.button("🛠️ Deploy Patch", key="vm1"):
        add_score(20)
        st.session_state.vm_level += 1

def vm_level_2(mode):
    st.subheader("🛡️ VM Level 2 – Risk Mitigation")
    if st.button("⚖️ Temporary Mitigation", key="vm2"):
        add_score(20)
        st.session_state.vm_level += 1

def vm_level_3(mode):
    st.subheader("🛡️ VM Level 3 – Executive Closure")
    if st.button("📄 Submit Executive Report", key="vm3"):
        add_score(30)
        st.session_state.vm_completed = True
        st.balloons()