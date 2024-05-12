from fastapi import APIRouter 

entry_root = APIRouter()

# endpoint 
@entry_root.get("/")
def apiRunning():
    res = {
        "status" : "ok" ,
        "message" : "FastAPI is running!!!"
    }
    return res