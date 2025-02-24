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
    
def take_a_number():
    pass
    
def now_serving():
    pass