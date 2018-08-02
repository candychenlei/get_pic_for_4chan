import requests,urllib
from pyquery import PyQuery as pq
import threading
from time import ctime,sleep
import os

threads = []
pic_urls = []

global pic_dir

pic_dir=""

base_url="http://boards.4chan.org/{0}/"


def download():
    for pic in pic_urls:
        file="http:{0}".format(pic)
        print ("downloading : {0}".format(file))
        file_name = file.split("/")[4]

        cmd="wget -P {0} {1}".format(pic_dir,file)
        #print (cmd)
        os.system(cmd)

        #open("./images/{0}".format(file_name), "wb").write(urllib.request.urlopen(file).read())

def get_pics_from_url(url):

    print (url);

    r = requests.get(url)
    html = r.text
    d = pq(r.text)
    pics = d(".fileThumb")
    for pic in pics:
        file = pic.attrib['href']
        pic_urls.append(file);
        print ("add : {0}".format(file))


def get_pic(channel):

    global pic_dir
    pic_dir="{0}/images/{1}".format(os.path.dirname(os.path.realpath(__file__)),channel)



    channel_url=base_url.format(channel)

    page_url=channel_url+"{0}"

    get_pics_from_url(channel_url)

    for num in range(2,3):
        get_pics_from_url(page_url.format(num))

    download()
    #     threads.append(threading.Thread(target=get_pics_from_url,args=(page_url.format(num))))
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()

if __name__ == '__main__':
    get_pic("diy")
