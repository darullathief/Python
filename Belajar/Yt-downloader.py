from pytube import YouTube

#Mengambil / menerima link youtube 
link = input("Masukan Link vidio : ")
yt = YouTube(link)

#memilih resolusi
print('''Resolusi :
[1] 360p
[2] 720p
[3] 1080p''')

try: #mencegah eror ketika menginput angka
    res = int(input("Pilih Resolusi : ")) #input resolusi
    #pengecekan resolusi
    if res == 1 or res == 360:
        vid = yt.streams.get_by_itag(18)
    elif res == 2 or res == 720:
        vid = yt.streams.get_by_itag(22)
    elif res == 3 or res == 1080:
        vid = yt.streams.get_by_itag(137)

    vid.download(output_path="Downloads")

    print("Selesai")
except:
    print("Tolong masukan angka")
