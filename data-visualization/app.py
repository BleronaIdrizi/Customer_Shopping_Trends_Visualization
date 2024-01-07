# hello.py
import pandas as pd
from modules.index import *

st.set_page_config(layout="wide")

dataset = pd.read_csv('../files/Preprocessed_Shopping_Trends_Dataset.csv')

# Custom CSS to inject for styling the tabs
custom_css = """
    <style>
        /* Style the tab bar */
        .stTabs {
            justify-content: center; /* Center tabs */
        }
        /* Style each tab */
        .st-bb {
            flex-grow: 1; /* Each tab takes equal space */
            justify-content: center; /* Center text in each tab */
        }
    </style>
"""

# Inject custom CSS with markdown
st.markdown(custom_css, unsafe_allow_html=True)

tabForDataTypeViz_, tabStaticInteractivViz_, tabForMultiDimensinalViz_, tabForAbout = st.tabs(["Vizualizimi sipas tipeve të dhënave", "Vizualizimi statik dhe interaktiv", "Vizualizimi i të dhënave shumë dimensionale", "About"])

with tabForDataTypeViz_:
    dataTypeVizualizationPage(dataset)

with tabStaticInteractivViz_:
    staticIntercativVizualizationPage(dataset)

with tabForMultiDimensinalViz_:
    multidimensionalVizualizationPage(dataset)

with tabForAbout:
    getAboutPage()