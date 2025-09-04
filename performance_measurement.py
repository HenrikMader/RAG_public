import subprocess
import time
import os

thread_counts = [1, 4, 8, 16, 32, 64]
output_dir = "performance_logs"
os.makedirs(output_dir, exist_ok=True)

for threads in thread_counts:
    print(f"Running converter_docling.py with {threads} threads...")
    start_time = time.time()
    
    # Run the script as a subprocess
    result = subprocess.run(
        ["python3", "converter_docling_performance.py", f"--num_threads={threads}"],
        capture_output=True,
        text=True
    )
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    # Define output file path
    output_file = os.path.join(output_dir, f"threads_{threads}.txt")
    
    # Write stdout, stderr, and elapsed time to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Execution with {threads} threads took {elapsed:.2f} seconds\n\n")
        f.write("===== STDOUT =====\n")
        f.write(result.stdout + "\n")
        f.write("===== STDERR =====\n")
        f.write(result.stderr + "\n")
    
    print(f"Logged output to {output_file}\n")
