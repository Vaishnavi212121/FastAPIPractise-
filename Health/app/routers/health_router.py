from fastapi import APIRouter ,HTTPException #Depends
from app.schemas.health_schema import (HealthResponse,HealthRecordResponse,HealthUpdateRequest,HealthRecordCreate)
from app.services.health_service import (create_health_record_service,get_all_health_records,get_health_record_by_id_service, update_health_status,delete_health_record_service)
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
'''
@router.get("/health", response_model=HealthResponse)
def health(app_name: str = Depends(get_app_name)):
    return get_health_status(app_name)
'''
@router.get("/health", response_model=HealthResponse)
def health():
    return {
        "status": "healthy",
        "app": "Health API"
    }

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

'''
@router.put(
    "/health/records/{index}",
    response_model=HealthResponse
)
def update_health(index: int, request: HealthUpdateRequest):

    return update_health_status(index, request.status)
'''
@router.put("/health/records/{record_id}", response_model=HealthRecordResponse)
def update_health(
    record_id: int,
    request: HealthUpdateRequest
):
    record = update_health_status(
        record_id,
        request.patient_name,
        request.age,
        request.heart_rate,
        request.blood_pressure,
        request.temperature,
        request.oxygen_level,
        request.status
    )

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Health record not found"
        )

    return record

'''

@router.post("/health/records", response_model=HealthRecordResponse)
def create_health_record_endpoint(request: HealthRecordCreate):
    return create_health_record(
        request.patient_name,
        request.age,
        request.heart_rate,
        request.blood_pressure,
        request.temperature,
        request.oxygen_level,
        request.status
    )
    '''

@router.post("/health/records", response_model=HealthRecordResponse)
def create_health_record_endpoint(request: HealthRecordCreate):
    return create_health_record_service(
        request.patient_name,
        request.age,
        request.heart_rate,
        request.blood_pressure,
        request.temperature,
        request.oxygen_level,
        request.status
    )

@router.get("/health/records/{record_id}", response_model=HealthRecordResponse)
def get_health_record(record_id: int):
    record = get_health_record_by_id_service(record_id)

    if record is None:
        raise HTTPException(status_code=404, detail="Health record not found")

    return record

@router.delete("/health/records/{record_id}")
def delete_health_record_endpoint(record_id: int):
    deleted = delete_health_record_service(record_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Health record not found"
        )

    return {
        "message": "Health record deleted successfully"
    }