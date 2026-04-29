import os
import json
import time
import statistics
import subprocess


BASIC_LOG = "profiler_logs/basic_logs.jsonl"
OPT_LOG = "profiler_logs/optimized_logs.jsonl"
INPUT_FILE = "../tests/sample.py"

os.makedirs("profiler_logs", exist_ok=True)


if os.path.exists(BASIC_LOG):
    os.remove(BASIC_LOG)

basic_times = []
for i in range(5):
    start = time.perf_counter()
    subprocess.run(["python3", "basic.py", "--source", INPUT_FILE],cwd="client",check=True)
    end = time.perf_counter()
    ms = (end - start) * 1000
    basic_times.append(ms)
basic_rows = []



with open(BASIC_LOG, "r", encoding="utf-8") as f:
    for line in f:
        basic_rows.append(json.loads(line))
basic_payload_in = 0
basic_payload_out = 0
for row in basic_rows:
    basic_payload_in += row["payload_in_bytes"]
    basic_payload_out += row["payload_out_bytes"]
basic_total_data = basic_payload_in + basic_payload_out



if os.path.exists(OPT_LOG):
    os.remove(OPT_LOG)

opt_times = []
for i in range(5):
    start = time.perf_counter()
    subprocess.run(["python3", "optimized.py", "--source", INPUT_FILE],cwd="client",check=True)
    end = time.perf_counter()
    ms = (end - start) * 1000
    opt_times.append(ms)



opt_rows = []
with open(OPT_LOG, "r", encoding="utf-8") as f:
    for line in f:
        opt_rows.append(json.loads(line))


opt_payload_in = 0
opt_payload_out = 0
for row in opt_rows:
    opt_payload_in += row["payload_in_bytes"]
    opt_payload_out += row["payload_out_bytes"]

opt_total_data =opt_payload_in + opt_payload_out




print("======================================= FINAL RESULTS ==================================")

print("Basic latency mean:", statistics.mean(basic_times))
print("Basic latency std:", statistics.pstdev(basic_times))
print("Basic RPC count:", len(basic_rows))
print("Basic total data transferred:",basic_total_data)
print("Optimized latency mean:", statistics.mean(opt_times))
print("Optimized latency std:", statistics.pstdev(opt_times))
print("Optimized RPC count:", len(opt_rows))
print("Optimized total data transferred:", opt_total_data)


print("======================================= FINAL RESULTS ==================================")