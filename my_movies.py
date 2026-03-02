# Initialize and Empty List 
favorite_movies = []

# Function to add a movie to List 
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added")

# Function to remove movie from list 
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found")

# Function to display movies in list
def display_movies():
    print("Favorite Movies:")
    for movie in favorite_movies:
        print(f"- '{movie}'")

# Function to count movies in the list 
def count_movies():
    total_movies = len(favorite_movies)
    print(total_movies) 

# Function to find a movie
def find_movie(movie):
    if movie in favorite_movies:
        print(f"Found '{movie}'")
    else:
        print("Movie not found")

# Clear the list 
def clear_movies():
    favorite_movies.clear()
    print("List has been cleared")

# Adding movies 
add_movie("A League of Their Own")
add_movie("Princess and the Frog")
add_movie("Beauty and The Beast")
add_movie("I Love You, Man")
add_movie("Forgetting Sarah Marshall")
add_movie("Lord of The Rings: Fellowship of The Ring")

#Space to make it easier to read
print()

# Display List
display_movies()
print()

# Removing a movie
remove_movie("Forgetting Sarah Marshall")
print()

# Display List 
display_movies()
print()

# Count movies in list 
count_movies()
print()

# Find movie in list 
find_movie("A League of Their Own")
print()

# Clear the List 
clear_movies()
print()
display_movies()
