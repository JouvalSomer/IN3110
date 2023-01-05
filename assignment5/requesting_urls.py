import requests as req

def get_html(url, params=None, output=None):
    """ 
    The function take a url and some optional arguments, params and output, and returns the url and its content

    Arguments:
        url: The url of the websight one wants to inspect
        params: Optional argument. A dictionary of strings of keys and coresponding values
        output: Optional argument. The name of the output file
    
    return:
        If output is given the function writes the url and it's content to the given file.
        If output is not given the functions simply returns url and it's content
    """

    response = req.get(url, params=params)

    assert response.status_code == 200, f'The request was unsuccesfull, status code = {response.status_code}.'

    if output is not None:
        with open(output, 'w') as file:
            file.write("url:" + url + "\n")
            file.write(response.text)
    else:
        return response.text


if __name__ == '__main__':

    url1 = "https://en.wikipedia.org/wiki/Studio_Ghibli"
    url2 = "https://en.wikipedia.org/wiki/Star_Wars"
    url3 = "https://en.wikipedia.org/w/index.php"

    params = {'title': 'Main_Page', 'action': 'info'}

    get_html(url1, params=None, output="requesting_urls/Studio_Ghibli.txt")
    get_html(url2, params=None, output="requesting_urls/Star_Wars.txt")
    get_html(url3, params=params, output="requesting_urls/index.txt")