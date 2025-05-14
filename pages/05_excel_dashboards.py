import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Set up Streamlit UI
st.title("AI-Powered Excel Dashboard Generator 📊")

# File Upload
uploaded_file = st.file_uploader("Upload a preprocessed Excel file", type=["xls", "xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("### Preview of the Data:")
    st.dataframe(df.head())

    # User selects columns for analysis
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if not numeric_cols:
        st.error("No numeric columns found for visualization!")
        st.stop()

    x_axis = st.selectbox("Select X-axis variable:", numeric_cols)
    y_axis = st.selectbox("Select Y-axis variable:", numeric_cols)
    chart_type = st.multiselect("Select Chart Types:", ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot", "Box Plot", "Histogram", "Heatmap", "Area Chart", "Density Plot"])
    color_palette = st.selectbox("Select Color Palette:", ['coolwarm', 'viridis', 'plasma', 'magma', 'cividis'])

    # Generate Dashboard
    if st.button("Generate Dashboard"):
        st.write("### Data Visualizations:")

        num_charts = len(chart_type)

        if num_charts == 0:
            st.warning("Please select at least one chart type.")
            st.stop()

        # Determine grid layout
        cols = 2
        rows = (num_charts // cols) + (num_charts % cols > 0)

        fig, axes = plt.subplots(rows, cols, figsize=(12, 5 * rows))
        axes = axes.flatten()[:num_charts]  # Ensure only required subplots are used

        plot_index = 0

        for chart in chart_type:
            ax = axes[plot_index]

            if chart == "Bar Chart":
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax, palette=color_palette)
                ax.set_title("Bar Chart")
            elif chart == "Line Chart":
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax, color="b")
                ax.set_title("Line Chart")
            elif chart == "Pie Chart":
                df[x_axis].value_counts().plot.pie(autopct="%.1f%%", ax=ax, colors=sns.color_palette(color_palette))
                ax.set_title("Pie Chart")
            elif chart == "Scatter Plot":
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax, color="r")
                ax.set_title("Scatter Plot")
            elif chart == "Box Plot":
                sns.boxplot(x=df[x_axis], y=df[y_axis], ax=ax, palette=color_palette)
                ax.set_title("Box Plot")
            elif chart == "Histogram":
                sns.histplot(df[x_axis], bins=20, kde=True, ax=ax, color="g")
                ax.set_title("Histogram")
            elif chart == "Heatmap" and len(numeric_cols) > 1:
                sns.heatmap(df[numeric_cols].corr(), annot=True, cmap=color_palette, ax=ax)
                ax.set_title("Heatmap")
            elif chart == "Area Chart":
                df.plot.area(x=x_axis, y=y_axis, ax=ax, colormap=color_palette)
                ax.set_title("Area Chart")
            elif chart == "Density Plot":
                sns.kdeplot(df[x_axis], ax=ax, fill=True, color="purple")
                ax.set_title("Density Plot")

            plot_index += 1

        plt.tight_layout()
        st.pyplot(fig)

        # Download Option
        buffer = BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        st.download_button("Download Dashboard", buffer, file_name="dashboard.png", mime="image/png")
