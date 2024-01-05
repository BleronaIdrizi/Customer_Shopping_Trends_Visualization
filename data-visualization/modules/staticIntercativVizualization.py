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
    col1, col2 = st.columns([1, 2])

    # Initialize selected as None
    selected = None

    with col1:
        st.subheader("Filtrat:")
        # Use session state to store and reset the last selected filter
        if 'selected_filter' not in st.session_state:
            st.session_state['selected_filter'] = None

        # Define the filter selection
        filter_option = st.selectbox("Zgjidhni një filter:", ["", "Mosha", "Kategoria", "Mënyra e pagesës"])

        if filter_option == "Mosha":
            selected = st.selectbox("Zgjidh moshën:", options=[""] + sorted(list(df['Age'].unique())))
        elif filter_option == "Kategoria":
            selected = st.selectbox("Zgjidh kategorinë:", options=[""] + sorted(list(df['Category'].unique())))
        elif filter_option == "Mënyra e Pagesës":
            selected = st.selectbox("Zgjidh mënyrën e pagesës:", options=[""] + sorted(list(df['Payment Method'].unique())))

        # Update session state
        if selected:
            st.session_state['selected_filter'] = (filter_option, selected)

    # Check if a filter has been selected and plot the corresponding pie chart
    if st.session_state['selected_filter']:
        filter_option, selected = st.session_state['selected_filter']

        if filter_option == "Mosha":
            filtered_data = df[df['Age'] == selected]['Season']
            plot_title = f"Distribuimi i sezoneve për moshën: {selected}"
        elif filter_option == "Kategoria":
            filtered_data = df[df['Category'] == selected]['Season']
            plot_title = f"Distribuimi i sezoneve për kategorinë: {selected}"
        elif filter_option == "Mënyra e Pagesës":
            filtered_data = df[df['Payment Method'] == selected]['Season']
            plot_title = f"Distribuimi i sezoneve për mënyrën e pagesës: {selected}"

        plot_pie_chart(filtered_data, plot_title, col2)