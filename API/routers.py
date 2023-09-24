from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from models import pieceMould, updatePieceMould, pieceHelper
from bson.objectid import ObjectId

router = APIRouter()

#create route
@router.post("/", response_description="Add piece")
async def newPiece(request: Request, piece: pieceMould = Body(...)):
    piece = jsonable_encoder(piece)
    creatorAllmighty = await request.app.mongodb["pieces"].insert_one(piece) #name choosen make clear whom is the creator and whom is the created
    creationPowerless = await request.app.mongodb["pieces"].find_one({"_id": creatorAllmighty.inserted_id}) #name choosen make clear whom is the creator and whom is the created
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=pieceHelper(creationPowerless))

#read routes
@router.get("/{id}", response_description="Get a piece")
async def showPiece(id: str, request: Request):
    if (piece := await request.app.mongodb["pieces"].find_one({"_id": ObjectId(id)})) is not None: return pieceHelper(piece)
    raise HTTPException(status_code=404, detail=f"Piece {id} not found")

@router.get("/", response_description="List all pieces")
async def listAllPieces(request: Request):
    piecesList = []
    for piece in await request.app.mongodb["pieces"].find().to_list(length=100):
        piecesList.append(pieceHelper(piece))
    return piecesList

#update route
@router.put("/{id}", response_description="Update a piece")
async def updatePiece(id: str, request: Request, piece: updatePieceMould = Body(...)):
    piece ={k: v for k, v in piece.dict().items() if v is not None}
    if len(piece) >= 1:
        pieceProcessing = await request.app.mongodb["pieces"].update_one({"_id": ObjectId(id)}, {"$set": piece})
        if pieceProcessing == 1:
            if pieceDonecessing := await request.app.mongodb["pieces"].find_one({"_id": ObjectId(id)}) is not None: return pieceDonecessing
    if pieceFinished := await request.app.mongodb["pieces"].find_one({"_id": ObjectId(id)}) is not None: return pieceFinished
    raise HTTPException(status_code=404, detail=f"Piece {id} not found")

#delete route
@router.delete("/{id}", response_description="Delete a piece")
async def deltePiece(id: str, request: Request):
    deletePiece = await request.app.mongodb["pieces"].delete_one({"_id": ObjectId(id)})
    if deletePiece.deleted_count == 1: return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Piece {id} not found")