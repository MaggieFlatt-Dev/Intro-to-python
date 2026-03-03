planet_list = ["Mercury", "Mars"]
planets = ["Neptune", "Uranus"]
# CHALLENGE:
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.
spacecraft_list = [
    ("Mariner 10", "Mercury", "Venus"),
    ("MESSENGER", "Mercury", "Venus"),
    ("Venera 1-16", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Pioneer Venus 1 and 2", "Venus"),
    ("Vega 1 and 2", "Venus"),
    ("Magellan", "Venus"),
    ("Venus Express", "Venus"),
    ("Parker Solar Probe", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 6 and 7", "Mars"),
    ("Mariner 9", "Mars"),
    ("Viking 1 and 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("InSight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10 and 11", "Jupiter"),
    ("Voyager 1 and 2", "Jupiter", "Saturn", "Uranus", "Neptune"),
    ("Ulysses", "Jupiter"),
    ("Galileo", "Venus", "Jupiter"),
    ("Cassini", "Venus", "Jupiter", "Saturn"),
    ("New Horizons", "Jupiter", "Pluto"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Jupiter", "Saturn"),
]


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


# CHALLENGE
# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.

for spacecraft in spacecraft_list:
    spacecraft_name, *planets = spacecraft
    print()
    print(f"{spacecraft_name} has visited")
    print("---------------------")
    for planet in planets:
      print(f"{planet}")
