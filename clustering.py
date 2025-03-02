import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_songs(df, k=4):
    features = ["danceability", "energy", "valence", "tempo"]
    df_features = df[features].copy()

    # ✅ 標準化（スケーリング）
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_features)

    # ✅ KMeans クラスタリング
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(df_scaled)

    return df, kmeans

def plot_clusters(df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=df["danceability"], y=df["energy"], hue=df["cluster"], palette="tab10")
    plt.title("KMeans Clustering of Songs")
    plt.xlabel("Danceability")
    plt.ylabel("Energy")
    plt.legend(title="Cluster")
    plt.show()
