
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# The datamodels.
# they are referred to as moulds instead, because the terms PieceModels and BoardModel became confusing rather clear, as in normal speach piece and model can be used nearly interchangeably, so mould have selected instead as piece and board are cast in moulds.

class pieceMould(BaseModel):
    name: str = Field(...)
    xPos: int = Field(...)
    yPos: int = Field(...)
    size: int = Field(default=1)
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        #json_encoders = {ObjectId: str}
        """
        schema_extra = {
            "example": {
                #"uid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "the piecest piece of pieces",
                "xPos": "0",
                "yPos": "1",
                "size": "2",
                "created": "2023-09-21T10:51:56.938Z",
                "updated": "2023-09-21T10:51:56.938Z" 
            }
        }
        """
           
class updatePieceMould(BaseModel):
    name: Optional[str]
    xPos: Optional[int]
    yPos: Optional[int]
    size: Optional[int]
    updated: datetime = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True
        """
        schema_extra = {
            "example": {
                #"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "the most updated piece of pieces",
                "xPos": "0",
                "yPos": "1",
                "size": "2",
                "created": "2023-09-21T10:51:56.938Z", 
                "updated": "2023-09-21T10:51:56.938Z" 
            }
        }
        """

def pieceHelper(piece) -> dict:
    return {
        "id": str(piece["_id"]),
        "name": piece["name"],
        "xPos": piece["xPos"],
        "yPos": piece["yPos"],
        "size": piece["size"],
        "created": piece["created"],
        "updated": piece["updated"],        
    }