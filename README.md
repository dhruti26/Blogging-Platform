# Simple Blogging System 
Welcome to the Blogging Platform API! This API allows you to interact with a simple blogging platform, enabling users to create, read, update, and delete blog posts, add comments to blog posts, and like/dislike blog posts.


## Base URL
The base URL for all API endpoints is:

  ```bash
     http://127.0.0.1:8000
  ```
## Error Handling
The API follows standard HTTP status codes for indicating the success or failure of a request. In case of an error, additional information is provided in the response body.

**To set up and run the API locally, follow these steps:**

### Step 1: Clone the Repository
Clone the repository containing the codebase to your local machine.

```bash
      git clone <repository_url>
      cd <repository_name>
```
### Step 2: Install Dependencies
Install the required Python dependencies using pip mentioned in downloadmodules.txt file.
```bash
      pip install -r downloadmodules.txt
```

### Step 3: Configure MongoDB
Make sure you have MongoDB installed and running locally on the default port (27017). Create a database named Blogging.

### Step 4: Update Configuration (if required)
If your MongoDB configuration differs from the default, update the connection string in config/db.py accordingly.

### Step 5: Run the API
Run the FastAPI server using uvicorn.
```bash
  uvicorn main:app --reload
```
## API Documentation
Endpoints:

**1. Create a new blog post**

- URL: /add/blog
- Method: POST
- Request Body:
  1. title (string, required): Title of the blog post

  2. description (string, required): Description of the blog post

  3. author (string, required): Author of the blog post
   
  4. tags (list of strings, required): Tags associated with the blog post

- Response: JSON object containing the status, message, and ID of the newly created blog post.


**2. Retrieve all blog posts**
- URL: /getall/blogs
- Method: GET
- Response: JSON object containing the status and data, where data is a list of all blog posts.

**3. Retrieve a specific blog post by ID**
- URL: /get/{blog_id}
- Method: GET
- Response: JSON object containing the status and data, where data is the specified blog post.
  
**4. Update a blog post by ID**
- URL: /update/{blog_id}
- Method: PATCH
- Request Body: JSON object containing fields to be updated (title, description, author, tags)
- Response: JSON object containing the status and message indicating the success of the update operation.

 **5. Delete a blog post by ID**
- URL: /delete/{blog_id}
- Method: DELETE
- Response: JSON object containing the status and message indicating the success of the delete operation.

**6. Add a comment to a blog post**
- URL: /blogs/{blog_id}/comments/
- Method: POST
- Request Body:
   1. text (string, required): Text of the comment
   2. user (string, required): User who posted the comment
- Response: JSON object containing the status, message, and details of the posted comment.

  **7. Like or dislike a blog post**
- URL: /blogs/{blog_id}/like_dislike/ 
- Method: POST
- Request Body:
 1. user (string, required): User who liked/disliked the blog post
 2. liked (boolean, required): Indicates whether the user liked (true) or disliked (false) the blog post
- Response: JSON object containing the status, message, and details of the like/dislike action.

## Data Models
  **Examples :**

**Blog Model:**
```json
{
    "title": "Example Blog Post",
    "description": "This is an example blog post.",
    "author": "John Doe",
    "tags": ["example", "blog", "post"]
}
```

**UpdateBlog Model**
```json
{
    "description": "This is the updated content of the blog post.",
    "author": "Jane Smith"
}
```
**CommentModel**
```json
{
    "text": "This is a comment on the example blog post.",
    "user": "Alice",
    "blog_id": "1234567890"
}
```
**LikeDislike Model**
```json
{
    "user": "Bob",
    "liked": true,
    "blog_id": "1234567890"
}
```

### Key features:

- Create, read, update, and delete blog posts.
- Add comments to blog posts.
- Like or dislike blog posts.
- Store data in a MongoDB database.
- Built with FastAPI and adheres to RESTful principles.
- Object-oriented programming for clean and maintainable code.
