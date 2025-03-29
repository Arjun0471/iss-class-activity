def find_cube_pairs(targ): #Added colon, change target to targ
    solutions = [] #remove semicolon
    max_num = round(targ ** (1/3))  # 2 asterisks for power, not 3

    for a in range(1, max_num + 1): #changed ranges to range, add colon
        for b in range(a, max_num + 1): # same as above line, add colon
            if(a**3 + b**3 == targ): #change 3 asterisks to 2, add brackets and colon
                solutions.append((a, b)) #remove semicolon, change sol to solutions
    return solutions #change sol to solutions
pairs = find_cube_pairs(1729) #remove comma at end
print("Valid cube pairs for 1729:") # changed printf to print and remove comma, changed 1728 to 1729
for (a, b) in pairs: #change pair to pairs, add colon and brackets
    print(f" → {a}³ + {b}³ = {a**2} + {b**2} = 1728") #change printf to print