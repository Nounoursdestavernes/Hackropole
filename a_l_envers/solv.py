import time
from pwn import *
from alive_progress import alive_bar

r = remote("localhost", 4000) # connection to the docker container

with alive_bar(bar=None) as bar:
    while True:
        full_text = r.recv().decode()
        if "FCSC" in full_text:
            print(full_text)
            break
        word = full_text.split(">>> ")[1].rstrip()[::-1] + "\n"
        r.send(word.encode())
        bar()
        time.sleep(0.1) # To avoid being kicked out

    