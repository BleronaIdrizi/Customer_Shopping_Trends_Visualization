import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

colors = sns.color_palette('pastel')  # Mund të përdorni paleta të tjera të ngjyrave

def plot_age_distribution(df):
    # Create age groups
    bins = [0, 18, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # Plot pie chart for age groups
    age_group_counts = df['AgeGroup'].value_counts().sort_index()
    fig, ax = plt.subplots()
    age_group_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')
    ax.set_title('Shpërndarja e Grupmoshave')
    st.pyplot(fig)

def plot_pie_chart(df, column, title):
    counts = df[column].value_counts()
    
    # Create an 'explode' list with a slight offset for each category
    explode = [0.1 if i == 0 else 0 for i in range(len(counts))]  # Only the first slice is exploded

    plt.figure(figsize=(20, 6))
    counts.plot(kind='pie', fontsize=12, colors=colors[:len(counts)], explode=explode, autopct='%1.1f%%')
    plt.title(title)
    plt.xlabel(column, weight="bold", color="#2F0F5D", fontsize=14, labelpad=20)
    plt.ylabel('Counts', weight="bold", color="#2F0F5D", fontsize=14, labelpad=20)
    plt.legend(labels=counts.index, loc="best")
    st.pyplot(plt)  # Use Streamlit's function to show the plot

def plot_horizontal_bar_chart(df, column, title):
    plt.figure(figsize=(16, 6))
    top_colors = df[column].value_counts()[:10].sort_values(ascending=True)
    top_colors.plot(kind='barh', color=sns.color_palette('tab20', n_colors=len(top_colors)), edgecolor='black')
    plt.xlabel('\n Counts', weight="bold", color="#D71313", fontsize=14, labelpad=20)
    plt.ylabel('\n' + column, weight="bold", color="#D71313", fontsize=14, labelpad=20)
    plt.xticks(rotation=0, ha='center', fontsize=16)
    plt.title(title)
    plt.tight_layout()
    st.pyplot(plt)

def plot_bar_chart(df, column, title):
    # Merrni vlerat unike dhe numrin e tyre
    counts = df[column].value_counts()

    # Plot bar chart
    plt.figure(figsize=(20, 10))
    barplot = sns.barplot(x=counts.index, y=counts.values, palette=colors[:len(counts)])
    barplot.set_title(title)

    # Shtoni anotimet në çdo shtyllë
    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.0f'), 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha='center', va='center', 
                         xytext=(0, 10), 
                         textcoords='offset points')

    # Vendosni etiketat e boshtit x dhe y
    plt.xlabel(column, weight="bold", color="#D71313", fontsize=14, labelpad=20)
    plt.ylabel('Counts', weight="bold", color="#D71313", fontsize=14, labelpad=20)
    plt.xticks(rotation=45)  # Rrotulloni etiketat nëse janë të gjata ose shumë
    st.pyplot(plt)


def dataTypeVizualizationPage(df):
    st.header("Vizualizimi sipas tipeve të dhënave")
    if 'selected_column' not in st.session_state:
        st.session_state['selected_column'] = None

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Opsionet e Vizualizimit:")
        viz_option = st.radio("Zgjidhni stilin e vizualizimit:", ['Pie Charts', 'Columns', 'Horizontal Bar'])

        st.subheader("Kolonat:")
        for column in df.columns:
            # If the button for the column is clicked, or if it's the currently selected column, mark it
            if st.button(f"Shfaq {column}", key=column):
                st.session_state['selected_column'] = column
            if st.session_state['selected_column'] == column:
                st.write(f"Kolona e zgjedhur: {column}")

    with col2:
        if 'selected_column' in st.session_state and st.session_state['selected_column'] is not None:
            # Based on the last clicked button, display the appropriate chart
            if viz_option == 'Columns':
                plot_bar_chart(df, st.session_state.selected_column, f"Shpërndarja e {st.session_state.selected_column}")
            elif viz_option == 'Horizontal Bar':
                plot_horizontal_bar_chart(df, st.session_state.selected_column, f"Shpërndarja e {st.session_state.selected_column}")
            else:
                if st.session_state.selected_column == 'Age':
                    plot_age_distribution(df)
                else:
                    plot_pie_chart(df, st.session_state.selected_column, f"Shpërndarja e {st.session_state.selected_column}")
        
