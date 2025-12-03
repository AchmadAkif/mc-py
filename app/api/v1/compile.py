from fastapi import APIRouter

router = APIRouter(prefix="/compile")

@router.get("/start")
def startCompiler():
    return {"status": "success", "result": "result"}

@router.get("/download")
def downloadFile():
    return {"status": "success", "result": "result"}