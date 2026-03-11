import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Food Analytics Dashboard", layout="wide")

st.title("🍽 Food  Orders Analytics Dashboard")

# Upload dataset
file = st.file_uploader("zomato_india_orders_2025_10k.xlsx", type=["xlsx"])

if file is not None:

    df = pd.read_excel(file)

    st.write("Total Orders:", len(df))

    # Sidebar filter
    st.sidebar.header("Filter")
    city = st.sidebar.selectbox("Select City", ["All"] + list(df["City"].unique()))

    if city != "All":
        df = df[df["City"] == city]

    # ---------------- ROW 1 ----------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Orders by City")
        fig, ax = plt.subplots()
        df["City"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("Popular Cuisines")
        fig, ax = plt.subplots()
        df["Cuisine"].value_counts().head(5).plot(kind="bar", ax=ax)
        st.pyplot(fig)

    # ---------------- ROW 2 ----------------

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Payment Methods")
        fig, ax = plt.subplots()
        df["Payment_Method"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

    with col4:
        st.subheader("Delivery Time Distribution")
        fig, ax = plt.subplots()
        ax.hist(df["Delivery_Time_Min"], bins=20)
        st.pyplot(fig)

else:
    st.info("Upload your dataset to view the dashboard.")