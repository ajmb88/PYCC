from operator import itemgetter
from plotly.graph_objs import Bar, Layout
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code: {r.status_code}")


# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dicitonary for each article.
    if 'descendants' in response_dict:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

y = 1
number_order = []
titles = []
links = []
comments = []

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link:{submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

    title = submission_dict['title']
    link = submission_dict['hn_link']
    comment = submission_dict['comments']

    titles.append(title)
    links.append(link)
    comments.append(comment)
    
    number_order.append(y)
    y += 1

print(f"\nTitles: {titles},\nLinks: {links},\nComments: {comments}")


x_value = titles
data = (Bar(x = x_value, y = comments))

x_axis_config = {'title': 'Conversations'}
y_axis_config = {'title': 'Comment Ammount'}
my_layout = Layout(title="Popularity of hacker News articles", xaxis = x_axis_config,
                    yaxis = y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename= 'HackerNews.html')



