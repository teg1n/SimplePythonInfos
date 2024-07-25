import pytube

url = input("Lütfen indirmek istediğiniz videonun url'sini giriniz: ")
path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)