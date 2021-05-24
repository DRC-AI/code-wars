def validate_pin(pin):
    return str(pin).isdigit() and len(pin) in (4, 6) 

print(validate_pin('1234'))
