import streamlit as st
import plotly.express as px
import pandas as pd

# Ky funksion krijon grafikë të ndryshme në varësi të zgjedhjes së përdoruesit
def create_multidimensional_plot(df, x_axis, y_axis, z_axis, color_dimension, plot_type):
    # Krijon grafikë shpërndarjeje
    if plot_type == 'Scatter Plot':
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_dimension if color_dimension != 'None' else None)
    # Krijon grafikë shiriti
    elif plot_type == 'Bar Chart':
        fig = px.bar(df, x=x_axis, y=y_axis, color=color_dimension if color_dimension != 'None' else None)
    # Krijon grafikë vijore
    elif plot_type == 'Line Chart':
        fig = px.line(df, x=x_axis, y=y_axis, color=color_dimension if color_dimension != 'None' else None)
    # Krijon grafikë shpërndarjeje 3D
    elif plot_type == '3D Scatter Plot':
        fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis, color=color_dimension if color_dimension != 'None' else None)
    else:
        st.error("Lloji i zgjedhur i grafikut është i pavlefshëm")
        return None
    return fig

# Ky funksion krijon një Heatmap bazuar në dy kolona të zgjedhura
def create_heatmap(df, col1, col2):
    # Kontrollon nëse janë zgjedhur dy kolona të ndryshme
    if col1 and col2 and col1 != col2:
        crosstab = pd.crosstab(df[col1], df[col2])
        fig = px.imshow(crosstab, text_auto=True, aspect='auto', 
                        labels=dict(x=col2, y=col1, color='Count'), 
                        title=f'Harta e Nxehtësisë për {col1} vs {col2}')
        return fig
    else:
        st.warning("Ju lutem zgjidhni dy kolona të ndryshme për Heatmap.")
        return None

# Ky është funksioni kryesor i aplikacionit Streamlit
def multidimensionalVizualizationPage(df):
    st.title('Vizualizimi i të dhënave shumëdimensionale')
    
    # Zgjedhje të përdoruesit për vizualizimin
    x_axis = st.selectbox('Zgjidh boshtin X', options=df.columns)
    y_axis = st.selectbox('Zgjidh boshtin Y', options=df.columns)
    z_axis = st.selectbox('Zgjidh boshtin Z për grafikun 3D', options=['None'] + list(df.columns))
    color_dimension = st.selectbox('Zgjidh dimensionin e ngjyrës', options=['None'] + list(df.columns))
    plot_type = st.selectbox('Zgjidh llojin e grafikut', ['Scatter Plot', 'Bar Chart', 'Line Chart', '3D Scatter Plot'])

    # Krijimi dhe shfaqja e grafikut
    if plot_type != '3D Scatter Plot' or z_axis != 'None':
        fig = create_multidimensional_plot(df, x_axis, y_axis, z_axis, color_dimension, plot_type)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.error('Ju lutem zgjidhni një bosht Z për grafikun 3D Scatter.')

    # Menu për zgjedhjen e kolonave për hartën e nxehtësisë
    col1 = st.selectbox('Zgjidh kolonën e parë', options=[''] + list(df.columns))
    col2 = st.selectbox('Zgjidh kolonën e dytë', options=[''] + list(df.columns))

    # Krijimi dhe shfaqja e hartës së nxehtësisë
    fig = create_heatmap(df, col1, col2)
    if fig:
        st.plotly_chart(fig, use_container_width=True)
