men= ["Rio", "Kylo", "Miles", "Lunis"]

def line(queu):
    if type(queu) is list and len(queu)>0:
        rotation = []
        for element in queu:
            rotation.append(f"{queu.index(element) +1}. {element}")
        print("The line is currently: " + " ".join(rotation))
        return "The line is currently: " + " ".join(rotation)
    else:
        print("The line is currently empty.")
        return "The line is currently empty."
    
def take_a_number(queu, new_person):
    if len(queu) > 0:
        queu.append(new_person)
        print(f"Welcome, {new_person}. You are number {queu.index(new_person) +1} in line.")
    else:
        queu.append(new_person)
        print(f"Welcome, {new_person}. You are number {queu.index(new_person) +1} in line.")
    
def now_serving():
    pass