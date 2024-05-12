from pydantic import BaseModel 

class BlogModel(BaseModel):
    title : str 
    description : str  
    author : str 
    tags : list 

class UpdateBlogModel(BaseModel):
    title : str  = None
    description : str  = None 
    author : str = None 
    tags : list = None    

class CommentModel(BaseModel):
    text: str
    user: str
    blog_id: str  
    blog_title: str = None  # Optional 

class LikeDislikeModel(BaseModel):
    user: str
    liked: bool
    blog_id: str
    blog_title: str = None  # Optional     