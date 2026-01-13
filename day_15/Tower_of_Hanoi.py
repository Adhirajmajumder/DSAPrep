### Tower Of Hanoi ###

def tower_of_Hanoi(n, source, auxaliary, destination):
    if n == 0:
        return 
    
    tower_of_Hanoi(n-1, source, destination, auxaliary)
    print(f"Disk {n} moved from {source} to {destination}")
    tower_of_Hanoi(n-1, auxaliary, source, destination)

tower_of_Hanoi(3, "A","B","C")