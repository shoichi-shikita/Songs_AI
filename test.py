import requests

access_token ="BQA6RCp6FVDCphqUR0PcG4b5nOmMaAlljHdWLFAq7n8oW6JvVepDWNkgLR_QxjY9ShLspWlKUsvZ_Mjj4UdM2cha650Jo_DIxe2-Fq9xH_hO4tAp51Lxa3nN0hbASLv6jG0Aew_UI7-EUbAbk0CwJa0T5d7HA_dyxoCnXm72dMCBhMrL7tlTYCET_SNgjbcFHHWZ-KuX1zEbPmwRiNbyDMStVh08k05OVFQAwgsEIlljkEwMbtnJ2XJySpW5jpNnNcTzrNtB8TszQQ28XXI"
track_id = "24yjeET9kkN8mQMHLBdSoV"  # 1曲だけを指定

headers = {
    "Authorization": f"Bearer {access_token}"
}
url = f"https://api.spotify.com/v1/audio-features/{track_id}"

response = requests.get(url, headers=headers)

print(f"HTTP Status Code: {response.status_code}")
print("Response JSON:", response.json())

import time

token_expiry = 1740894124  # 取得したトークンの有効期限（UNIX時間）
current_time = int(time.time())

if current_time > token_expiry:
    print("⚠️ アクセストークンが期限切れです！更新してください。")
else:
    print("✅ トークンはまだ有効です。")
