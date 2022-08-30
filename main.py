import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print(f'Starting {self.name} \n')
        print_time(self.name, 1, self.count)
        print(f'Exiting {self.name} \n')


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


thread1 = MyThread(1, "Thread1", 10)
thread2 = MyThread(2, "Thread2", 5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Done main thread")
