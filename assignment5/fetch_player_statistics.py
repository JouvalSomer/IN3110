from bs4 import BeautifulSoup
from requesting_urls import get_html
from filter_urls import find_articles
import matplotlib.pyplot as plt
import re


def extract_teams(wiki_url):
    """Extract team names and urls from the NBA Playoff 'Bracket' section table.
    Returns:
        team_names (list): A list of team names that made it to the conference
            semifinals.
        team_urls (list): A list of absolute Wikipedia urls corresponding to team_names.
    """
    # get html using for example get_html from requesting_urls
    html = get_html(wiki_url)

    # create soup
    soup = BeautifulSoup(html, "html.parser")
    # find bracket we are interested in
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")

    # create list of teams
    team_list = []
    teams = ['Washington', 'Philadelphia', 'New York', 'Atlanta',
             'Miami', 'Brooklyn', 'Boston', 'Milwaukee',
             'Memphis', 'Utah', 'Dallas', 'LA Clippers',
             'Phoenix', 'Portland', 'Denver', 'LA Lakers']

    for i in range(1, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]

        # Filter out the cells that are empty
        cells_text = [cell for cell in cells_text if cell]
        # Find the rows that contain seeding, team name and games won
        if len(cells_text) > 1:
            for text in cells_text:
                for team in teams:
                    team_pattern = rf'(:?{team})'
                    match = re.match(team_pattern, text.strip())
                    if match:
                        team_list.append(match.group())

    team_list_semi = []
    for team in teams:
        count = team_list.count(team)
        if count >= 2:
            team_list_semi.append(team)

    urls = find_articles(html)
    team_urls = []
    team_urls = extract_url(team_list_semi, urls)

    return team_list_semi, team_urls


def extract_url(team_list_semi, url_list):
    """
        Extract team urls

        Args:
            team_list_semi (list): list of teams that made to semifinal
            url_list (list): list of urls from html string

        Returns:

        team_urls (list):
            List of all semifinal team urls
    """
    team_urls = []
    for team in team_list_semi:
        if ' ' in team:
            first, second = team.split(' ')
            ff = first[0]
            fs = second[0]
            team_pattern = rf'https:\/\/en\.wikipedia\.org\/wiki\/2020%E2%80%9321_{ff}.+{fs}.+_season.*'
            for url in url_list:
                match = re.match(team_pattern, url)
                if match:
                    team_urls.append(match.group())
        else:
            team_pattern = rf'https:\/\/en\.wikipedia\.org\/wiki\/2020%E2%80%9321_{team}.*_season.*'
            for url in url_list:
                match = re.match(team_pattern, url)
                if match:
                    team_urls.append(match.group())
    return team_urls


