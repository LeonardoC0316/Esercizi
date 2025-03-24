'''8-6. City Names: Write a function called city_country()
that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs,
and print the values that are returned.'''

def city_country(**kwargs):
    for k, v in kwargs.items():
        print(f'"{k}, {v}"')

city_country(roma="Italia", foggia="Italia", milano="Italia")

list = [1,2,3,4,5,6,7]
for i in list:
    i+=1
    print(i)
