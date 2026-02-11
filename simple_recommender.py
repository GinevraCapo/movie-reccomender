import pandas as pd

# 1. Create a dummy dataset of movie ratings
data = {
    'user_id': [1, 2, 3, 1, 2, 3, 1, 2, 4],
    'movie_title': ['Star Wars', 'Star Wars', 'Star Wars', 'Titanic', 'Titanic', 'Avengers', 'Avengers', 'Avengers', 'Avengers'],
    'rating': [5, 4, 5, 2, 1, 5, 4, 4, 5]
}

df = pd.DataFrame(data)

# 2. Calculate the most popular movies (highest average rating)
recommendations = df.groupby('movie_title')['rating'].mean().sort_values(ascending=False)

print("Top Recommended Movies Based on Average Rating:")
print(recommendations)
# 3. Get the top 2 recommended movies
top_recommendations = recommendations.head(2)
print("\nTop 2 Recommended Movies:")
print(top_recommendations)
# 4. Get the top 2 recommended movies for a specific user (e.g., user_id = 1)
user_recommendations = df[df['user_id'] == 1].groupby('movie_title')['rating'].mean().sort_values(ascending=False).head(2)
print("\nTop 2 Recommended Movies for User 1:")
print(user_recommendations)
# 5. Get the top 2 recommended movies for a specific user (e.g., user_id = 2)
user_recommendations_2 = df[df['user_id'] == 2].groupby('movie_title')['rating'].mean().sort_values(ascending=False).head(2)
print("\nTop 2 Recommended Movies for User 2:")
print(user_recommendations_2)
# 6. Get the top 2 recommended movies for a specific user (e.g., user_id = 3)
user_recommendations_3 = df[df['user_id'] == 3].groupby('movie_title')['rating'].mean().sort_values(ascending=False).head(2)
print("\nTop 2 Recommended Movies for User 3:")
print(user_recommendations_3)
# 7. Get the top 2 recommended movies for a specific user (e.g., user_id = 4)
user_recommendations_4 = df[df['user_id'] == 4].groupby('movie_title')['rating'].mean().sort_values(ascending=False).head