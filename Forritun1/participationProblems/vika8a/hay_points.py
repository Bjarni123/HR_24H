# taking in n and m. which are the number of haypoints and job description
number_of_haypoints, number_of_job_descriptions = map(int, input().split())

# Create the dictionary for haypoints
haypoints_dict = dict()

# take in the haypoint key and value and put it in a dictionary
for x in range(number_of_haypoints):
    haypoint_key, haypoint_value = input().split()
    haypoints_dict[haypoint_key] = int(haypoint_value)

# Create the sums list with as many 0 as there are job descriptions
the_sums = [0 for x in range(number_of_job_descriptions)]

# loop over how many job descriptions there are
for x in range(number_of_job_descriptions):
    # Create an empty string to loop over the loop atleast once (do-while loop)
    the_input = ''

    while the_input != '.':
        # Split the input into words seperated by space
        for word in the_input.split():
            # an if the word is in the haypoint dict, We add the value to the sum.
            if word in haypoints_dict:
                the_sums[x] += haypoints_dict[word]
        
        the_input = input()

# Print the sums
for x in the_sums:
    print(x)