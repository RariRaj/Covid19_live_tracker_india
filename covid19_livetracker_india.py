# import all modules needed
import requests
import bs4
import plyer

#To give request to website for the required url
def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_details_india():
    url="https://www.mohfw.gov.in/"
    html_data=get_html_data(url)
    #print(html_data.text)




def main():
    get_corona_details_india()


if __name__ == '__main__':
    main()





