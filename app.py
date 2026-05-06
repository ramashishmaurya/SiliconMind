import streamlit as st
import os
from pdf_loader import load_pdf, split_pdf, create_vectorstore
from agent import load_vectorstore, create_agent, ask_question

# Page setup
st.set_page_config(
    page_title="ChipMind",
    page_icon="🔌",
    layout="wide"
)

st.title("ChipMind")
st.caption("Semiconductor Datasheet AI Agent — Powered by Llama3")

# ---- Sidebar ----
with st.sidebar:
    st.header("Datasheet Upload")

    uploaded_file = st.file_uploader(
        "PDF upload karo",
        type=['pdf']
    )

    if uploaded_file is not None:

        # PDF save karo folder mein
        os.makedirs("data/datasheets", exist_ok=True)
        pdf_path = f"data/datasheets/{uploaded_file.name}"

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"{uploaded_file.name} upload ho gayi!")

        # Process button
        if st.button("Process karo"):
            with st.spinner("PDF padh raha hoon..."):
                pages = load_pdf(pdf_path)

            with st.spinner("Chunks bana raha hoon..."):
                chunks = split_pdf(pages)

            with st.spinner("Database bana raha hoon... thoda time lagega"):
                create_vectorstore(chunks)

            st.success("Ready hai! Ab neeche sawaal poochho!")
            st.session_state['pdf_ready'] = True

    # Status dikhao
    if os.path.exists("faiss_index"):
        st.info("Database ready hai!")
    else:
        st.warning("Pehle PDF upload karo")

# ---- Main Area ----
st.header("Chip ke baare mein poochho")

# Quick question buttons
st.write("Quick sawaal:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Max voltage?"):
        st.session_state['q'] = "What is the maximum supply voltage for this chip?"

with col2:
    if st.button("Max temperature?"):
        st.session_state['q'] = "What is the maximum operating temperature?"

with col3:
    if st.button("Chip kya karta hai?"):
        st.session_state['q'] = "What does this chip do? Explain in simple words."

# Text input
question = st.text_input(
    "Ya apna sawaal likho:",
    value=st.session_state.get('q', '')
)

# Answer button
if st.button("Poochho!"):

    # Check: sawaal hai?
    if not question:
        st.error("Pehle kuch poochho!")

    # Check: database ready hai?
    elif not os.path.exists("faiss_index"):
        st.error("Pehle PDF upload aur process karo!")

    else:
        with st.spinner("Llama3 soch raha hai..."):
            vectorstore = load_vectorstore()
            agent = create_agent(vectorstore)
            answer = ask_question(agent, question)

        # Answer dikhao
        st.success("Jawab:")
        st.write(answer)