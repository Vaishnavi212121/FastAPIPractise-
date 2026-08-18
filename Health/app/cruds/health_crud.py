from app.models.health_model import HealthRecord
health_records = []


'''
def create_health_record(status, app_name):
    record = {
        "status": status,
        "app_name": app_name
    }
'''
def create_health_record(status, app_name):
    record = HealthRecord(status, app_name)
    health_records.append(record)

    return record

def get_health_records():
    return health_records

def update_health_record(index, status):
    health_records[index].status = status

    return health_records[index]