import re
from requesting_urls import get_html

def find_dates(html_str, output=None):
    """
    The function takes a string of html, uses regex to pars the string to find all dates of the form 
    DMY, MDY, YMD and ISO. Then it formats them as YYYY/MM/DD, and returns them

    Arguments:
        html_str:   Html string to be parsed
        output:     (optional) The name of output file the links would be stored in 

    Return:
        A list of all the dates found formated as YYYY/MM/DD. 
    """
    # Pattern for finding the months
    jan = r"\b[jJ]an(?:uar)?\b"
    feb = r"\b[fF]eb(?:ruar)?\b"
    mar = r"\b[mM]ar(?:s)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM]ay?\b"
    jun = r"\b[jJ]un(?:e)?\b"
    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA](?:ust)?\b"
    sep = r"\b[sS]ept*(?:ember)?\b"
    oct_ = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"

    months_words = rf"(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{oct_}|{nov}|{dec})"
    months_numbers = r'(?:0*[1-9]|1[0-2])'
    month_converter_list = {jan:'01', feb:'02', mar:'03', apr:'04', may:'05', jun:'06', jul:'07', aug:'08', sep:'09', oct_:'10', nov:'11', dec:'12'}

    # Pattern for finding the days
    day = r'(?:0*[1-9]|[1-2][0-9]|3[01])'

    # Pattern for finding the years
    year = r'[12]\d{3}'

    # Patterns
    DMY_pattern = rf'({day})\s({months_words})\s({year})'
    MDY_pattern = rf'({months_words})\s({day}),\s({year})'
    YMD_pattern = rf'({year})\s({months_words})\s({day})'
    ISO_pattern = rf'({year})-({months_numbers})-({day})'

    final_dates_formated = []

    # DMY: ex. 13 Oct(ober) 2020
    # Finds all the matching dates
    DMYs = re.findall(DMY_pattern, html_str)
    # Loops through the dates, example of a dmy: 13 Oct(ober) 2020
    for dmy in DMYs:
        # Loops through the dictionary month_converter_list to convert the written out month to numbers
        for letters, numbers in month_converter_list.items():
            if re.match(letters, dmy[1]):
                dmy = ' '.join(dmy)
                date = re.sub(DMY_pattern, rf"\3/{numbers}/\1", dmy)
                final_dates_formated.append(date)

    # MDY: ex. Oct(ober) 13 , 2020
    MDYs = re.findall(MDY_pattern, html_str)
    for mdy in MDYs:
        for letters, numbers in month_converter_list.items():
            if re.match(letters, mdy[1]):
                mdy = ' '.join(mdy)
                date = re.sub(MDY_pattern, rf"\3/{numbers}/\1", mdy)
                final_dates_formated.append(date)

    # YMD: ex. 2020 Oct (ober) 13
    YMDs = re.findall(YMD_pattern, html_str)
    for ymd in YMDs:
        for letters, numbers in month_converter_list.items():
            if re.match(letters, ymd[1]):
                ymd = ' '.join(ymd)
                date = re.sub(YMD_pattern, rf"\3/{numbers}/\1", ymd)
                final_dates_formated.append(date)

    # ISO: ex. 2020-10-13
    ISOs = re.findall(ISO_pattern, html_str)
    for iso in ISOs:
        date = '/'.join(iso)
        final_dates_formated.append(date)

    final_date_format_temp = []
    [final_date_format_temp.append(date) for date in final_dates_formated if date not in final_date_format_temp]
    final_date_format = final_date_format_temp

    if output != None:
        with open(f'{output}', 'w') as file:
            for date in final_date_format:
                file.write(f'{date}\n')
    else:
        return final_date_format

if __name__=='__main__':

    url1 = 'https://en.wikipedia.org/wiki/J._K._Rowling'
    url2 = 'https://en.wikipedia.org/wiki/Richard_Feynman'
    url3 = 'https://en.wikipedia.org/wiki/Hans_Rosling'

    URLs = {url1:'J._K._Rowling', url2:'Richard_Feynman', url3:'Hans_Rosling'}

    for url in URLs:
        html_str = get_html(url)
        print(html_str.decode("utf-8"))
        find_dates(html_str, output=f'collect_dates_regex/{URLs[url]}_dates.txt')

