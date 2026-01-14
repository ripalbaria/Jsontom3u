import json
import requests

# The exact source you provided
json_url = "https://raw.githubusercontent.com/ripalbaria/play/refs/heads/main/Slivtv.json"

def convert_json_to_m3u():
    try:
        # Fetching the JSON with a timeout to prevent hanging
        response = requests.get(json_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print(f"Successfully fetched JSON. Items found: {len(data)}")
        
        m3u_content = "#EXTM3U\n"
        
        count = 0
        for item in data:
            # Using the specific keys from your Slivtv.json file
            name = item.get('channel_name')
            url = item.get('stream_url')
            logo = item.get('logo', '')
            cat = item.get('category', 'SlivTV')

            if name and url:
                m3u_content += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{cat}",{name}\n'
                m3u_content += f'{url}\n'
                count += 1

        # Write the file
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        
        print(f"Finished! Processed {count} channels into playlist.m3u")

    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    convert_json_to_m3u()
