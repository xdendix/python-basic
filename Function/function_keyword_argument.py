def cetakProfile(name, age, address, hobby):  # keyword arguments
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")
    print(f"Hobby: {hobby}")


cetakProfile(  # keyword arguments
    address="Jakarta",  # positional argument
    hobby="Coding",  # keyword arguments
    name="Budi",  # positional argument
    age=25  # keyword arguments
)
