import requests
import os

def image_down(url, number):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(url, headers=headers)

        response.raise_for_status()  # Raise an exception if the response status code is not 200

        image_data = response.content

        os.makedirs("EventsCalendar", exist_ok=True)

        location = f'EventsCalendar_image_{number}.jpg'

        with open(f'EventsCalendar/{location}', 'wb') as f:
            f.write(image_data)

        return location

    except requests.exceptions.RequestException as e:
        # print(f"An error occurred while downloading the image: {e}")
        return 0

    except IOError as e:
        # print(f"An error occurred while writing the image file: {e}")
        return 0

    except Exception as e:
        # print(f"An unexpected error occurred: {e}")
        return 0

    return location
        
