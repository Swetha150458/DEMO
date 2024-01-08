import streamlit as sṭ
st.set_page_config(page_title="Flowers")
st.header("types of flowers")

col1,col2=st.column(2)
with col1:
  st.subheader("Daisy")
  st.image("C:\Users\NIHARIKA\Desktop\daisy.jpg",caption="Daisy flower",width=300,use_column_width=True)
  st.write("Daisy flowers sre beautiful")
with col2:
  st.subheader("Lily")
  st.image("C:\Users\NIHARIKA\Desktop\lily.jpg",caption="lily flower",width=300,use_column_width=True)
  st.write("lily flowers sre awsome")
