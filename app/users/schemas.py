from pydantic import BaseModel, ConfigDict
    
    
class User(BaseModel):
    id: int
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)
    
    
    
class UserCreate(BaseModel):
    name: str
    email: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John",
                "email": "johndoe123@c.com",
                
            }
        }
    }
    

