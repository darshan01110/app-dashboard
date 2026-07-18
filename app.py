
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Smart Wearable AI Dashboard", layout="wide")
st.title("🩺 Smart Wearable AI Healthcare Dashboard")
st.caption("Demo dashboard - replace simulated values with Arduino serial data.")

c1,c2,c3,c4,c5=st.columns(5)
hr=np.random.randint(68,85)
spo2=np.random.randint(96,100)
temp=round(np.random.normal(36.8,0.2),1)
press=np.random.randint(1005,1018)
alt=np.random.randint(145,160)

c1.metric("❤️ Heart Rate",f"{hr} BPM")
c2.metric("🫁 SpO₂",f"{spo2}%")
c3.metric("🌡 Temperature",f"{temp} °C")
c4.metric("🩸 Pressure",f"{press} hPa")
c5.metric("⛰ Altitude",f"{alt} m")

left,right=st.columns([2,1])

with left:
    st.subheader("Live ECG")
    x=np.arange(300)
    y=np.sin(x/10)+np.random.normal(0,0.08,300)
    fig=go.Figure(go.Scatter(x=x,y=y,mode="lines"))
    fig.update_layout(height=300)
    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Sensor Trends")
    t=np.arange(60)
    f=go.Figure()
    f.add_trace(go.Scatter(x=t,y=70+5*np.sin(t/5),name="HR"))
    f.add_trace(go.Scatter(x=t,y=98+0.4*np.sin(t/7),name="SpO₂"))
    f.add_trace(go.Scatter(x=t,y=36.8+0.1*np.sin(t/4),name="Temp"))
    st.plotly_chart(f,use_container_width=True)

with right:
    st.subheader("🧠 AI")
    st.success("Prediction: Healthy")
    st.metric("Confidence","98.7%")
    st.info("Recommendation:\n- Continue monitoring\n- Replace demo data with Arduino")
    st.json({"Accelerometer":{"X":0.03,"Y":0.98,"Z":0.02},
             "Gyroscope":{"X":2.0,"Y":0.5,"Z":1.4}})

st.divider()
st.write("### System Status")
st.write(f"Last Update: {datetime.now().strftime('%H:%M:%S')}")
st.write("Arduino: Demo Mode")
