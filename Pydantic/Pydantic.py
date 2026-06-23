from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length = 50, title= 'Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['suhas', 'sam'])]
    email : EmailStr
    Linkdein_URL : AnyUrl
    age : int
    weight : Annotated[float, Field(gt = 0, strict=True)]
    married : Annotated[bool, Field(default = None)]
    allegries : Annotated[Optional[List[str]], Field(default = None, max_length = 5)]
    contact_details : Dict[str, str]

def update_patient_info(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allegries)
    print("Data Inserted")

patient_info = {'name' : 'suhas', 'email' : 'suhas@gmail.com', 'Linkdein_URL' : 'http://likdein.com/1233', 'age' : '21', 'weight' : 72.5, 'married' : 'False', 'contact_details' : { 'phone' : '23487578'}}

patient1 = Patient(**patient_info)

update_patient_info(patient1)

