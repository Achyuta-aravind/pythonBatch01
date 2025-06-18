print("AI alerting system")

memory = 1024 #In gb

memory_resources = 0

name = None

threshold_limit = 512

while memory_resources < memory:
    memory_resources += 1
    if memory_resources == threshold_limit:
        print("Memory resources half exceeded check the processes")
        continue
    print(memory_resources)