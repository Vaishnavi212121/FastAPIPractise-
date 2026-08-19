#from app.cruds.health_crud import create_health_record
from app.cruds.health_crud import (
    create_health_record,
    get_health_records,
    get_health_record_by_id,
    update_health_record,
    delete_health_record
)

'''
def get_health_status(app_name):
    return {
        "status": "healthy",
        "app": app_name
    }
    '''
'''
def get_health_status(app_name):
    return create_health_record("healthy", app_name)
    '''
'''
def get_health_status(app_name):
    record = create_health_record("healthy", app_name)

    return {
        "status": record.status,
        "app": record.app_name
    }
'''
def create_health_record_service(
    patient_name,
    age,
    heart_rate,
    blood_pressure,
    temperature,
    oxygen_level,
    status
):
    return create_health_record(
        patient_name,
        age,
        heart_rate,
        blood_pressure,
        temperature,
        oxygen_level,
        status
    )

def get_all_health_records():
    return get_health_records()

def get_health_record_by_id_service(record_id):
    return get_health_record_by_id(record_id)

'''
def update_health_status(index, status):
    record = update_health_record(index, status)

    return {
        "status": record.status,
        "app": record.app_name
    }
    '''

def update_health_status(
    record_id,
    patient_name,
    age,
    heart_rate,
    blood_pressure,
    temperature,
    oxygen_level,
    status
):
    return update_health_record(
        record_id,
        patient_name,
        age,
        heart_rate,
        blood_pressure,
        temperature,
        oxygen_level,
        status
    )

def delete_health_record_service(record_id):
    return delete_health_record(record_id)