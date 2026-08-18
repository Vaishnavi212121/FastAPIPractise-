#from app.cruds.health_crud import create_health_record
from app.cruds.health_crud import (
    create_health_record,
    get_health_records,
    update_health_record
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

def get_health_status(app_name):
    record = create_health_record("healthy", app_name)

    return {
        "status": record.status,
        "app": record.app_name
    }

def get_all_health_records():
    return get_health_records()

def update_health_status(index, status):
    record = update_health_record(index, status)

    return {
        "status": record.status,
        "app": record.app_name
    }