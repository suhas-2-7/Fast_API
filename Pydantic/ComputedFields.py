from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    height : float 
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def update_patient_info(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')


patient_info = {'name' : 'sam', 'email' : 'sam@gmail.com', 'age' : 30, 'weight' : 72.3, 'height' : 1.75, 'married' : 0, 'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '5689985577'}}

patient1 = Patient(**patient_info)

update_patient_info(patient1)
