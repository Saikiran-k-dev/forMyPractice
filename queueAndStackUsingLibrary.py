import queue

ueue = queue.Queue()
ueue.put(10)
ueue.put(20)
ueue.put(30)
sai = queue.LifoQueue()
sai.put(10)
sai.put(20)
sai.put(30)
while not(ueue.empty()):
    print(ueue.get())
while not(sai.empty()):
    print(sai.get())
