import praw
import json

# Create a Reddit instance
reddit = praw.Reddit(
    client_id='zhWmTbsYov6YY00AdvpLRA',
    client_secret='aJQQM1vVMqCaVeDW5SXOJDgcwBBSxg',
    user_agent='my_reddit_app_v1.0'
)

# Get the subreddit
subreddit = reddit.subreddit('GYM')

# Initialize a list to store post data
posts = []

# Fetch posts
for submission in subreddit.hot(limit= None):
    # Dictionary to store each post's data
    post_data = {
        'title': submission.title,
        'content': submission.selftext,
        'comments': []
    }
    
    # Fetch comments for the post
    submission.comments.replace_more(limit=100)  # Replace "MoreComments" objects with actual comments
    for comment in submission.comments.list():
        post_data['comments'].append({
            'comment': comment.body,
            'author': str(comment.author)  # Convert author to string (it can be None)
        })
    
    # Add the post data to the list
    posts.append(post_data)

# Save data to JSON file
with open('reddit_posts_1.json', 'w') as f:
    json.dump(posts, f, indent=4)

print("Data saved to reddit_posts_with_comments.json")