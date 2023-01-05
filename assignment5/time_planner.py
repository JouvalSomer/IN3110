import re
from bs4 import BeautifulSoup
from requesting_urls import get_html
import os

def extract_events(url):
    """ 
    Extract date, venue and discipline for competitions.
    
    Args:
        url (str): The url to extract events from .
    Returns:
        table_info ( list of lists ): A nested list where the rows
        represent each
        race date , and the columns are [date , venue ,
        discipline ].

    """
    disciplines = {
        "DH": " Downhill ",
        "SL": " Slalom ",
        "GS": " Giant Slalom ",
        "SG": " Super Giant Slalom ",
        "AC": " Alpine Combined ",
        "PG": " Parallel Giant Slalom "}

    # get the html
    html = get_html(url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # Find the tag that contains the Calendar header span
    calendar_header = soup.find(id="Calendar")

    # Find the following table
    calendar_table = calendar_header.find_all_next("table")[0]

    # Find the rows of the first table
    rows = calendar_table.find_all("tr")

    events = []
    for row in rows:
        cells = row.find_all("td")
        # Discards all uninteresting celles
        if len(cells) in {9, 10, 11}:
            date = cells[2].text.strip()

            if len(cells) == 11:
                venue = cells[3].text.strip()
                for cell in cells:
                    # Checks if the celles has a venue name in it
                    match = re.match(r'[A-Z]{2}', cell.text.strip())
                    if match:
                        events.append((venue, date, disciplines[match.group()]))
            else:
                for cell in cells:
                    match = re.match(r'[A-Z]{2}', cell.text.strip())
                    if match:
                        events.append((venue, date, disciplines[match.group()]))
    return events


def create_betting_slip(events, save_as):
    """ Saves a markdown format betting slip to the location
    ’./ datetime_filter /< save_as >. md ’.
    Args :
        events (list): takes a list of 3- tuples containing date, venue and type for each event
        save_as (string): filename to save the markdown betting slip as.
    """
    # ensure directory exists
    os.makedirs("datetime_filter", exist_ok = True)

    with open(f"./datetime_filter/{save_as}.md", "w") as out_file:
        out_file.write(f"#BETTING SLIP ({save_as})\n\nName:\n\n")
        out_file.write("Date | Venue | Discipline | Who wins?\n")
        out_file.write("| --- | --- | --- | --- \n")
        for e in events:
            venue, date, type = e
            out_file.write(f"| {date} | {venue} | {type} | |\n")


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/2021%E2%80%9322_FIS_Alpine_Ski_World_Cup'

    events = extract_events(url)
    save_as = 'FIS Betting sheet'
    create_betting_slip(events, save_as)
