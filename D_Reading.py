def find_reading_hours(n, k, light_levels):
    min_light = float('inf')
    reading_hours = []

    # Iterate through all possible combinations of k hours
    for i in range(n - k + 1):
        hours = light_levels[i:i+k]
        max_light = max(hours)
        
        # Update the minimum light level and reading hours if found
        if max_light < min_light:
            min_light = max_light
            reading_hours = [(i+1) for i, light in enumerate(hours) if light == max_light]

    return min_light, reading_hours

# Read the input
n, k = map(int, input().split())
light_levels = list(map(int, input().split()))

# Call the function to find the reading hours
min_light, reading_hours = find_reading_hours(n, k, light_levels)

# Print the results
print(min_light)
print(' '.join(map(str, reading_hours)))