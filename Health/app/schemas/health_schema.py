from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app: str

class HealthRecordCreate(BaseModel):
    patient_name: str
    age: int
    heart_rate: int
    blood_pressure: str
    temperature: float
    oxygen_level: int
    status: str

'''
class HealthRecordResponse(BaseModel):
    status: str
    app_name: str
'''
class HealthRecordResponse(BaseModel):
    id: int
    patient_name: str
    age: int
    heart_rate: int
    blood_pressure: str
    temperature: float
    oxygen_level: int
    status: str

'''
class HealthUpdateRequest(BaseModel):
    status: str
    '''

class HealthUpdateRequest(BaseModel):
    patient_name: str
    age: int
    heart_rate: int
    blood_pressure: str
    temperature: float
    oxygen_level: int
    status: str