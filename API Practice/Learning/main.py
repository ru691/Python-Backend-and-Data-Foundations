age: int
age = 19
name: str
name = "Angela"
height : float
height = 1.79
is_human : bool
is_human = True

def police_check(age) -> bool:
    if age >= 18:
        can_drive = True
    else :
        can_drive = False
    return can_drive

print(police_check(age))
