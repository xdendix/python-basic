def sayHello(*, name):  # keyword argument only
    print(f"Hello, {name}!")


sayHello(name="Alice")  # This will work
# sayHello("Alice")  # This will raise a TypeError
