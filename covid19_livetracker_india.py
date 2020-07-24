# import all modules needed
import requests
import bs4
import plyer
import tkinter as tk


# To give request to website for the required url
def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_details_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    # print(html_data.text)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    # print(bs.prettify())
    info_div = bs.find("div", class_="site-stats-count").find("ul").find_all("li")[0:4]
    # print(info_div)
    all_details = ""
    for item in info_div:
        count = item.find("strong").get_text()
        data_text = item.find("span").get_text()
        all_details = all_details + data_text + ":" + count + "\n"

    return all_details


def main():
    print(get_corona_details_india())


if __name__ == '__main__':
    main()

window = tk.Tk()
window.geometry("500x500")
window.title("CORONA_LIVE_TRACKER_INDIA")
window.config(background="yellow")

# image label for window
img = tk.PhotoImage(file='coronavirus.png')
image_label = tk.Label(window, image=img, background="powder blue").pack()

# for live data

content_label = tk.Label(window, text=get_corona_details_india(),font=("Arial", 18, "bold"),
                         background="powder blue")
content_label.pack()

window.mainloop()
