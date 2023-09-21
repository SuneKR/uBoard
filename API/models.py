
#from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional
import uuid

from pydantic import BaseModel, Field

# The datamodels.
# they are referred to as moulds instead, because the terms PieceModels and BoardModel became confusing rather clear, as in normal speach piece and model can be used nearly interchangeably, so mould have selected instead as piece and board are cast in moulds.

class pieceMould(BaseModel):
    id: uuid.UUID = Field(alias="_id", default_factory=lambda: uuid.uuid4())
    name: str = Field(...)
    xPos: int
    yPos: int
    size: int
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "the piecest piece of pieces",
                "xPos": "0",
                "yPos": "1",
                "size": "2",
                "created": "2023-09-21T10:51:56.938Z",
                "updated": "2023-09-21T10:51:56.938Z" 
            }
        }
           
class updatePieceMould(BaseModel):
    name: Optional[str]
    xPos: Optional[int]
    yPos: Optional[int]
    size: Optional[int]
    updated: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "the most updated piece of pieces",
                "xPos": "0",
                "yPos": "1",
                "size": "2",
                "created": "2023-09-21T10:51:56.938Z", 
                "updated": "2023-09-21T10:51:56.938Z" 
            }
        }
    
    