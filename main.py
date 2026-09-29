import streamlit as st
from ollama import chat

st.title("My AI Bot: Synora")
name = "eesha"
st.write("Welcome,",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    # st.write("You asked: ",question)
    response=chat(model = "gemma3:1b",messages=[
        {
            "role":"system",
            "content":"you are a friendly tutor. you explain concepts in a very simple way.Explain in 30 words max"    
        },
        {
            "role":"user",
            "content":question
        }


    ])
    answer=response.message.content
    st.write(answer)

#dropdown
# options = ["c++","java","python"]
# choice = st.selectbox("select your favourite language: ",options)
# st.write(f"you selected : {choice}")