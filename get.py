import requests,urllib
from pyquery import PyQuery as pq

base_url="http://boards.4chan.org/{0}/"

def download(file):
    file="http:{0}".format(file)
    print (file)
    file_name = file.split("/")[4]
    open("./images/{0}".format(file_name), "wb").write(urllib.request.urlopen(file).read())

def get_pics_from_url(url):

    print (url);

    r = requests.get(url)
    html = r.text
    d = pq(r.text)
    pics = d(".fileThumb")
    for pic in pics:
        file = pic.attrib['href']
        download(file)
    #fileThumb

def get_pic(channel):

    channel_url=base_url.format(channel)

    page_url=channel_url+"{0}"

    get_pics_from_url(channel_url)

    for num in range(2,11):
        get_pics_from_url(page_url.format(num))


if __name__ == '__main__':
    get_pic("diy")
