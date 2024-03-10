import requests

def get_latest_commits(username, repository, token):
    # Set the GitHub API endpoint
    api_url = f'https://api.github.com/repos/{username}/{repository}/commits'

    # Set headers, including the Authorization header with the GitHub token
    headers = {
        'Authorization': f'Token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Make the API request to get the latest commits
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch commits (HTTP {response.status_code})")
        return None

# Replace these variables with your GitHub username, repository, and personal access token
github_username = 'EuniceLeyanda'
github_repository = 'https://github.com/EuniceLeyanda/Assignment5.git'
github_token = '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'

# Call the function to get the latest commits
latest_commits = get_latest_commits(github_username, github_repository, github_token)

# Print the details of the latest commits
if latest_commits:
    print(f"Latest Commits in {github_username}/{github_repository}:\n")
    for commit in latest_commits:
        commit_data = commit['commit']
        author_name = commit_data['author']['name']
        commit_message = commit_data['message']
        print(f"Author: {author_name}\nMessage: {commit_message}\n")
else:
    print("Unable to retrieve commits.")
