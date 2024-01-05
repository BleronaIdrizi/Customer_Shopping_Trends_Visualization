# hello.py
import pandas as pd
import streamlit as st
from modules.index import *

st.set_page_config(layout="wide")

dataset = pd.read_csv('../files/Preprocessed_Shopping_Trends_Dataset.csv')

tabForDataTypeViz_, tabStaticInteractivViz_, tabForStatistics, tabForAbout = st.tabs(["Tipet e të dhënave", "Static & Interactive", "Statistics", "About"])

with tabForDataTypeViz_:
    dataTypeVizualizationPage(dataset)

with tabStaticInteractivViz_:
    staticIntercativVizualizationPage(dataset)

with tabForAbout:
    getAboutPage()