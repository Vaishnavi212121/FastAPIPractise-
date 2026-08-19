from app.models.health_model import HealthRecord
import json
from pathlib import Path
DATA_FILE = Path(__file__).parent.parent / "health_data.json"

def load_health_records():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_health_records(records):
    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)
#health_records = []

'''
def create_health_record(status, app_name):
    record = {
        "status": status,
        "app_name": app_name
    }
'''
'''
def create_health_record(status, app_name):
    records = load_health_records()

    record = {
        "status": status,
        "app_name": app_name
    }

    records.append(record)
    save_health_records(records)
    return HealthRecord(status, app_name)

'''

def create_health_record(
    patient_name,
    age,
    heart_rate,
    blood_pressure,
    temperature,
    oxygen_level,
    status
):
    records = load_health_records()

    new_id = len(records) + 1

    record = {
        "id": new_id,
        "patient_name": patient_name,
        "age": age,
        "heart_rate": heart_rate,
        "blood_pressure": blood_pressure,
        "temperature": temperature,
        "oxygen_level": oxygen_level,
        "status": status
    }

    records.append(record)
    save_health_records(records)

    return HealthRecord(
        new_id,
        patient_name,
        age,
        heart_rate,
        blood_pressure,
        temperature,
        oxygen_level,
        status
    )

'''
def get_health_records():
    return health_records
'''

'''
def get_health_records():
    return load_health_records()

    '''

def get_health_records():
    records = load_health_records()

    return [
        HealthRecord(
            record["id"],
            record["patient_name"],
            record["age"],
            record["heart_rate"],
            record["blood_pressure"],
            record["temperature"],
            record["oxygen_level"],
            record["status"]
        )
        for record in records
    ]

def get_health_record_by_id(record_id):
    records = load_health_records()

    for record in records:
        if record["id"] == record_id:
            return HealthRecord(
                record["id"],
                record["patient_name"],
                record["age"],
                record["heart_rate"],
                record["blood_pressure"],
                record["temperature"],
                record["oxygen_level"],
                record["status"]
            )

    return None
'''
def update_health_record(index, status):
    health_records[index].status = status

    return health_records[index]
    '''

def update_health_record(
    record_id,
    patient_name,
    age,
    heart_rate,
    blood_pressure,
    temperature,
    oxygen_level,
    status
):
    records = load_health_records()

    for record in records:
        if record["id"] == record_id:
            record["patient_name"] = patient_name
            record["age"] = age
            record["heart_rate"] = heart_rate
            record["blood_pressure"] = blood_pressure
            record["temperature"] = temperature
            record["oxygen_level"] = oxygen_level
            record["status"] = status

            save_health_records(records)

            return HealthRecord(
                record["id"],
                record["patient_name"],
                record["age"],
                record["heart_rate"],
                record["blood_pressure"],
                record["temperature"],
                record["oxygen_level"],
                record["status"]
            )

    return None

def delete_health_record(record_id):
    records = load_health_records()

    for record in records:
        if record["id"] == record_id:
            records.remove(record)
            save_health_records(records)
            return True

    return False