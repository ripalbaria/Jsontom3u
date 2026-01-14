import json
import requests

# The specific source URL you provided
json_url = "https://raw.githubusercontent.com/ripalbaria/play/refs/heads/main/Slivtv.json"

def convert_json_to_m3u():
    try:
        response = requests.get(json_url)
        # Ensure we get the latest data
        response.raise_for_status()
        data = response.json()
        
        m3u_content = "#EXTM3U\n"
        
        # In your Slivtv.json, the data is a direct list of objects
        for item in data:
            name = item.get('channel_name', 'Unknown')
            url = item.get('stream_url', '')
            logo = item.get('logo', '')
            # If your JSON has categories/groups, add them here
            group = item.get('category', 'SlivTV')

            if url:
                # Format the M3U line correctly
                m3u_content += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
                m3u_content += f'{url}\n'

        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Success: playlist.m3u has been updated with Slivtv data.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    convert_json_to_m3u()
