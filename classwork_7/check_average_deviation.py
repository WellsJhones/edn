import statistics


def analyze_training_log(file_path):
    times = []
    with open(file_path, 'r') as file:
        for line in file:
            if "execution_time" in line:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    try:
                        time = float(parts[1].strip())
                        times.append(time)
                    except ValueError:
                        continue
    if times:
        avg = statistics.mean(times)
        std_dev = statistics.stdev(times)
        print(f"Average: {avg:.2f} seconds")
        print(f"Standard deviation: {std_dev:.2f} seconds")
    else:
        print("No execution times found.")

# Example usage:
# analyze_training_log("training_log.txt")
