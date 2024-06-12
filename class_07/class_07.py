from typing import Dict, Union, Optional

key = Union[int, str] # Create Custom type
value = Union[int, str, dict, set, tuple]

data : Dict[key,value] = {
    "name" : "Muhammad Afzal",
    "age" : "26",
    "city" : "Nankana Sahib",
    "country" : "Pakistan",
    "hobbies" : {"reading", "writing", "coding"},
    "education" : "Masters in Computer Science"
}
print(data)
