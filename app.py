import streamlit as st
from levels.soc_levels import soc_level_1, soc_level_2, soc_level_3
from levels.vm_levels import vm_level_1, vm_level_2, vm_level_3
from levels.helpers import init_state

st.set_page_config(page_title="CyberQuest ENTERPRISE", layout="wide")
st.title("🛡️ CyberQuest ENTERPRISE – Cyber Range")

init_state("soc_level", 1)
init_state("vm_level", 1)
init_state("soc_completed", False)
init_state("vm_completed", False)
init_state("mode", None)
init_state("score", 0)

if not st.session_state.mode:
    st.subheader("🎮 Select Learning Mode")
    col1, col2 = st.columns(2)
    if col1.button("🟢 Fresher Mode"):
        st.session_state.mode = "Fresher"
        st.rerun()
    if col2.button("🔴 Advanced Mode"):
        st.session_state.mode = "Advanced"
        st.rerun()
    st.stop()

mode = st.session_state.mode
role = st.sidebar.radio("Select Role", ["SOC Analyst", "VM Lead"])

st.metric("Score", st.session_state.score)

if role == "SOC Analyst":
    if st.session_state.soc_level == 1:
        soc_level_1(mode)
    elif st.session_state.soc_level == 2:
        soc_level_2(mode)
    elif st.session_state.soc_level == 3:
        soc_level_3(mode)

if role == "VM Lead":
    if not st.session_state.soc_completed:
        st.warning("🚫 Complete SOC story to unlock VM")
    else:
        if st.session_state.vm_level == 1:
            vm_level_1(mode)
        elif st.session_state.vm_level == 2:
            vm_level_2(mode)
        elif st.session_state.vm_level == 3:
            vm_level_3(mode)