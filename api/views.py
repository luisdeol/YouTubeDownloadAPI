from rest_framework.decorators import api_view
from rest_framework.response import Response
from winreg import *
from bs4 import BeautifulSoup
import urllib.request
from pytube import YouTube
import os

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0] + '\\videos\\'


# Create your views here.
@api_view(['GET'])
def download_videos(request):
    url = request.GET.get('url')
    if not os.path.isdir(path):
        os.makedirs(path)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    h3s = soup.findAll("h3", class_="yt-lockup-title")
    urls = [a.find("a")["href"] for a in h3s]
    for u in urls:
        full_url = "https://www.youtube.com"+u
        yt = YouTube(full_url)
        video = yt.get('mp4', '720p')
        video.download(path)
    return Response({"status":"Ok!"})