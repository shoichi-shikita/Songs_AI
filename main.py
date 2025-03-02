from get_spotify_data import fetch_spotify_data
from clustering import cluster_songs, plot_clusters
from recommend import recommend_songs

# ✅ 1. Spotifyデータを取得
playlist_id = "37i9dQZF1DXcBWIGoYBM5M"  # ここにプレイリストIDを指定
df = fetch_spotify_data(playlist_id)

# ✅ 2. クラスタリング
df, kmeans = cluster_songs(df)

# ✅ 3. クラスタごとの可視化
plot_clusters(df)

# ✅ 4. ユーザーの好みのクラスタを取得（仮でクラスタ0を選択）
target_cluster = 0
recommended_songs = recommend_songs(df, target_cluster)

# ✅ 5. 結果を表示
print("🎵 あなたへのおすすめ曲 🎵")
print(recommended_songs)
