import time
import sys



def animation(length):
    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    # noinspection PyShadowingNames
    animation = ["10% [■□□□□□□□□□]", "20% [■■□□□□□□□□]", "30% [■■■□□□□□□□]", "40% [■■■■□□□□□□]", "50% [■■■■■□□□□□]",
                 "60% [■■■■■■□□□□]", "70% [■■■■■■■□□□]", "80% [■■■■■■■■□□]", "90% [■■■■■■■■■□]", "100% [■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(length)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
