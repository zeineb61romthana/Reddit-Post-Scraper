import praw
import json

# Create a Reddit instance
reddit = praw.Reddit(
    client_id='zhWmTbsYov6YY00AdvpLRA',
    client_secret='aJQQM1vVMqCaVeDW5SXOJDgcwBBSxg',
    user_agent='my_reddit_app_v1.0'
)

# Define the specific post URL or ID
post_url = 'https://www.reddit.com/r/GYM/comments/1bgu16g/rgym_daily_simple_questions_and_misc_discussion/'

# Get the submission (post) object
submission = reddit.submission(url=post_url)

# Dictionary to store the post data
post_data = {
    'title':submission.title,
    'content': submission.selftext,
    'comments': []
}

# Fetch comments for the post
submission.comments.replace_more(limit=None)  # Replace "MoreComments" objects with actual comments
for comment in submission.comments.list():
    post_data['comments'].append({
        'comment': comment.body,
        'author': str(comment.author)  # Convert author to string (it can be None)
    })

# Save data to a JSON file
with open('reddit_post_7.json', 'w') as f:
    json.dump(post_data, f, indent=4)

print("reddit_post_7.json")