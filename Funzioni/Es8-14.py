def make_car(manufacturer:str, model_name:str, **info):
    car = f"{manufacturer} {model_name}"
    for key,value in info.items():
        car += f", {key} {value}"
    return car
car = make_car("toyota", "corolla", color="red", km="10.000" )
print(car)