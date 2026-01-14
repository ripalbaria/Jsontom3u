import json
import requests

# URL of your JSON file
json_url = "https://raw.githubusercontent.com/ripalbaria/play/refs/heads/main/Slivtv.json"

def convert_json_to_m3u():
    try:
        response = requests.get(json_url)
        data = response.json()
        
        # Start M3U file content
        m3u_content = "#EXTM3U\n"
        
        # Access the list (adjust 'channels' if your JSON uses a different key)
        channels = data.get('channels', data) if isinstance(data, dict) else data

        for item in channels:
            name = item.get('name', 'Unknown')
            url = item.get('url', '')
            logo = item.get('logo', '')
            group = item.get('group', 'Default')

            if url:
                m3u_content += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
                m3u_content += f'{url}\n'

        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("M3U playlist generated successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_json_to_m3u()

