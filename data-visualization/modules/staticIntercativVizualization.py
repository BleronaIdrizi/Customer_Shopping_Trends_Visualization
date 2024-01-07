import streamlit as st
import matplotlib.pyplot as plt

# Funksion për të krijuar grafikun pie në baze të filtrit të zgjedhur
def plot_pie_chart(data, title, col2):
    fig, ax = plt.subplots()
    data.value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')
    ax.set_title(title)
    col2.pyplot(fig)

def staticIntercativVizualizationPage(df):
    st.header("Vizualizimi statik dhe interaktiv")

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
        if filter_option:
            filtered_data = df[df[filter_option] == selected][filter_second_option]
            plot_title = f"Distribuimi i sezoneve për moshën: {selected}"

            plot_pie_chart(filtered_data, plot_title, col2)