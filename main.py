import requests, os
import send_email

topic = "tesla"
news_api_key = "3d1212fa93cc4f968e52953b4367abff"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-11-19&sortBy=publishedAt&apiKey={news_api_key}&language=en"


# Make request
response = requests.get(url)

# Get a dictionary with the data
content = response.json()

# Access article titles and description
body = "subject: Daily Tesla News \n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += f"Title: {article["title"]} \nDescription: {article["description"]} \nArticle URL: {article["url"]} \n\n"

body += "\n\nSourced from, \nNewsAPI"
body = body.encode("utf-8")
send_email.send_email(body)


