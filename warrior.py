class warrior:
    def __init__(self,id,name,ki,maxKi,race,gender,description,affiliation):
        self.id=id
        self.name=name
        self.ki=ki
        self.maxKi=maxKi
        self.race=race
        self.gender=gender
        self.description=description
        self.affiliation=affiliation
    def __str__(self):
        return f"warrior {self.id} {self.name}"