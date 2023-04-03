import streamlit as st

st.title("Gelir Vergisi Ödeme")

kazanc=st.number_input("Kazanç Giriniz")

v32=32000*0.15
v70=(70000-32000)*0.20
v170=(170000-70000)*0.27
v880=(880000-170000)*0.35

if kazanc<32_000:
    vergi=0.15*kazanc
elif kazanc<70_000:
    vergi=v32+((kazanc-32000)*0.20)
elif kazanc<170_000:
    vergi=v32+v70+((kazanc-70000)*0.27)
elif kazanc<880_000:
    vergi=v32+v70+v170+((kazanc-170000)*0.35)
else:
    vergi=v32+v70+v170+v880+((kazanc-880000)*0.40)

st.write(vergi)

st.title("Yavrum Nerdesin Kim Bilir Kimlerlesin")

