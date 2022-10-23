from pydantic import BaseModel

class Post(BaseModel):
    id: int 
    title: str
    content: str
    
class PostItem(BaseModel):
    title: str
    content: str
        
    class Config: 
        title: str
        content: str
