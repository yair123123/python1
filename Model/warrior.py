from os.path import split

import requests
import toolz
from toolz import pipe, compose
from toolz.curried import partial


class warrior:
    def __init__(self,uid,name,ki,maxKi,race,gender,description,affiliation,type):
        self.uid=uid
        self.name=name
        self.ki=ki
        self.maxKi=maxKi
        self.race=race
        self.gender=gender
        self.description=description
        self.affiliation=affiliation
        self.type = type

    def __repr__(self):
        return f"warrior {self.uid} {self.name} {self.type}"
    def __gt__(self, other):
        to_int = compose(
            int,
            "".join,
            lambda s:s.split(".")
        )
        return pipe(
            other.ki,
            to_int,
            lambda x:x > to_int(self.ki),
        )