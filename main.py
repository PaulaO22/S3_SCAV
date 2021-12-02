# S3 Final exercises
from s3 import seminar3

ans = True
class_ = seminar3()
while ans:
    print("""
    1. Convert them into VP8, VP9, h265 & AV1.

    2. Create a script that will export 2 video comparision.
        For example: VP8 vs VP9 (both in same screen).
        Then choose 2 codecs of the 4 mentioned before, create the output and comment the
        differences you find there

    3.Try to achieve with FFMPEG to create a live streaming of the BBB Video. You should
        broadcast it into an IP address (locally of course) and open this IP or URL inside VLC Media Player.

    4. Create a script that let you choose the IP to broadcast the previous video

    5.Exit/Quit --> Press enter
    """)
    ans = input("What would you like to do? ")
    # Exercise 1
    if ans == "1":
        class_.ex1()

    # Exercise 2
    elif ans == "2":
        class_.ex2()

    # Exercise 3
    elif ans == "3":
        class_.ex3()

    # Exercise 4
    elif ans == "4":
        class_.ex4()
