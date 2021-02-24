"""
Round-Robin principle example
"""

from time import sleep

#task queue
queue = []

#generator counting numbers
def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield 
        sleep(0.5)

#generator that print bang every 3 secons
def print_bang():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Bang!')
        counter += 1
        yield
        sleep(0.5)

#even loop 
def main():
    #endless loop
    while True:
        #getting the value from the first task
        g = queue.pop(0)
        next(g)
        #appending said task to the end of the queue
        queue.append(g)


if __name__ == '__main__':
    #initializing geners and adding them to a loop
    g1 = counter()
    queue.append(g1)
    g2 = print_bang()
    queue.append(g2)
    main()