import json
import requests
from bs4 import BeautifulSoup
from datetime import date


# Sends whatsapp message to the number mentioned.
def sendMessage(result):
    WHATSAPP_NUMBER_ID = ''  # Your whatsapp number ID
    TEMP_TOKEN = ''  # Your Temp token.
    SEND_MESSAGE_ENDPOINT = 'https://graph.facebook.com/v13.0/%s/messages'.format(WHATSAPP_NUMBER_ID)
    # data = {}
    data = {
        "messaging_product": "whatsapp",
        "to": "",  # Recipient Number
        "type": "template",
        "template": {
            "name": "top_news",
            "language": {
                "code": "en_US"
            },
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "TEXT",
                            "text": str(date.today())
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "TEXT",
                            "text": result
                        }
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": "Bearer " + TEMP_TOKEN,
        "Content-Type": "application/json"
    }
    print("Sending Message...")
    response = requests.post(
        url=SEND_MESSAGE_ENDPOINT,
        data=json.dumps(data),
        headers=headers
    )
    if response.status_code == 200:
        print("Message Sent..")
    else:
        print("Response: ", response)
        print("Response body", response.content)
        print("Response Status:", response.status_code)
        print("Failed to sent message..")


# Extracts top news from Times of India webpage
def extract_news():
    URL_TOI = 'https://timesofindia.indiatimes.com/news'
    response = requests.get(URL_TOI)
    soup = BeautifulSoup(response.content, 'html5lib')

    articles = soup.findAll(class_="w_tle")
    result = ''
    i = 1
    for article in articles:
        if i <= 10:
            result += "(" + str(i) + ") " + article.a['title']
        i += 1
    return result


def main():
    result = extract_news()
    sendMessage(result)


main()
