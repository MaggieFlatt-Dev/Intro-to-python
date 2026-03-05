# 1. Initialize a List of Movies 
movie_collection = [
  ("She's the Man", ["Andy Fickman"] , 2006),
  ("I Love You, Man", ["John Hamburg"], 2009),
  ("Princess and The Frog", ["Ron Clements","John Musker"], 2009),
  ("The Mummy", ["Stephen Sommers"], 1999)
]

# 2. Add Movies to the Collection 
def add_movie(title, director, year):
  new_movie = (title, director, year)
  movie_collection.append(new_movie)
  for dir in director:
    print(f"Movie '{title}' directed by {dir} was added to collection.")


# 3. Display All Movies 
def display_movies():
  print("Movie Collection:")
  for movie in movie_collection:
    print(movie)

# 4. Search for Movies by Director 
def search_by_director(director):
  movies_by_director = []
  for movie in movie_collection:
    title, movie_director, year = movie
    if director.lower() in [d.lower() for d in movie_director]:
      movies_by_director.append(movie)
  return movies_by_director 

# Add movies
add_movie("Beauty & The Beast", ["Gary Trousdale", "Kirk Wise"], 1991 )
add_movie("Pride & Prejudice", ["Joe Wright"], 2005)
add_movie("Sinners", ["Ryan Coogler"], 2025)
print("-----")

# Display Movies
display_movies()
print("-----")

# Find Movies by Director 
movies_by_hamburg = search_by_director("John Hamburg")
print("Movies Directed by Hamburg:")
for title, director, year in movies_by_hamburg:
    print(f"Title: {title}, Year: {year}")
    print("-----")


# CHALLENGE 

# 1. Remove a Movie from the Collection 
def remove_movie(title):
  for movie in movie_collection:
    title_check, director, year = movie
    if title_check.lower() == title.lower():
      movie_collection.remove(movie)
      print(f"{title} has been removed from movie collection.\n") 
      return
  print(f"{title} was not found in collection")


# 2. Update Movie Information 
def update_movie(title, director, year):
  remove_movie(title)
  add_movie(title, director, year)
  print(f"{title} has been updated")

# 3. Sort Movies by Release Year


# Remove Movie from Collection
remove_movie("Beauty & The Beast")
display_movies()
print("-----")

# Update Movie
update_movie("The Mummy", ["Alex Kurtzman"], 2017)
print()
display_movies()