import time


def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = f'{minutes}:{seconds}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print('The wait is Over')


t = input('Input your time in Seconds: ')
countdown(int(t))
