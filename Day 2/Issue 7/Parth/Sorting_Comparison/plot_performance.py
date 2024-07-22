import subprocess
import matplotlib.pyplot as plt

# Compile the C program
subprocess.run(["gcc", "sorting_algorithms.c", "-o", "sorting_algorithms"])

# Run the C program and capture output
result = subprocess.run(["./sorting_algorithms"], capture_output=True, text=True)

# Parse the output to get performance metrics (time taken for each algorithm)
output_lines = result.stdout.splitlines()
bubble_sort_time = float(output_lines[0].split(': ')[1].strip().split()[0])
quick_sort_time = float(output_lines[1].split(': ')[1].strip().split()[0])
selection_sort_time = float(output_lines[2].split(': ')[1].strip().split()[0])
heap_sort_time = float(output_lines[3].split(': ')[1].strip().split()[0])
merge_sort_time = float(output_lines[4].split(': ')[1].strip().split()[0])
radix_sort_time = float(output_lines[5].split(': ')[1].strip().split()[0])

# Plotting
algorithms = ['Bubble Sort', 'Quick Sort', 'Selection Sort', 'Heap Sort', 'Merge Sort', 'Radix Sort']
times = [bubble_sort_time, quick_sort_time, selection_sort_time, heap_sort_time, merge_sort_time, radix_sort_time]

plt.figure(figsize=(12, 8))
plt.bar(algorithms, times, color=['blue', 'green', 'orange', 'red', 'purple', 'cyan'])
plt.ylabel('Time (seconds)')
plt.title('Performance of Sorting Algorithms')
plt.ylim(0, max(times) * 1.2)  # Adjust y-axis limit for better visualization
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
