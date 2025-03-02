import pandas as pd
from sklearn.neighbors import NearestNeighbors

def recommend_songs(df, target_cluster, num_recommendations=5):
    """
    指定したクラスタの中からランダムに曲を推薦
    """
    recommendations = df[df["cluster"] == target_cluster].sample(n=num_recommendations, replace=True)
    return recommendations[["name", "artist"]]

