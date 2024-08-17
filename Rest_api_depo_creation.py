import requests


# GitLab credentials to create a new repos

GITHUB_TOKEN = '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'
GITHUB_USERNAME = 'https://github.com/ErtonyBashil'
REPO_NAME = 'Exam_control_versioning'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# To create a new repository

create_repo_url = f'https://api.github.com/user/repos'
repo_data = {
    'name': REPO_NAME,
    'description': 'This is a new repository created using GitHub API',
    'private': False  # We specify the public repo here
}

response = requests.post(create_repo_url, headers=headers, json=repo_data)

if response.status_code == 201:
    print(f'Repos created')
else:
    print(f'Failed to create, try again')

# Once the repos has been creatted we have to create two issues


if response.status_code == 201:
    repo_full_name = response.json()['full_name']
    
    create_issue_url = f'https://api.github.com/repos/{repo_full_name}/issues'
    
    # Create first issue
    issue1_data = {
        'title': 'First ticket|issue',
        'body': 'check out the first issue in here'
    }
    issue1_response = requests.post(create_issue_url, headers=headers, json=issue1_data)
    
    if issue1_response.status_code == 201:
        print('First issue created')
    else:
        print(f'Failed check your settings')
    
    # Create second issue
    issue2_data = {
        'title': 'Second ticket',
        'body': '2nd '
    }
    issue2_response = requests.post(create_issue_url, headers=headers, json=issue2_data)
    
    if issue2_response.status_code == 201: # check if the code passed
        print('Second issue created')
    else:
        print(f'Failed check your settings')

