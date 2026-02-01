import streamlit as st
from s3_utils import upload_file, list_files, download_file, delete_file

st.set_page_config(page_title="Cloud Storage System", layout='centered', page_icon="☁️")

st.write('Manage your files in AWS S3 with ease!')

st.header("Upload a file")
uploaded_file = st.file_uploader("Choose a file to upload")
if uploaded_file:
    upload_file(uploaded_file)
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

st.header("Files in Cloud Storage")
files = list_files()
if files:
    for i, file in enumerate(files):
        st.write(f"- {file}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download", key=f"download_{i}"):
                messg = download_file(file)
                st.success(messg)
        with col2:
            if st.button("Delete", key=f"delete_{i}"):
                delete_file(file)
                st.success(f"File '{file}' deleted successfully!")
else:
    st.info("No file found in cloud storage.")

