# enum(enumerate)
from enum import Enum
class SmartPhone(Enum):
    samsung=1
    apple=2
    Nokia=3
print(SmartPhone.samsung)
print(SmartPhone.samsung.name)
print(SmartPhone.samsung.value)