import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# ✅ Spotify API 認証情報
CLIENT_ID = "32219c3f409a46e8969451e5330cd1f9"
CLIENT_SECRET = "ea0e77ed1b3e45e2b10eb37883f36f77"
REDIRECT_URI = "http://127.0.0.1:8888/callback"


# ✅ SpotifyOAuth のスコープ修正
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope="playlist-read-private user-library-read user-read-private user-read-playback-state user-top-read",
                                                show_dialog=True))

token_info = sp.auth_manager.get_access_token(as_dict=True)
print("✅ アクセストークン:", token_info.get("access_token", "取得できませんでした"))
print("⏳ トークン有効期限:", token_info.get("expires_at", "不明"))

token_info = sp.auth_manager.get_access_token(as_dict=True)
print("✅ 現在のスコープ:", token_info.get("scope", "スコープ情報なし"))
# ✅ プレイリストID
playlist_id = "5dr9EzIk0hDx734FpQmEi4"

# ✅ プレイリストの曲情報を取得
def get_playlist_tracks(playlist_id):
    try:
        results = sp.playlist_tracks(playlist_id)
        print("✅ APIリクエスト成功！")
        tracks = results['items']
    except spotipy.exceptions.SpotifyException as e:
        print(f"🚨 APIリクエストエラー: {e}")
        return [], []

    track_list = []
    track_ids = []
    
    for track in tracks:
        track_data = track['track']
        if track_data and 'id' in track_data:
            track_list.append({
                'name': track_data['name'],
                'artist': track_data['artists'][0]['name'],
                'id': track_data['id']
            })
            track_ids.append(track_data['id'])

    print(f"✅ 取得した曲数: {len(track_list)}")
    print(f"✅ 取得した曲IDリスト: {track_ids}")

    return track_list, track_ids

# ✅ 曲の特徴量を取得（100曲ずつリクエスト）
def get_audio_features(track_ids):
    feature_list = []

    for i in range(0, len(track_ids), 100):  # ✅ 100曲ずつ処理
        batch = track_ids[i:i+100]
        try:
            features = sp.audio_features(batch)
            if features:
                for feature in features:
                    if feature and feature.get('id'):  # ✅ Noneチェック
                        feature_list.append({
                            'id': feature['id'],
                            'danceability': feature['danceability'],
                            'energy': feature['energy'],
                            'valence': feature['valence'],
                            'tempo': feature['tempo']
                        })
        except spotipy.exceptions.SpotifyException as e:
            print(f"🚨 APIリクエストエラー: {e}")

    return feature_list

# ✅ データ取得
track_data, track_ids = get_playlist_tracks(playlist_id)
audio_features = get_audio_features(track_ids)

# ✅ DataFrameに変換
df_tracks = pd.DataFrame(track_data)
df_features = pd.DataFrame(audio_features)

# ✅ データが取得できたか確認
if df_features.empty:
    print("🚨 特徴量データが取得できませんでした。APIのスコープを確認してください！")
else:
    # ✅ 曲情報 + 特徴量を結合
    df = df_tracks.merge(df_features, on="id")