def extract_players(team_url):
    """
    Extract players that played for a specific team in the NBA playoffs.

    Args:
        team_url (str): URL to the Wikipedia article of the season of a given
            team.
    Returns:
        player_names (list): A list of players names corresponding to the team whos URL was passed.
            semifinals.
        player_urls (list): A list of Wikipedia URLs corresponding to
            player_names of the team whos URL was passed.
    """

    # keep base url
    base_url = "https://en.wikipedia.org"

    # get html for each page using the team url you extracted before
    html = get_html(team_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # get the header of the Roster
    roster_header = soup.find(id="Roster")
    # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # prepare lists for player names and urls
    player_names = []
    player_urls = []

    # Change implemented for the code below -------------------------------------------
    # You can find the original code commented below this change

    for i in range(0, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]
        if len(cells_text) == 7:

            name_cell = cells[2]
            name_cell = name_cell.text.strip()
            # Use e.g. regex to remove information in parenthesis following the name
            name_cell = re.sub(r'(\s\(.*\))', "", name_cell)
            player_names.append(name_cell)

            rel_url = cells[2].find_next("a").attrs["href"]

            # create urls to each player
            # need to create absolute urls combining the base and the relative url
            player_urls.append(base_url + rel_url)


    # for i in range(0, len(rows)):
    #     cells = rows[i].find_all("td")
    #     cells_text = [cell.get_text(strip=True) for cell in cells]
    #     if len(cells_text) == 7:
    #         name_pattern = r'(:?=?\w+,\s[^\(\\]+)'
    #         match = re.match(name_pattern, cells_text[2])
    #         if match:
    #             lastname, firstname = match.group().split(', ')
    #             player_names.append(firstname + ' ' + lastname)
    #         else:
    #             if match is not None:
    #                 print("NAMMMMMMEEEEEE", match.group())

    #         player_url = cells[2].find_next("a").attrs["href"]

    #         # Finds /wiki/Justin_Jackson in /wiki/Justin_Jackson_(basketball,_born_1995)
    #         if re.match(r'\/wiki\/(:?=?.+)\(', player_url):
    #             match = re.match(r'\/wiki\/?\w+_\w[^_]+', player_url)
    #             player_urls.append(base_url + match.group())

    #         # Finds /wiki/P._J._Tucker
    #         elif re.match(r'\/wiki\/\w\.\w+\.\w+', player_url):
    #             match = re.match(r'\/wiki\/\w\.\w+\.\w+', player_url)
    #             player_urls.append(base_url + match.group())

    #         # Finds everyone else
    #         else:
    #             player_urls.append(base_url + player_url)

    return player_names, player_urls


def extract_player_statistics(player_url, team_url):
    """Extract player statistics for NBA player.
    # Note: Make yourself familiar with the 2020-2021 player statistics wikipedia page and adapt the code accordingly.

    Args:
        player_url (str): URL to the Wikipedia article of a player.
        team_url (str): URL to the team

    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.
    """
    # As some players have incomplete statistics/information, you can set a default score, if you want.
    ppg = 0.0
    bpg = 0.0
    rpg = 0.0

    # get html
    html = get_html(player_url)

    # # make soup
    soup = BeautifulSoup(html, "html.parser")
    # find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")

    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")
    try:
        # find regular season header
        # You might want to check for different spellings, e.g. capitalization
        # You also want to take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season")

        # next we should identify the table
        nba_table = regular_season_header.find_next("table")

    except:
        try:
            # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")

        except:
            return ppg, bpg, rpg

    
    # find nba table header and extract rows

    # Change implemented for the code below -------------------------------------------
    # You can find the original code commented below this change

    table_header = nba_table.find_all("th") # YOUR CODE
    category_columns = [cell.get_text(strip=True) for cell in table_header]

    # find the columns for the different categories
    ppg_column = category_columns.index('PPG')
    bpg_column = category_columns.index('BPG')
    rpg_column = category_columns.index('RPG')

    # YOUR CODE HERE
    # Extract the scores from the different categories

    rows = nba_table.find_all("tr")
    for i in range(1, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]

        if('21' in cells_text[0]):
            if len(cells_text) == 13:    
                ppg = cells_text[ppg_column]
                bpg = cells_text[bpg_column]
                rpg = cells_text[rpg_column]

    scores = [ppg, bpg, rpg]
    # Convert the scores extracted to floats
    # Note: In some cases the scores are not defined but only shown as ’-’.
    # In such cases you can just set the score to zero or not defined.
    for i in range(len(scores)):
        try:
            scores[i] = float(scores[i])
        except ValueError:
            scores[i] = 0.0

    ppg = scores[0]
    bpg = scores[1]
    rpg = scores[2]

    # table_header = nba_table.find_all("th")
    # index_ppg = 0
    # index_bpg = 0
    # index_rpg = 0
    # for i, cell in enumerate(table_header):
    #     ppg_match = re.match(r'PPG', cell.text.strip())
    #     bpg_match = re.match(r'BPG', cell.text.strip())
    #     rpg_match = re.match(r'RPG', cell.text.strip())
    #     if ppg_match:
    #         index_ppg = i
    #     elif bpg_match:
    #         index_bpg = i
    #     elif rpg_match:
    #         index_rpg = i

    # table = nba_table.find_all("tr")
    # for row in table:
    #     cells = row.find_all("td")
    #     if len(cells) > 0:
    #         pattern = r'2020.+'
    #         match = re.match(pattern, cells[0].text.strip())
    #         if match:
    #             team = re.match(r'(\w+[^\\])', cells[1].text).group()
    #             if team in team_url:
    #                 ppg = float(re.match(r'(:?\.*\d+\.*\d*)',
    #                             cells[index_ppg].text.strip()).group())
    #                 bpg = float(re.match(r'(:?\.*\d+\.*\d*)',
    #                             cells[index_bpg].text.strip()).group())
    #                 rpg = float(re.match(r'(:?\.*\d+\.*\d*)',
    #                             cells[index_rpg].text.strip()).group())

    return ppg, bpg, rpg


color_table = {"Philadelphia": "#006BB6", 
                "Atlanta": "#E03A3E", 
                "Milwaukee": "#00471B",
                "Brooklyn": "#000000",
                "Utah": "#002B5C",
                "LA Clippers": "#1D428A",
                "Phoenix": "#1D1160",
                "Denver": "#FEC524"}


def plot_NBA_player_statistics(teams, plotKind):
    """Plot NBA player statistics. In this case, just PPG"""
    count_so_far = 0
    all_names = []
    plt.subplots(figsize=(20, 8.5))

    # iterate through each team and the
    for team, players in teams.items():
        # pick the color for the team, from the table above
        color = color_table[team]
        # collect the stats and name of each player on the team
        # you’ll want to repeat with other stats as well
        namesAndStats = []
        names = []
        stats = []
        for player in players:
            namesAndStats.append([player["name"], player[plotKind]])
        # record all the names, for use later in x label
        namesAndStats.sort(key=lambda x: x[1], reverse=True)

        # Take only the top 3 scores
        for i in range(3):
            names.append(namesAndStats[i][0])
            stats.append(namesAndStats[i][1])

        all_names.extend(names)
        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(names))
        count_so_far += len(names)
        # make bars for this team ’s players stats ,
        # with the team name as the label
        
        bars = plt.bar(x, stats, color=color, label=team, width=0.8)
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 45 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90) # add the legend with the colors for each team
    plt.tick_params(axis='x', labelsize=10)
    plt.legend(loc=0)

    # turn off gridlines
    plt.grid(False)
    # set the title
    plt.title("points per game") # save the figure to a file

    plt.tight_layout()
    plt.savefig("NBA_player_statistics/" + plotKind)


if __name__ == '__main__':

    wiki_url = 'https://en.wikipedia.org/wiki/2021_NBA_playoffs'


    #Change implemented for the code below -------------------------------------------
    #You can find the original code commented below this change

    teams = {}
    team_names, team_urls = extract_teams(wiki_url)

    for i in range(len(team_urls)):
        player_names, player_urls = extract_players(team_urls[i])
        players = []

        for j in range(len(player_urls)):
            player_stats = {}
            ppg, bpg, rpg = extract_player_statistics(player_urls[j], team_urls[i])
            player_stats['name'] = player_names[j]
            player_stats['ppg'] = ppg
            player_stats['bpg'] = bpg
            player_stats['rpg'] = rpg
            players.append(player_stats)
        teams[team_names[i]] = players

    plot_NBA_player_statistics(teams, "ppg")
    plot_NBA_player_statistics(teams, "bpg")
    plot_NBA_player_statistics(teams, "rpg")


    # team_list_semi, team_urls = extract_teams(wiki_url)
    # for team_url in team_urls:
    #     player_names, player_url = extract_players(team_url)
    #     for url in player_url:
    #         extract_player_statistics(url, team_url)
