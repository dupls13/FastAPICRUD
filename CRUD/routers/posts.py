from fastapi import APIRouter, Path, HTTPException, status 
from .. import models 

post_router = APIRouter()

post_list = []

#Create
@post_router.post("/post")
async def add_post(post: models.Post): 
    post_list.append(post)
    return {
        "message": "Post added successfully"
    }


# Retrieve 
@post_router.get("/post", status_code = 201)
async def get_posts():
    return {
        "posts": post_list
    }
    
@post_router.get("/post/{post_id}")
async def get_specific_post(post_id: int = Path(..., title = "The ID fo the post to retrieve.")):
    for post in post_list: 
        if post.id == post_id:
            return {
                "post": post
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Post with ID {post_id} doesn't exist."
    )
    



# Update
@post_router.put("/post/{post_id}")
async def update_post(post_data: models.PostItem, post_id: int = Path(..., title = "ID of post updated")):
    for post in post_list:
        if post.id == post_id:
            post.title = post_data.title 
            post.content = post_data.content 
            return {
                "message": "Post updated successfully"
            }

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Post with ID {post_id} doesn't exist."
    )

# Delete
@post_router.delete("/post")
async def delete_all_posts():
    post_list.clear()
    return {
        "message": "Posts deleted successfully"
    }
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Post with ID {post_id} doesn't exist."
    )