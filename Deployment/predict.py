import pandas as pd
import numpy as np
import streamlit as st

# Library Load Model
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Library Pre-Processing
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

#load model
model = load_model('model')
    
# Membuat fungsi cleaning
cleaning_pattern = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
lemmatizer = WordNetLemmatizer()
# Additional Stopwords
additional_stopwords = ['the', 'to', 'and', 'of', 'a', 'in', 'for', '#coronavirus', 'is', 'are', 'on', 'I', 'you', 'at', 'prices', 'with', 'have', 'this', 'that', 'be', 'grocery',
    'store', 'as', 'food', 'supermarket', 'from', 'people', 'your', 'will', 'it', 'all', 'The', 'COVID-19', 'we', 'not', 'has', '&', 'by', 'our', 'or', '19',
    'can', 'out', 'my', 'up', '#COVID19', 'their', 'more', 'they', 'during']

# Setting stopwords english
stpwds_eng = list(set(stopwords.words('english')))
for i in additional_stopwords:
    stpwds_eng.append(i)

# Membuat fungsi cleaning
cleaning_pattern = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
lemmatizer = WordNetLemmatizer()
stpwds_eng = list(set(stopwords.words('english')))

# build text cleaning function
def text_proses(text):

    # Mengubah text ke Lowercase
    text = text.lower()

    # Menghilangkan mention, link, dan karakter non-alfanumerik
    text = re.sub(cleaning_pattern, ' ', text)

    # Menghilangkan Mention
    text = re.sub("@[A-Za-z0-9_]+", " ", text)

    # Menghilangkan Hashtag
    text = re.sub("#[A-Za-z0-9_]+", " ", text)

    # Menghilangkan \n (newline)
    text = re.sub(r"\\n", " ",text)

    # Menghilangkan kata dibawah 3 character
    text = re.sub(r'\b\w{1,3}\b', " ",text)

    # URL removal
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www.\S+", " ", text)

    # Menghilangkan Whitespace di awal dan akhir
    text = text.strip()

    # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
    text = re.sub("[^A-Za-z\s']", " ", text)

    # Menghilangkan double space
    text = re.sub("\s\s+" , " ", text)

    # Melakukan Tokenisasi
    tokens = word_tokenize(text)

    # Menghilangkan Stopwords
    text = ' '.join([word for word in tokens if word not in stpwds_eng])

    # Melakukan Lemmatizer
    text = lemmatizer.lemmatize(text)

    return text

def run():
    # membuat title
    st.title('Amazon reviews')
    st.subheader('Tweets Sentiment Detection')
    st.markdown('---')
    # Buat form
    with st.form(key='tweet_sentiment_detect'):
        st.write("## Tweets")
        # URL input
        text = st.text_input("Enter Your tweets:")
        submitted = st.form_submit_button('Predict')
        # Perform prediction
        if submitted:
                data_inf = {'text': text}
                data_inf = pd.DataFrame([data_inf])
                # Preprocess the text (apply the same preprocessing steps as used during training)
                data_inf['text'] = data_inf['text'].apply(lambda x: text_proses(x))
                # Make the prediction using the loaded model
                y_pred_inf = model.predict(data_inf)
                y_pred_inf = np.argmax(y_pred_inf)

                # Display the prediction result
                if y_pred_inf == 0:
                    st.subheader("Prediction: Negative Tweet")
                elif y_pred_inf == 1:
                    st.subheader("Prediction: Neutral Tweet")
                else:
                    st.subheader("Prediction: Positive Tweet")

                # Display the extracted text
                st.subheader("Extracted Text:")
                st.write(text)

if __name__ == '__main__':
    run()