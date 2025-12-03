

def exclusive_time(n: int, logs: list[str]) -> list[int]:
    stack = list()
    execution_times = [0] * n
    prev_time = 0
    for log in logs:
        id, state, timestamp = log.split(":")
        if state == "start":
            if stack:
                execution_times[stack[-1]] += int(timestamp) - prev_time
            stack.append(int(id))
            prev_time = int(timestamp)
        else:
            execution_times[stack.pop()] += int(timestamp) - prev_time + 1
            prev_time = int(timestamp) + 1
    return execution_times




if __name__ == "__main__":
    print(exclusive_time(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))
