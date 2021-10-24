from redis import Redis

red = Redis()

red.set('py1','python1')

a = red.get('py1')
print(a)
