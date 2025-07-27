from pydantic import BaseModel
from typing import List, Optional

class Car(BaseModel):
    manufacturer: str
    model_name: str
    manufacturing_year: str
    variant_name: str
    showroom_price: str
    fuel_type: str
    engine_capacity_cc: str
    body_type: str
    seating_capacity: str
    torque_nm: str
    mileage_kmpl: str
    power_bhp: str
    transmission: str
    safety_rating: str
    features: List[str]