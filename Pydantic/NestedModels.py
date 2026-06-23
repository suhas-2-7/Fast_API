from pydantic import BaseModel

class Address(BaseModel):

    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city' : 'banglore', 'state' : 'Karnataka', 'pin' : '576512'}

address1 = Address(**address_dict)

patient_info = {'name' : 'sam', 'gender' : 'male', 'age' : 21, 'address' : address1}

patient1 =  Patient(**patient_info)

print(patient1.address.city)