import json
import requests

# Your exact source URL
json_url = "https://raw.githubusercontent.com/ripalbaria/play/refs/heads/main/Slivtv.json"

def convert_json_to_m3u():
    try:
        # Fetch the JSON
        response = requests.get(json_url, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # Initialize M3U with the header
        m3u_content = "#EXTM3U\n"
        
        count = 0
        # Iterate through the list in Slivtv.json
        for item in data:
            # Using the exact keys found in your file: 'name', 'link', 'logo'
            name = item.get('name', 'Unknown Channel')
            url = item.get('link', '')
            logo = item.get('logo', '')

            if url:
                # Adding entry to M3U format
                m3u_content += f'#EXTINF:-1 tvg-logo="{logo}" group-title="SlivTV",{name}\n'
                m3u_content += f'{url}\n'
                count += 1

        # Save to the file that your playlist link points to
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        
        print(f"Success! Processed {count} channels.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_json_to_m3u()
