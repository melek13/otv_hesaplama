import streamlit as st

fiyat=st.number_input("Vergisiz Fiyat Giriniz")
motorhacmi=st.number_input("Motor Hacmini CC olarak giriniz")
kdv=1.18

if motorhacmi<1600:
    if fiyat<184_000:
        otv=1.45
    elif fiyat<220_000:
        otv=1.50
    elif fiyat<250_000:
        otv=1.60
    elif fiyat<280_000:
        otv=1.70
    else:
        otv=1.80
elif motorhacmi<2000:
    if fiyat<170_000:
        otv=2.30
    else:
        otv=2.50
else:
    otv=3.20

herseydahil=fiyat*otv*kdv

st.write("KDV ÖTV Dahil Tavsiye EdilenSatış Fiyatı",herseydahil)
