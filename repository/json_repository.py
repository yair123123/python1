import json

from Model.warrior import warrior


def read_json(path):
    try:
        with open (path,'r') as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []
def convert_from_json_warrior(json,type):
    return warrior(
        uid=json["id"],
        name=json['name'],
        ki=json['ki'],
        maxKi=json['maxKi'],
        race=json['race'],
        gender=json['gender'],
        description=json['description'],
        affiliation=json['affiliation'],
        type=type
    )
def fight(obj1,obj2):
    return obj1 if obj1>obj2 else obj2