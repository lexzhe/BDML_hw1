import sys

c_cur = 0
m_cur = 0
v_cur = 0

for line in sys.stdin:
    parts = line.split(' ')
    c = int(parts[0])
    m = float(parts[1])
    v = float(parts[2])
    v_cur = (c * v + c_cur * v_cur)/(c + c_cur) + c * c_cur * ((m_cur - m) / (c + c_cur)) ** 2
    m_cur = (c * m + c_cur * m_cur) / (c + c_cur)
    c_cur += c
	
f = open("reducer_result.txt", "w")
f.write(f'{c_cur} {m_cur} {v_cur}')
f.close()