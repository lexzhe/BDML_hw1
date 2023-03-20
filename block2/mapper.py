import sys

chunk_size = 1000
index = 0
cur_sum = 0
cur_vals = []
for line in sys.stdin:
    index += 1
    cur_sum += int(line)
    cur_vals.append(int(line))
    if index == chunk_size:
        print(index, cur_sum / index, sum([(i - cur_sum / index) ** 2 for i in cur_vals]) / index)
        index = 0
        cur_sum = 0
        cur_vals = []
print(index, cur_sum / index, sum([(i - (cur_sum / index)) ** 2 for i in cur_vals]) / index)

