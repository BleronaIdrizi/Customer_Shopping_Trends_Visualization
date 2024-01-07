import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# Funksion për të krijuar grafikun pie në baze të filtrit të zgjedhur
def plot_pie_chart(data, title, col2):
    fig, ax = plt.subplots()
    data.value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')
    ax.set_title(title)
    col2.pyplot(fig)

def interactiveDisplay(df):
    fig = px.scatter(df, x='Review Rating', y='Purchase Amount (USD)', 
                 color='Category', # Color points by category
                 hover_data=['Item Purchased', 'Age', 'Gender']) # Additional info on hover
    st.title('Interactive Scatter Plot Example')

    # Filters or other interactive components
    category = st.selectbox('Select Category:', df['Category'].unique())

    # Filtering data based on selection
    filtered_data = df[df['Category'] == category]

    # Update the plot
    fig = px.scatter(filtered_data, x='Review Rating', y='Purchase Amount (USD)', 
                    color='Category', 
                    hover_data=['Item Purchased', 'Age', 'Gender'])

    st.plotly_chart(fig, use_container_width=True)

def staticDisplay(df):
    # Create two columns for filters and visualizations
    col1, col2 = st.columns([1, 3])

    # Initialize selected as None
    selected = None

    with col1:
        st.subheader("Filtrat:")
        # Use session state to store and reset the last selected filter
        if 'selected_filter' not in st.session_state:
            st.session_state['selected_filter'] = None

        # Define the filter selection
        filter_option = st.selectbox("Zgjidhni një filter:", df.columns)

        if filter_option:
            selected = st.selectbox("Zgjidh vlerën:", options=[""] + sorted(list(df[filter_option].unique())))

        filter_second_option = st.selectbox("Zgjidh filterin për krahasim:", options=[""] + sorted(list(df.columns.unique())))

        # Update session state
        if selected:
            st.session_state['selected_filter'] = (filter_option, selected, filter_second_option)
    
    # Check if a filter has been selected and plot the corresponding pie chart
    if st.session_state['selected_filter']:
        filter_option, selected, filter_second_option = st.session_state['selected_filter']
        st.write(filter_option, selected, filter_second_option)
        if filter_option and filter_second_option:  # Check if both options are non-empty and valid
            filtered_data = df[df[filter_option] == selected][filter_second_option]
            plot_title = f"Distribuimi i sezoneve për moshën: {selected}"
            plot_pie_chart(filtered_data, plot_title, col2)

def staticIntercativVizualizationPage(df):
    st.header("Vizualizimi statik dhe interaktiv")

    tabForStaticViz_, tabForInteractiveViz_ = st.tabs(["Static", "Interactive"])

    with tabForStaticViz_:
        staticDisplay(df)

    with tabForInteractiveViz_:
        interactiveDisplay(df) 