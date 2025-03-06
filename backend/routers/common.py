from fastapi import APIRouter

router = APIRouter(prefix="/v1")

# 헬스체크 api
@router.get("/ping", status_code=200)
async def health_check():
    """
        Health Check API
    """

    return {"status" : "Good"}