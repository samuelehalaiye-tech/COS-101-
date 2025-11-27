formula_choice = str(input(" Pick A to E to use a formula\n Pick A for Velocity\n B for Acceleration\n C for Force\n D for potential Energy\n E for Kinetic Energy\n Put your Option here\n "))

if formula_choice == "A":
    displacement = int(input("Enter displacement here "))
    time= int(input("Enter time here "))
    velocity= displacement/time
    print("The Velocity is",velocity)

elif formula_choice == "B":
    velocity= int(input("Enter velocity here "))
    time= int(input("Enter time here "))
    acceleration= velocity/time
    print("The Acceleration is",acceleration)
elif formula_choice == "C":
    mass= int(input("Enter mass here "))
    acceleration= int(input("Enter acceleration here "))
    force= mass*acceleration
    print("The Force is",force)
elif formula_choice == "D":
    mass= int(input("Enter mass here "))
    gravity= int(input("Enter gravity here "))
    height= int(input("Enter height here "))
    potential_energy= mass*gravity*height
    print("The Potential Energy is",potential_energy)
elif formula_choice == "E":
    mass= int(input("Enter mass here "))
    velocity= int(input("Enter velocity here "))
    kinetic_energy= 1/2*mass*(velocity^2)
    print= ("The Kinetic Energy is",kinetic_energy)
else:
    print("invalid input")