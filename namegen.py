from googleapiclient.discovery import build

# API-Key
api_key = "YOUR API KEY"

youtube = build('youtube', 'v3', developerKey=api_key)

def get_youtube_url(query):
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1,  # result limit
        type="video",
        regionCode="DE"  # region code
    )
    response = request.execute()

    urls = []
    if response['items']:
        for item in response['items']:
            video_id = item['id']['videoId']
            urls.append(f"https://www.youtube.com/watch?v={video_id}")
    return urls

# Title from file
def read_titles_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        titles = [line.strip() for line in file.readlines()]
    return titles

# load titles
titles = read_titles_from_file('titles.txt')

# get URLs
urls = {title: get_youtube_url(title) for title in titles}

# URLs ausgeben
for title, url_list in urls.items():
    print(f"{title}:")
    for url in url_list:
        print(f" - {url}")
