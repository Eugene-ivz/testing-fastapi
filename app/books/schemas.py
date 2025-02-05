from pydantic import BaseModel, ConfigDict


class Book(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    
    model_config = ConfigDict(from_attributes=True)
    
    
class BookCreate(BaseModel):
    title: str
    description: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "new book",
                "description": "a nice book",
                
            }
        }
    }