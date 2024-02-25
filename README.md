### Installation
1. <a href="https://docs.python.org/3/tutorial/venv.html ">Create and activate virtual environments</a>
2. Install requirements.txt
```sh
    pip install -r requirements.txt
   ```

## API Documentation

## Introduction
The API provides access to posts and scores data.

## Get All Posts
Retrieves a list of all posts.

- URL: `/post/`
- Method: GET
- Parameters: None


## Get All Score
Retrieves a list of all scores.

- URL: `/score/`
- Method: GET
- Parameters: None


## Add a Score

- URL: `/score/`
- Method: POST
- Parameters: score, user, post

  
## Add a Post

- URL: `/post/`
- Method: POST
- Parameters: title, body

## Update Score
Updates the score with the specified ID.

- URL: `/score-update/<score_id>/`
- Method: PUT
- score_id: The ID of the score to be updated (integer)
- Other parameters required for the update

note : I didn't implement authentication because you asked me to keep it simple.
