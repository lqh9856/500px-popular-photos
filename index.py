import requests
import os

#page为页数，size为每页图片数
count = 0
url = "http://500px.me/community/discover/rating?type=json&page=1&size=100"
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
    'X-Requested-With' : 'XMLHttpRequest',
    'Connection' : 'keep-alive',
    'Referer' : 'http://500px.me/community/discover/rating',
}
photos_url = []

def get_photos_url():
    global url,headers,photos_url
    print("getting api file ...")
    json = requests.get(url,headers = headers).json()
    print("done")
    print("extract URLs ...")
    for photo in json :
        tmp = {}
        tmp['id'] = photo['id']
        tmp['url'] = photo['url']['p4']
        photos_url.append(tmp)
    print("done")

def save_photos():
    global headers,photos_url,count
    #当前目录
    dir = os.getcwd()
    #路径分隔符
    sep = os.sep
    for photo in photos_url :
        path = dir + sep + "photo" + sep
        file_path = path + photo['id'] + ".jpg"
        print("save photo " + photo['id'] + ".jpg ...")
        if not(os.path.isdir(path)) :
            os.mkdir(path)
        if os.path.isfile(file_path) :
            print("skip")
            continue
        with open(file_path,'wb') as file :
            file.write(requests.get(photo['url'],headers = headers).content)
            ++count
        print("done")

get_photos_url()
save_photos()
print("all done.\nsave " + str(count) + " photos.")


