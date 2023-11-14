import feedparser
import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/1165012803871060050/NfwQ1ccQRcgUwIYVy-QG2zXZen2jd5fjnwFgRZudiNnqWUWLGvVDLAGZV-ei5PRUH3zy'

def main():
	print("Connecting to RSS Feed...")
	
	message, url = get_rss_feed_info('')

	print("Data collected. Sending to server...")

	post_message(message, url)

def get_rss_feed_info(website):

	url = f'http://dailyillini.com//rss'
	headers = {"User-Agent": "ICSSP RSS Checker v1.0"}
	
	feed = feedparser.parse(url)
	print(feed["entries"][0])

	for item_data in feed['entries']:
#
		# item_data = item["data"]
#
#		# We will collect only the fields we are interested in.
		title = item_data["title"]
		permalink = item_data["link"]
		author = item_data["author"]
		image_url = item_data['media_content'][0]["url"]
#
#		# Compose a Markdown message using string formatting.
		message = f"[{title}]({permalink})\nby **{author}**"
#
		return (message, image_url)
	
def post_message(message, image_url):
    """Sends the formatted message to a Discord server.
    
    Parameters
    ----------
    message : str
        The formatted message to post.

    image_url : str
        The URL used as the thumbnail.
    
    """

    payload = {
        "username": "Today's Post",
        "embeds": [
            {
                "title": "Top Rising Post",
                "color": 102204,
                "description": message,
                "thumbnail": {"url": image_url},
            }
        ]
    }

    with requests.post(WEBHOOK_URL, json=payload) as response:
        print(response.status_code)
#
main()
