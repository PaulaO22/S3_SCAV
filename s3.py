import subprocess
class seminar3:
    def ex1(self):
        ans1 = input("Choose video size a:1280x720 , b:640×480, c:360x240 or d:160x120 ")
        ans2 = input("Choose a video codec type 1:VP8, 2:VP9, 3:h265, 4:AV1")
        #resize video
        if ans1 == "a":
            subprocess.call(
                ['ffmpeg', '-i', '1min.mp4', '-s', '1280x720', '-c:a', 'copy',
                 'resized.mp4'])
        elif ans1 == "b":
            subprocess.call(
                ['ffmpeg', '-i', '1min.mp4', '-s', '640×480', '-c:a', 'copy',
                 'resized.mp4'])
        elif ans1 == "c":
            subprocess.call(
                ['ffmpeg', '-i', '1min.mp4', '-s', '360x240', '-c:a', 'copy',
                 'resized.mp4'])
        elif ans1 == "d":
            subprocess.call(
                ['ffmpeg', '-i', '1min.mp4', '-s', '160x120', '-c:a', 'copy',
                 'resized.mp4'])
        #codec type
        if ans2 == '1':
            subprocess.call(
                ["ffmpeg", "-i", 'resized.mp4', "-c:v", "libvpx", "-b:v", "1M",
                "-c:a", "libvorbis", "vp8.webm"])
        elif ans2 == '2':
            subprocess.call(
                ["ffmpeg", "-i", 'resized.mp4', "-c:v", "libvpx-vp9", "-b:v", "1M",
                 "-c:a", "libvorbis", "vp9.webm"])
        elif ans2 == '3':
            subprocess.call(
                ["ffmpeg", "-i", 'resized.mp4', "-c:v", "libx265", "-crf", "26",
                 "-preset", "fast", "h265.mp4"])
        elif ans2 == '4':
            subprocess.call(
                ["ffmpeg", "-i", 'resized.mp4', "-c:v", "libaom-av1", "-crf", "30",
                 "-b:v", "0", "av1.mp4"])

        else:
            print("Enter a valid command")

    def ex2(self):
        # First we create a 1 minute video
        subprocess.call(
            ["ffmpeg", "-i", "vp8.webm", "-i", "vp9.webm",
             "-filter_complex", "[0][1]vstack", "compare_video.mp4"])

    def ex3(self):
        subprocess.call(['ffmpeg', '-i',  '1min.mp4',  '-f',  'mpegts', 'udp://@127.0.0.1:2222'])

    def ex4(self):
        inp = input('Enter the IP to broadcast the video')
        ip = 'udp://@' + str(inp)
        subprocess.call(['ffmpeg', '-i', '1min.mp4', '-f', 'mpegts', ip])