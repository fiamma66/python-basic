from pytube import YouTube

url = "https://www.youtube.com/watch?v=aWBtpBwzzdM&list=PL3g0NG84hZuCF1R68_77mnhPH11x_3sFy&t=0s&index=2"
yt = YouTube(url)
(yt.streams
   .filter(progressive=True, file_extension='mp4')
   .order_by('resolution')
   .desc()
   .first()
   .download())



