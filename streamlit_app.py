import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv('final_clustered_milan_data.csv')

# فیلترها
st.sidebar.header('Filter Properties')
price_min, price_max = st.sidebar.slider('Price Range', int(df['price'].min()), int(df['price'].max()), (600000, 1200000))
area_min, area_max = st.sidebar.slider('Area Range (sqm)', int(df['area_sqm'].min()), int(df['area_sqm'].max()), (60, 140))
growth_options = st.sidebar.multiselect('Growth Cluster', df['growth_cluster'].unique(), default=list(df['growth_cluster'].unique()))

# فیلتر کردن
filtered_data = df[
    (df['price'] >= price_min) &
    (df['price'] <= price_max) &
    (df['area_sqm'] >= area_min) &
    (df['area_sqm'] <= area_max) &
    (df['growth_cluster'].isin(growth_options))
]

# نمایش
st.title('Filtered Properties')
st.dataframe(filtered_data)


# Load data
df = pd.read_csv("final_clustered_milan_data.csv")

# Title
st.title("🏙️ Investment Potential in Milan")
st.markdown("Analyze and explore real estate growth potential across Milan's districts.")

# Filter by growth label
growth_filter = st.selectbox("Select Growth Category:", ["All"] + df['growth_label'].unique().tolist())
if growth_filter != "All":
    df = df[df['growth_label'] == growth_filter]

# Show dataframe
st.write("Filtered Properties", df)

# Bar chart of growth label counts
st.subheader("Number of Properties by Growth Label")
st.bar_chart(df['growth_label'].value_counts())

# Download button
st.download_button("Download Filtered Data", df.to_csv(index=False), file_name="filtered_milan_data.csv")
