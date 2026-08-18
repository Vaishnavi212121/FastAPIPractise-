from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app: str

class HealthRecordResponse(BaseModel):
    status: str
    app_name: str

class HealthUpdateRequest(BaseModel):
    status: str