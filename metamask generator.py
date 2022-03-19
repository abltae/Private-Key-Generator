import secrets
import time
import threading

start = time.perf_counter()

account_amount = input("How many Metamask Accounts do you want?: ")

def generate():
    priv_key = "0x" + secrets.token_hex(32)
    print(priv_key)

threads = []

for i in range(int(account_amount)):
    t = threading.Thread(target=generate)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
finish = time.perf_counter()
print(f'Completed in {round(finish-start,2)} seconds')