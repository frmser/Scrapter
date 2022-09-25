import requests

ip = 'http://' + '192.168.137.8'
up = ip + '/up'
down = ip + '/down'
left = ip + '/left'
right = ip + '/right'


def can():
    requests.get(left)
    requests.get(down)
    requests.get(right)
    requests.get(up)


def plastic():
    requests.get(right)
    requests.get(down)
    requests.get(left)
    requests.get(up)


def plastic_bottle():
    requests.get(down)
    requests.get(up)


def smh_my_head():
    requests.get(left)
    requests.get(right)
    requests.get(right)
    requests.get(left)


def move(classification):
    if classification == 'Can':
        can()
    elif classification == 'Plastic Bottle':
        plastic_bottle()
    elif classification == 'Plastic':
        plastic()

if __name__ == '__main__':
    can()
