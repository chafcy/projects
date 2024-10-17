import html
import requests
import streamlit as st

# API key
API_KEY = "4b45c33cf806444da350b1f0a32561b2"
# Keyword
KEYWORD = "apple"
# API URL
API_URL = f"https://newsapi.org/v2/everything?q={KEYWORD}&from=2024-04-29&to=2024-04-29&sortBy=popularity&apiKey={API_KEY}"

# Function to fetch news articles
def _get_news():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        st.error("Failed to fetch news articles.")
        return []

# Main function for the news page
def news_page():
    # Fetch news articles
    news_articles = _get_news()

    # Display each news article
    for article in news_articles:
        st.markdown(f"<h2>{html.unescape(article['title'])}</h2>", unsafe_allow_html=True)
        if article.get("urlToImage"):
            st.image(article["urlToImage"])
        st.markdown(f"<h5>{article['description']}</h5>", unsafe_allow_html=True)
        st.markdown(f"Link: [{article['url'][:80]}...]({article['url']})")
        st.markdown(f"Author: {article.get('author', 'Unknown')}, Published at: {article['publishedAt'][:10]}")
        st.markdown("---")

# Calling the news page function
if __name__ == "__main__":
    news_page()