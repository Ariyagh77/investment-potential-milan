
import streamlit as st
import pandas as pd

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
