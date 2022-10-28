from pydantic import BaseModel
from typing import List 

class Post(BaseModel):
    id: int 
    title: str
    content: str
    
class PostItem(BaseModel):
    posts: List[Post]
    
    class Config: 
        orm_mode = True
