# 📄 Reddit Post Scraper: GYM Subreddit Comments

This Python script scrapes a specific Reddit post from the **r/GYM** subreddit, extracting the post's title, content, and all associated comments. The data is then stored in a structured JSON format for further analysis or usage.

## 🚀 Functionality Overview:

1. **Reddit API Access**: Utilizes the `praw` library to interact with Reddit's API, fetching the content of a post and its comments.
2. **Post & Comment Extraction**: Extracts the post's title, main content, and all user comments, including the username of the comment author.
3. **Data Storage**: Saves the collected data as a structured JSON file for easy manipulation and analysis.

## 🛠️ Technologies and Libraries Used:
- **PRAW (Python Reddit API Wrapper)**: For interacting with Reddit’s API to fetch posts and comments.
- **JSON**: For storing the scraped data in a readable and structured format.

## 📑 Code Walkthrough:

- **Reddit Instance Creation**: A Reddit instance is created using the `praw.Reddit()` function with client credentials (`client_id`, `client_secret`, `user_agent`).
- **Post Retrieval**: The specific post is fetched using its URL, and a submission object is created.
- **Comment Extraction**: All comments are fetched, including nested ones, and stored in a dictionary along with the post title and content.
- **Saving Data**: The final structured data is written to a JSON file (`reddit_post_7.json`).

## 🔍 Example Post Scraped:
The example post being scraped is a **Daily Simple Questions and Misc Discussion** thread from the **r/GYM** subreddit.

### Data Structure:
The scraped data is saved in the following format:
```json
{
    "title": "Post Title",
    "content": "Main post content goes here...",
    "comments": [
        {
            "comment": "First comment content",
            "author": "comment_author_1"
        },
        {
            "comment": "Second comment content",
            "author": "comment_author_2"
        },
        ...
    ]
}
