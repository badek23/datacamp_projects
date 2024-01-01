# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Upload CSV
netflix_df = pd.read_csv("netflix_data.csv")

# Filter for only Movies
netflix_subset = netflix_df[netflix_df['type']=='Movie']

# Keep a subset of columns
netflix_movies = netflix_subset[['title','country','genre','release_year','duration']]

# Inspect shorter duration movies
short_movies = netflix_movies[netflix_movies['duration']<60]
#short_movies

# Color code each movie based on genre
def color_coding(genre):
    if genre == 'Children':
        return 'blue'
    elif genre == 'Documentaries':
        return 'red'
    elif genre == 'Stand-Up':
        return 'green'
    else:
        return 'yellow'

colors = netflix_movies["genre"].apply(color_coding)

fig = plt.figure()

x = netflix_movies['release_year']
y = netflix_movies['duration']
plt.scatter(x, y, alpha=0.60, color=colors)
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel("Duration (min)")
plt.show()