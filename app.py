import streamlit as st
import pickle

# Load the pre-trained sentiment analysis model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Movie Sentiment Dashboard",
    page_icon=":clapper:",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .title {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        background-color: #000;
        color: #fff;
        padding: 10px 0;
    }
    .predict-button {
        background-color: #ff7043;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
    }
    .result-box {
        background-color: #e0e0e0;
        padding: 20px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header and navigation menu
with st.container():
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; padding: 10px 20px; background-color: white; border-bottom: 1px solid #e0e0e0;">
            <div style="font-weight: bold; font-size: 18px;color:black">🎬 Movie Sentiment Dashboard</div>
           
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main content
st.markdown('<div class="title">Movie Sentiment Analysis</div>', unsafe_allow_html=True)
st.write("")

# Input text area
review_text = st.text_area("Type or paste movie review here. We will predict the sentiment analysis positive or negative", height=150)

submit =  st.button("Predict", key="predict_button", help="Click to predict sentiment")

if submit:
    # Prediksi menggunakan model
    prediction = model.predict([review_text])

    # Determine the color based on sentiment
    sentiment_color = "green" if prediction[0].lower() == "positive" else "red"

    # Menampilkan hasil berdasarkan prediksi
    if prediction[0] == 'positive':
        st.success('Positive Review')
        # Menampilkan GIF gembira
        st.image('https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmZtMnlobWNkMm81ZWhoNHNmeHprYzdlZnk0eTEwNWJpNmN1YmYwNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TdfyKrN7HGTIY/giphy.webp', caption='Happy GIF', use_column_width=True)
    else:
        st.warning('Negative Review')
        # Menampilkan GIF kecewa
        st.image('https://media4.giphy.com/media/lKXEBR8m1jWso/200.webp?cid=ecf05e4786h9m41o8h2qx9m4czbw36yvyly4p61xq7lz8t3n&ep=v1_gifs_search&rid=200.webp&ct=g', caption='Sad GIF', use_column_width=True)
else:
    st.write("")

# Footer
st.markdown(
    """
    <div class="footer">
        © 2024 Movie Sentiment Analysis | Development By Group 4
    </div>
    """,
    unsafe_allow_html=True,
)
