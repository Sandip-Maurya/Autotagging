# File to be run by second python code

f = open('test.txt', 'r')
count_value = f'{int(f.read())+1}'
f.close()

f = open('test.txt', 'w')
f.write(count_value)
f.close()
import time
time.sleep(5)
