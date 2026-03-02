planet_list = ["Mercury", "Mars"]
planets = ["Neptune", "Uranus"]

# Display Planets
def display_planets():
    print("Planets:")
    for planet in planet_list:
        print(f"- {planet}")

# Use append() to add Jupiter and Saturn to the end of the list
def add_planet(planet):
    planet_list.append(planet)
    print(f"{planet} added")


# Display Planet List
display_planets()
print()

# Add planets
add_planet("Jupiter")
add_planet("Saturn")
print()
display_planets()

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
print()
planet_list.extend(planets)
display_planets()

# Use insert() to add Earth, and Venus in the correct order.
print()
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
display_planets()

# Use append() again to add Pluto to the end of the list.
print()
planet_list.append("Pluto")
display_planets()

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets. 
print()
rocky_planets = planet_list[0:4]
print(f"Rocky Planets = {rocky_planets}")

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
print()
del planet_list[8]
display_planets()