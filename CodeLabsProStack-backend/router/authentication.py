import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import APIRouter, Depends, status, HTTPException, Response
import schemas, models, database
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db())):
    user = db.query(models.User).filter(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    return user


