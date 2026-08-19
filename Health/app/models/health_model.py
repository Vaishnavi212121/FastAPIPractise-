'''
class HealthRecord:
    def __init__(self, status, app_name):
        self.status = status
        self.app_name = app_name
        '''

class HealthRecord:
    def __init__(
        self,
        id,
        patient_name,
        age,
        heart_rate,
        blood_pressure,
        temperature,
        oxygen_level,
        status
    ):
        self.id = id
        self.patient_name = patient_name
        self.age = age
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        self.oxygen_level = oxygen_level
        self.status = status