import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import dodge

# Function to create a pie chart based on the selected filter
def plot_pie_chart(data, title, col2):
    fig, ax = plt.subplots()
    data.value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')
    ax.set_title(title)
    col2.pyplot(fig)

# Function to display an interactive scatter plot using Plotly
def interactiveDisplay(df):
    fig = px.scatter(df, x='Review Rating', y='Purchase Amount (USD)', 
                     color='Category', # Color points by category
                     hover_data=['Item Purchased', 'Age', 'Gender']) # Additional info on hover

    category = st.selectbox('Zgjidh kategorinë:', df['Category'].unique())
    filtered_data = df[df['Category'] == category]
    fig = px.scatter(filtered_data, x='Review Rating', y='Purchase Amount (USD)', 
                     color='Category', hover_data=['Item Purchased', 'Age', 'Gender'])

    st.plotly_chart(fig, use_container_width=True)

# Function to create and display a Bokeh chart
def create_bokeh_chart(df):
    if df.empty or 'Category' not in df.columns or 'Purchase Amount (USD)' not in df.columns:
        st.write("Data not available or missing required columns for Bokeh plot.")
        return

    grouped_data = df.groupby('Category')['Purchase Amount (USD)'].mean().reset_index()
    source = ColumnDataSource(grouped_data)

    p = figure(x_range=grouped_data['Category'], width=800, height=400, 
               title="Mesatarja e shumës së blerjes sipas kategorisë",
               x_axis_label='Kategoria', y_axis_label='Mesatarja e shumës së blerjes (USD)')

    p.vbar(x=dodge('Category', -0.25, range=p.x_range), top='Purchase Amount (USD)', 
           width=0.2, source=source, color="skyblue")

    hover = HoverTool()
    hover.tooltips = [("Kategoria", "@Category"), ("Mesatarja e shumës", "@{Purchase Amount (USD)}")]
    p.add_tools(hover)

    st.bokeh_chart(p, use_container_width=True)

# Function to display static visualizations
def staticDisplay(df):
    col1, col2 = st.columns([1, 3])
    selected = None

    with col1:
        st.subheader("Filtrat:")
        if 'selected_filter' not in st.session_state:
            st.session_state['selected_filter'] = None

        filter_option = st.selectbox("Zgjidhni një filter:", df.columns)
        if filter_option:
            selected = st.selectbox("Zgjidh vlerën:", options=[""] + sorted(list(df[filter_option].unique())))
        filter_second_option = st.selectbox("Zgjidh filterin për krahasim:", options=[""] + sorted(list(df.columns.unique())))

        if selected:
            st.session_state['selected_filter'] = (filter_option, selected, filter_second_option)
    
    if st.session_state['selected_filter']:
        filter_option, selected, filter_second_option = st.session_state['selected_filter']
        if filter_option and filter_second_option:
            filtered_data = df[df[filter_option] == selected][filter_second_option]
            plot_title = f"Distribuimi i {filter_second_option} për {filter_option}: {selected}"
            plot_pie_chart(filtered_data, plot_title, col2)

# Main function to handle page layout and visualization
def staticIntercativVizualizationPage(df):
    st.header("Vizualizimi statik dhe interaktiv")
    tabForStaticViz_, tabForInteractiveViz_ = st.tabs(["Static", "Interactive"])

    with tabForStaticViz_:
        staticDisplay(df)

    with tabForInteractiveViz_:
        interactiveDisplay(df)
        create_bokeh_chart(df)

