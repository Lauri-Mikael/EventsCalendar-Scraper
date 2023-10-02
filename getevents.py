import requests
from bs4 import BeautifulSoup
from image_down import image_down
from datetime import date

def get_events():

    # Create an empty list to store the event data
    event_data = []

    number = 1

    # URL to SOUP
    url = 'https://districtfray.com/eventscalendar/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.get(url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the event listings on the page
    all_events = soup.find('div', class_='primary-events-list__container')
    event_listings = all_events.find_all('article')

    # Loop through each event listing and extract the event data
    
    for event in event_listings:
        print("Still Running")

        # Extract the event title and link
        title_holder = event.find('h4')
        title = title_holder.find('a')
        link = title_holder.find('a')['href']

        # Extract date and place
        datetime = event.find('p', class_='long-date').text.strip()
        datetime = datetime.split(' @ ')
        eventdate = datetime[0]
        eventtime = datetime[1]

        place = event.find('p', class_='venue-wrap')

        # Extract image
        image = event.find('img', class_='event-image')

        if image == None or place == None or title == None or link == None:
            continue

        place = place.text.strip()

        title = title.text.strip()

        image_url = image['src']
        image_name = image_down(image_url, number)

        if image_down == 0:
            continue
        
        number += 1
        final_data = [title, link, eventdate, eventtime, place, image_name]
        event_data.append(final_data)

    return event_data
