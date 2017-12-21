

def spinlock(step_size):
    ring = [0]

    val = 1
    curr_idx = 0

    while val <= 2017:
        ring.insert((curr_idx + step_size) % len(ring) + 1, val)

        curr_idx = ring.index(val)

        val += 1

    return ring


def spinlock_opt(step_size):
    curr_idx = 0
    for i in range(1, 50000000+1):
        curr_idx = (curr_idx + step_size) % i + 1
        if curr_idx == 1:
            val_after_zero = i
    return val_after_zero


ring_buff = spinlock(349)

print("Part 1:", ring_buff[ring_buff.index(2017) + 1])
print("Part 2:", spinlock_opt(349))

