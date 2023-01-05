import re 
from requesting_urls import get_html

def find_urls(html_str, base_url=None, output=None):
    """
    The function takes a html string and returns all valid URLs within that string.
    Valid URLs are url with <a> tag.

    Arguments:
        html_str:   Html string to be parsed
        base_url:   (optional) The base URL from wich the html string is taken from
        output:     (optional) The name of output file the links would be stored in 

    Return:
        A list of all the valid URLs in the parsed html string
    """

    # Pattern to fint all urls following herf= inside articles
    regex = r'<a\s.*?href=\"([^\"\#]+)\"'
    possible_links = re.findall(regex, html_str)

    for i, link in enumerate(possible_links):
        if link[:2] == '//':
            possible_links[i] = 'https:' + link

        elif link[:2] == '/w':
            if base_url is None:
                base_url_regex = r'https:\/\/[^\.]+\.wikipedia\.org'
                base = re.findall(base_url_regex, html_str)[0]
                possible_links[i] = base + link

            elif base_url is not None:
                possible_links[i] = base_url + link
    
    filtered_links = []
    for link in possible_links:
        if link[0] == 'h':
            if re.match(r'https:.+:', link):
                if re.match(r'https:.+http:', link):
                    filtered_links.append(link)
                else:
                    continue
            else:
                filtered_links.append(link)

    # Makes sure links only appears once in the list
    links_temp = []
    [links_temp.append(link) for link in filtered_links if link not in links_temp]
    filtered_links = links_temp

    ## Return ##
    # Writes the links to a file
    if output is not None:
        with open(output, 'w') as file:
            for link in filtered_links:
                file.write(link + "\n")
    # Returns the links
    else:
        return filtered_links


def find_articles(html_str, output=None):
    """ 
    The function takes a html string, uses the find_urls function to get a lit of urls,
    loops through those, and select the urls that are wikipedia articles

        Arguments:
            html_str:   Html string to be parsed
            output:     (optional) The name of output file the links would be stored in   
        Return:
            A list of wikipedia articles
    """
    urls = find_urls(html_str)
    articles = []
    for url in urls:
        if re.match(r'https:\/\/[^\.]+\.wikipedia\.org.+', url):
            articles.append(url)
   
   ## Return ##
    # Writes the links to a file
    if output is not None:
        with open(output, 'w') as file:
            for article in articles:
                file.write(article + "\n")
    # Returns the links
    else:
        return articles


if __name__=='__main__':

    url1 = "https://en.wikipedia.org/wiki/Nobel_Prize"
    url2 = "https://en.wikipedia.org/wiki/Bundesliga"
    url3 = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"

    URL = {url1:'Nobel_Prize', url2:'Bundesliga', url3:'FIS_Alpine_Ski_World_Cup'}

    for url in URL:
        html_str = get_html(url)
        # list_of_urls = find_urls(html_str, base_url=None, output=f'filter_urls/{URL[url]}.txt')
        find_articles(html_str, output=f'filter_urls/{URL[url]}_articles.txt')
