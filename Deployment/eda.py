# Streamlit
import streamlit as st

# Pandas
import pandas as pd

# Visualisasi
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud

def run():
    # Membuat judul
    st.title('Amazon Sentiment')

    # Membuat sub judul
    st.subheader('Deep Learning')

    st.divider()

    # Menambah Gambar dari url
    st.image('https://www.ciobulletin.com/assets/home_image/ciobulletin-amazon-gains-ecommerce-market.jpg')

    # Membuat caption
    st.caption("Source: Twitter")

    st.divider()

    # Buat deskripsi
    st.title('Problem Statement')
    st.write('''
        Im Data scientist and i want information about case problem in company amazon to understand customer satisfaction levels and the impact of comments on products on the Amazon website, analyzing review data using Natural Language Processing (NLP) is crucial. By applying NLP techniques, we can analyze customer reviews to measure satisfaction levels based on the sentiment contained in the review text, as well as evaluate how positive and negative comments affect product perception. This technique allows us to identify the sentiment patterns underlying customer feedback, understand the factors that contribute to satisfaction or dissatisfaction, and measure the impact of review sentiment on product reputation and success in the marketplace.    ''')

    st.divider()

    st.title('Objective')
    st.write('''
                evaluate customers' satisfaction levels by identifying whether their reviews are positive, negative, or neutral. In addition, we wanted to understand how comments, both positive and negative, affect the view and judgment of the product in the `NLP` process.
            ''')

    st.divider()

    # Menampilkan dataframe
    st.title('Data')
    df= pd.read_csv('Amazon_review.csv',  encoding='latin-1')
    st.dataframe(df)
    st.write('''Data ini diambil dari Kaggle ''')

    st.divider()

    # Visualisasi
    st.title('Exploratory Data Analysis')

    # Menampilkan chart

    # Menghitung top 10 lokasi berdasarkan jumlah
    st.subheader('Distribution of Sentiments')
    top_locations = df['Location'].value_counts().head(10)
    # Create Plotly bar chart
    fig = px.bar(x=top_locations.values, y=top_locations.index, orientation='h',
             labels={'x': 'Count', 'y': 'Location'},
             color=top_locations.values, color_continuous_scale='viridis')
    st.plotly_chart(fig)
    st.write('''Bar chart diatas menunjukan bahwa lokasi yang paling sering melakukan tweet tentang covid adalah London.''')
    
    st.divider()

    # Plotting the distribution of classes
    st.subheader('Distribution of Sentiments')
    # Menggunakan Plotly Express untuk plotting
    fig = px.histogram(df, x='Sentiment', color='Sentiment')
    st.plotly_chart(fig)
    st.write('''Informasi dari bar chart diatas bahwa tweet terbanyak tentang covid19 adalah tweet positive dan tweet yang paling sedikit adalah tweet extreamly negative.''')

    st.divider()

    
    # Select negative tweets
    negative_tweets = df[df["sentiment"] == "negatif"]

    # Plotly figure for negative tweets
    st.subheader('Kata paling populer Negative Tweets')
    fig_negative = px.bar(
    top_negative_locations,
    x=top_negative.values,
    y=top_negative.index,
    orientation='h',,
    color_continuous_scale='viridis'
    )
    st.plotly_chart(fig_negative)
    st.write('''Card terbanyak yang melakukan tweet negative, positve, dan neutral.''')

    st.divider()

    # Menggabungkan semua teks pada kolom OriginalTweet dengan spasi
    allWords = ' '.join([tweet for tweet in df["reviewText"]])
    # Membuat WordCloud
    wordCloud = WordCloud(width=500, height=300, random_state=2023).generate(allWords)
    # Aplikasi Streamlit
    st.subheader('WordCloud Example')
    # Menampilkan WordCloud menggunakan Plotly Express (px)
    fig = px.imshow(wordCloud)
    st.plotly_chart(fig)
    st.write('''Informasi menunjukkan kata yang paling dominan card.''')

    st.divider()

    # Aggregate text by sentiment
    negative_text = ' '.join(df[df.Sentiment == 'Negative'].OriginalTweet.tolist())
    neutral_text = ' '.join(df[df.Sentiment == 'Neutral'].OriginalTweet.tolist())
    positive_text = ' '.join(df[df.Sentiment == 'Positive'].OriginalTweet.tolist())

    # Generate WordCloud objects
    negative_wordcloud = WordCloud().generate(negative_text)
    neutral_wordcloud = WordCloud().generate(neutral_text)
    positive_wordcloud = WordCloud().generate(positive_text)
    # Display using Plotly and Plotly Express in Streamlit
    st.subheader('Word Clouds by Sentiment')

    # Negative Word Cloud with Plotly
    st.write('#### Negative Sentiment Word Cloud')
    fig_neg = px.imshow(negative_wordcloud)
    st.plotly_chart(fig_neg)
    st.write('''Negative sentiment''')

    # Neutral Word Cloud with Plotly
    st.write('#### Neutral Sentiment Word Cloud')
    fig_neu = px.imshow(neutral_wordcloud)
    st.plotly_chart(fig_neu)
    st.write('''Neutral sentiment.''')

    # Positive Word Cloud with Plotly
    st.write('#### Sentiment Word Cloud')
    fig_pos = px.imshow(positive_wordcloud)
    st.plotly_chart(fig_pos)
    st.write('''Positve sentiment.''')

if __name__ == '__main__':
    run()
