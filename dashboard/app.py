import sys
import os
import streamlit as st
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from orchestrator.agent_manager import AgentManager

st.set_page_config(page_title="AutoPilot AI", layout="wide")

st.title("🚀 AutoPilot AI")
st.caption("Agentic Supply Chain Decision Intelligence")

df = pd.read_csv("data/supply_chain_data.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")

manager = AgentManager()
results = manager.run_all(df)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Agent Insights")
    for k, v in results.items():
        if k not in ["recommendations", "pm_summary"]:
            st.write(f"**{k.upper()}**")
            st.write(v)

with col2:
    st.subheader("💡 Recommended Actions")
    for rec in results.get("recommendations", []):
        st.success(rec)

    st.subheader("🧑‍💼 PM Priority")
    for p in results.get("pm_summary", []):
        st.warning(p)
