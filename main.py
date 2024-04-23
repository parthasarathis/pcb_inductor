
# Main function that manages the PCB inductor design process.
def main_func(tw, cl, turn, shape):
    # Get the center coordinates of the PCB inductor from user input.
    center = [float(input("Enter the x coordinate:")), float(input("Enter the y coordinate:"))]
    x = center[0]
    y = center[1]
    
    # Ask the user to select the layer of the PCB.
    ly = "F.Cu" if int(input("Select the Layer using the number \n1) Top Layer\n2) Bottom Layer\nSelect Layer: ")) == 1 else "B.Cu"
    
    # Initialize variables for net and c.
    net = 1
    c = 0  
    
    # Get the starting angle and rotation direction from the user.
    the = float(input("Enter the starting angle in degrees:"))
    rot = int(input("Enter +1 for anticlockwise, -1 for clockwise:"))
    input("Press Enter to get the coordinates...") 
    
    # Determine the shape of the inductor and call the appropriate function.
    if shape == 1:
        x, y, c = square_plot(tw, cl, turn, x, y, ly, net, c, the, rot)
    elif shape == 2:
        x, y, c = hex_plot(tw, cl, turn, x, y, ly, net, c, the, rot)
    elif shape == 3:
        oct_plot(tw, cl, turn, x, y, ly, net, c, the, rot) 

# Function to plot octagonal-shaped inductor.
def oct_plot(tw, cl, turn, x, y, ly, net, c, the, rot):
    for i in range(8 * turn):
        # Calculate the travel distance.
        travel = abs((tw + cl) / (2 * math.sin(math.radians(315))))
        u = x
        v = y
        if i % 4 == 0:
            c += 1
        
        # Adjust coordinates based on rotation direction.
        if rot == 1:
            x += travel * c * math.cos(math.radians(the) + i * math.radians(315))
        else:
            x -= travel * c * math.cos(math.radians(the) + i * math.radians(315))
        
        # Update the y-coordinate.
        y += travel * c * math.sin(math.radians(the) + i * math.radians(315))
        
        # Call function to print coordinates.
        coordinates(u, v, x, y, tw, ly, net)

# Function to plot hexagonal-shaped inductor.
def hex_plot(tw, cl, turn, x, y, ly, net, c, the, rot):
    for i in range(6 * turn):
        # Calculate travel distance.
        travel = abs(((tw + cl) / 2) / math.sin(math.radians(300)))
        u = x
        v = y
        
        # Increment c every three iterations.
        if i % 3 == 0:
            c += 1
        
        # Adjust coordinates based on rotation direction.
        if rot == 1:
            x += travel * c * math.cos(math.radians(the) + i * math.radians(300))
        else:
            x -= travel * c * math.cos(math.radians(the) + i * math.radians(300))
        
        # Update the y-coordinate.
        y += travel * c * math.sin(math.radians(the) + i * math.radians(300))
        
        # Call function to print coordinates.
        coordinates(u, v, x, y, tw, ly, net)
    
    # Return updated coordinates and c.
    return x, y, c

# Function to plot square-shaped inductor.
def square_plot(tw, cl, turn, x, y, ly, net, c, the, rot):
    for i in range(4 * turn):
        # Calculate travel distance.
        travel = abs((tw + cl) / math.sin(math.radians(270)))
        u = x
        v = y
        
        # Increment c every two iterations.
        if i % 2 == 0:
            c += 1
        
        # Adjust coordinates based on rotation direction.
        if rot == 1:
            x += travel * c * math.cos(math.radians(the) + i * math.radians(270))
        else:
            x -= travel * c * math.cos(math.radians(the) + i * math.radians(270))
        
        # Update the y-coordinate.
        y += travel * c * math.sin(math.radians(the) + i * math.radians(270))
        
        # Call function to print coordinates.
        coordinates(u, v, x, y, tw, ly, net)
    
    # Return updated coordinates and c.
    return x, y, c

# Function to print coordinates of the PCB inductor.
def coordinates(u, v, x, y, tw, ly, net):
    print("(segment(start", u, v, ")(end", x, y, ")(width", tw, ")(layer", ly, ")(net", net, "))")

# Function to calculate the inductance of the inductor.
def calc_inductance(B, a1, a2, a3, a4, a5, shape):
    """
    Calculates the inductance using given formula.
    B: Constant for specific shape.
    a1, a2, a3, a4, a5: Exponents in the formula.
    shape: Shape type for inductor.
    """
    # Get user inputs for track width, clearance, and number of turns.
    tw = float(input("Enter the track width in mm:")) * 1000
    cl = float(input("Enter the clearance in mm:")) * 1000
    turn = int(input("Enter the number of turns:"))
    
    # Calculate inner diameter and outer diameter.
    id = 2 * (tw + cl)
    od = turn * id
    Davg = (od + id) / 2
    
    print("The average diameter of the coil is", Davg, "micrometers")
    
    # Calculate inductance using given formula.
    l = B * pow(od, a1) * pow(tw, a2) * pow(Davg, a3) * pow(turn, a4) * pow(cl, a5)
    
    print("The inductance of the coil is", l, "nanohenry")
    input("Press Enter to continue...")
    
    # Call the main function with user input.
    main_func(tw / 1000, cl / 1000, turn, shape)

# Function to prompt the user to select the shape of the inductor and calculate inductance.
def get_shape():
    """
    Prompts user to select the shape and initiates inductance calculation.
    """
    x = int(input("Select shape using the number:\n1. Square\n2. Octagon\n3. Hexagon\nSelect shape:"))
    
    # Depending on the chosen shape, use corresponding constants and exponents.
    if x == 1:
        B, a1, a2, a3, a4, a5 = 1.62 * pow(10, -3), -1.21, -0.147, 2.4, 1.78, -0.03
        calc_inductance(B, a1, a2, a3, a4, a5, x)
    elif x == 2:
        B, a1, a2, a3, a4, a5 = 1.28 * pow(10, -3), -1.24, -0.174, 2.47, 1.77, -0.049
        calc_inductance(B, a1, a2, a3, a4, a5, x)
    elif x == 3:
        B, a1, a2, a3, a4, a5 = 1.33 * pow(10, -3), -1.21, -0.163, 2.43, 1.75, -0.049
        calc_inductance(B, a1, a2, a3, a4, a5, x)

# Entry point of the script, prompting the user to select the shape.
get_shape()
