from fastapi import APIRouter , Depends
from app.schemas.health_schema import (HealthResponse,HealthRecordResponse,HealthUpdateRequest)
from app.services.health_service import (get_health_status,get_all_health_records, update_health_status)
from app.dependencies.health_dependency import get_app_name

router = APIRouter()

'''
@router.get("/health", response_model=HealthResponse)
def health():
    return {
        "status": "healthy"
    }
'''
'''
@router.get("/health", response_model=HealthResponse)
def health():
    return get_health_status()
'''

@router.get("/health", response_model=HealthResponse)
def health(app_name: str = Depends(get_app_name)):
    return get_health_status(app_name)

'''
@router.get("/health/records")
def get_health_records():
    return get_all_health_records()
    '''

@router.get(
    "/health/records",
    response_model=list[HealthRecordResponse]
)
def get_health_records():
    return get_all_health_records()

@router.put(
    "/health/records/{index}",
    response_model=HealthResponse
)
def update_health(index: int, request: HealthUpdateRequest):
    return update_health_status(index, request.status)