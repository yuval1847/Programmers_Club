import threading

num = 5

def Increasing(mutexLock):
    # The function gets a mutex object.
    # The function increas the global integer num by 1.
    global num
    for i in range(100000):
        mutexLock.acquire()
        num += 1
        mutexLock.release()
            
        

def Decreasing(mutexLock):
    # The function gets a mutex object.
    # The function increas the global integer num by 1.
    global num
    for i in range(100000):
        mutexLock.acquire()
        num -= 1
        mutexLock.release()



def main():
    # The main function

    # Creating the mutex
    mutexLock = threading.Lock()

    # Creating the 2 threads 
    increasThread = threading.Thread(target=Increasing(mutexLock))
    decreasThread = threading.Thread(target=Decreasing(mutexLock))


    # Starting the threads
    increasThread.start()
    decreasThread.start()

    # Closing the threads
    increasThread.join()
    decreasThread.join()

    print(num)


if __name__ == "__main__":
    main()