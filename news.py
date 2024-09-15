import requests
import json

def fetch_news(category):
    with open("cred.json") as f:
        config = json.load(f)
    
    NEWS_KEY = config["NEWS_API"]
    
    # Check if category is provided
    if not category:
        print("No category provided")
        return
    
    url = f'https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=in&token={NEWS_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()

        # Check if articles are available
        if news_data.get('articles'):
            articles = news_data['articles']
            for article in articles:
                title = article.get('title')
                description = article.get('description')
                source = article.get('source', {}).get('name')
                
                # Print title, description, and source
                print(f"Title: {title}")
                return title
                print(f"Description: {description}")
                print(f"Source: {source}")
                print("-" * 50)  # Separator for each article
        else:
            print("No articles found for this category.")
    else:
        print(f"Error {response.status_code}: {response.text}")
