#!/bin/bash

# Array of obstacle counts
obstacle_counts=(3 5 7 10 15 20)

# Loop through the obstacle counts
for count in "${obstacle_counts[@]}"; do
    echo "Timing model with $count obstacles..."
    
    # Construct the file name based on the obstacle count
    file_name="nusmv_obstacles_${count}.smv"
    
    # Use GNU time with high precision format
    # Use GNU time with high precision format
    gtime -f "Time: %E real, %U user, %S sys" NuSMV $file_name 2> "timing_${count}.txt"

done

echo "Timing completed."
