class House:
    def __init__(self,table,bedrooms,chairs,bathroom,roof,floor,adress):
        self.table=table
        self.bedrooms=bedrooms
        self.chairs=chairs
        self.bathroom=bathroom
        self.roof=roof
        self.floor=floor
        self.adress=adress
house1=House("1 table","64 bedrooms","435343 chairs","348338473747373 bathroom","4954893848958 roof","1 floor"," 24 blueberrys to eat")
print(house1.adress)