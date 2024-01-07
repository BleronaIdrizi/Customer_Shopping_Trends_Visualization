import streamlit as st

def getAboutPage():
    st.header("About")
    st.subheader("Përshkrimi i projektit")
    st.markdown("""
        Ky projekt është realizuar për kursin 'Përgatitja dhe vizualizimi i të dhënave' në kuadër të programit master në Universitetin e Prishtinës, departamenti i 
        Inxhinierisë Kompjuterike. Projekti synon digjitalizimin dhe vizualizimin interaktiv të të dhënave duke ofruar një pasqyrë të thellë mbi sjelljet dhe preferencat e blerjeve të konsumatorëve dhe duke ofruar një mjet të 
        avancuar analitik në ueb. Duke përdorur teknika të avancuara të parapërgatitjes dhe analizës së të dhënave, ne synojmë të paraqesim disa ide se si mund ti ndihmojmë bizneset të përshtaten në nevojat e klientëve të tyre. Projektimi, ekzekutimi dhe analiza e të dhënave janë bërë me qëllim të përmirësimit të strategjive të marketingut dhe ofertave të bizneseve, duke kontribuar drejt një përvoje më të personalizuar për konsumatorin.
    """)
    st.markdown("""
        Gjuha programuese kryesore e përdorur është Python, me një sërë librarish si Streamlit për ndërtimin e aplikacionit interaktiv, Pandas dhe Numpy për përpunimin e të dhënave, Plotly Express dhe Altair për vizualizime të të dhënave, si dhe libraritë re dhe hashlib për përpunimin e tekstit dhe sigurinë e të dhënave. Për përkthimin e përmbajtjes, është përdorur libraritë googletrans.
    """)
    st.markdown("""
        <ul style='line-height: 1;'>
            <li><a href="https://streamlit.io/" target="_blank">Streamlit</a></li>
            <li><a href="https://pandas.pydata.org/" target="_blank">Pandas</a></li>
            <li><a href="https://numpy.org/" target="_blank">NumPy</a></li>
            <li><a href="https://plotly.com/python/plotly-express/" target="_blank">Plotly Express</a></li>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown("Aplikacionet në të cilat jemi bazur janë:")
    st.markdown("""
        <ul style='line-height: 1;'>
            <li><a href="https://github.com/uran-lajci/Kosovas-Frequency-Plan-Analysis-and-Vizualization" target="_blank">Kosovas-Frequency-Plan-Analysis-and-Vizualization</a></li>
            <li><a href="https://realpython.com/python-data-visualization-bokeh/" target="_blank">Interactive Data Visualization in Python With Bokeh</a></li>
            <li><a href="https://www.kaggle.com/code/fathyfathysahlool/customer-shopping-trends" target="_blank">Customer Shopping Trends</a></li>
        </ul>
    """, unsafe_allow_html=True)

    st.subheader('Përshkrimi i datasetit')
    st.markdown("Dataseti që kemi përdorur në këtë projekt është Customer Shopping Trends Dataset. Ky dataset ofron njohuri të vlefshme për sjelljen e konsumatorëve dhe modelet e blerjeve. Kuptimi i preferencave dhe tendencave të klientëve është thelbësor për bizneset që të përshtatin produktet e tyre, strategjitë e marketingut dhe përvojën e përgjithshme të klientit. Ky grup të dhënash kap një gamë të gjerë të atributeve të klientit, duke përfshirë moshën, gjininë, historinë e blerjeve, mënyrat e preferuara të pagesës, shpeshtësinë e blerjeve dhe më shumë. Analizimi i këtyre të dhënave mund t'i ndihmojë bizneset të marrin vendime të informuara, të optimizojnë ofertat e produkteve dhe të rrisin kënaqësinë e klientit. Të dhënat e të dhënave qëndron si një burim i vlefshëm për bizneset që synojnë të harmonizojnë strategjitë e tyre me nevojat dhe preferencat e klientëve. Është e rëndësishme të theksohet se ky grup të dhënash është një grup i të dhënave sintetike i krijuar për fillestarët për të mësuar më shumë rreth analizës së të dhënave dhe mësimit të makinerisë.")
    st.subheader("Ky projekt është zhvilluar nga:")
    st.markdown("""
        <ul style='line-height: 1;'>
            <li>Blerona Idrizi(blerona.idrizi@student.uni-pr.edu)</li>
            <li>Vlora Gjoka(vlora.gjoka1@student.uni-pr.edu)</li>
        </ul>
    """, unsafe_allow_html=True)
