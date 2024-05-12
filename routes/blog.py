from fastapi import APIRouter 
from models.blog import BlogModel,UpdateBlogModel,CommentModel,LikeDislikeModel
from config.db import blogs_collection
from serializer.blog import BlogEntity, BlogEntities
import datetime
from bson import ObjectId
from typing import List  

node = APIRouter()

# Add new blog
@node.post("/add/blog")
def NewBlog(doc:BlogModel):
    doc = dict(doc)
    current_date = datetime.date.today()
    doc["date"] = str(current_date )
    
    res = blogs_collection.insert_one(doc)

    doc_id = str(res.inserted_id )

    return {
        "status" : "done" ,
        "message" : "Blog posted successfully" , 
        "_id" : doc_id
    }
 
 # Get all blogs
@node.get("/getall/blogs")
def AllBlogs():
    res =  blogs_collection.find() 
    blog_data = BlogEntities(res)

    return {
        "status": "ok" , 
        "data" : blog_data
    }

#Get a blog
@node.get("/get/{_id}") 
def GetBlog(_id:str) :
    res = blogs_collection.find_one({"_id" : ObjectId(_id) }) 
    blog_data = BlogEntity(res)
    return {
        "status" : "ok" ,
        "data" : blog_data
    }

# update blog 
@node.patch("/update/{_id}")
def UpdateBlog(_id: str , doc:UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True)) 
    blogs_collection.find_one_and_update(
       {"_id" : ObjectId(_id) } ,
       {"$set" : req}
    )

    return {
        "status" : "ok" ,
        "message" : "blog updated successfully"
    }


# delete blog 
@node.delete("/delete/{_id}")
def  DeleteBlog(_id : str):
    blogs_collection.find_one_and_delete(
        {"_id" : ObjectId(_id)}
    )

    return {
        "status" : "ok" ,
        "message" : "Blog deleted successfully"
    }

#Create comment on Blog post
@node.post("/blogs/{blog_id}/comments/", response_model=CommentModel)
def create_comment(blog_id: str, comment: CommentModel):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        return {"status": 404, "message": "Not found blog"}

 
    comment.blog_title = blog["title"]
    comment.blog_id = blog_id  
    
    comment_dict = dict(comment)
    current_date = datetime.date.today()
    comment_dict["date"] = str(current_date )
    blogs_collection.update_one({"_id": ObjectId(blog_id)}, {"$push": {"comments": comment_dict}})
    
    return comment

# Like or dislike a blog post
#true-user liked the blog
#false-user didn't like the blog
@node.post("/blogs/{blog_id}/like_dislike/", response_model=LikeDislikeModel)
def like_dislike_blog(blog_id: str, like_dislike: LikeDislikeModel):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        return {"status": 404, "message": "Not found blog"}

    like_dislike.blog_title = blog["title"]
    like_dislike.blog_id = blog_id

    like_dislike_dict = dict(like_dislike)
    blogs_collection.update_one({"_id": ObjectId(blog_id)}, {"$push": {"likes_dislikes": like_dislike_dict}})
    
    return like_dislike

