import streamlit as st
from text_to_speech import text_to_speech_streamlit
from speech_to_text import speech_to_text_streamlit
from text_to_text import text_to_text_gpt


def main():

    st.markdown("""
        <style>
        .reportview-container .main .block-container{
            padding-top: 0rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 0rem;
            max-width: 100%;
        }
        .reportview-container .sidebar .sidebar-content {
            padding-top: 1rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)

    st.sidebar.image("D:/2. GP/images/ColoredLogo.svg", use_column_width=True)
    st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
    languages = ['Arabic', 'English']
    st.sidebar.title("Select Language")
    language = st.sidebar.selectbox("Choose a language", languages)
    lang = language[:2].lower()

    st.title("Avatar")
    question = speech_to_text_streamlit(lang)

    while question is not None:
        st.write(question)

        answer = text_to_text_gpt(question)
        st.write(answer)

        text_to_speech_streamlit(answer, lang)
        break


if __name__ == "__main__":
    main()
