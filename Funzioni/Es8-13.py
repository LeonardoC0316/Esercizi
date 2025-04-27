def build_profile(first, last, **info):
    profile = f"{first} {last}"
    for key, value in info.items():
        profile += f", {key} {value}"
    return profile

my_profile = build_profile("Leonardo", "Cimitan", age= 21, hair="castani", weight=75)
print(my_profile)