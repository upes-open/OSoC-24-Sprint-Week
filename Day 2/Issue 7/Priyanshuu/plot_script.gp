set title 'Sorting Algorithm Performance'
set xlabel 'Array Size'
set ylabel 'Time (seconds)'
set key outside
plot 'sorting_data.txt' using 1:2 with lines title 'Bubble Sort',                                  '' using 1:3 with lines title 'Insertion Sort',                                  '' using 1:4 with lines title 'Selection Sort',                                  '' using 1:5 with lines title 'Quick Sort'
pause -1
