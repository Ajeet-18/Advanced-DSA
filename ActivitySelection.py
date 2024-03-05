"""
Activity Selection Problem:
Read in the input as n, (L1,R1), (L2,R2),....(Ln, Rn)
Implement EITHER the Left to Right and Right to Left variants described in the video.[They are symmetrical]
Display the input and the selected activities."""

def activity_selection(n, activities, direction):
    if direction == "left_to_right":
        activities.sort(key=lambda x: x[1])  # Sort activities by finish time 
    elif direction == "right_to_left":
        activities.sort(key=lambda x: x[0], reverse=True)  # Sort activities by start time in reverse order
    else:
        return "Invalid direction"

    selected_activities = [activities[0]]
    last_activity_finish_time = activities[0][1]

    for i in range(1, n):
        if direction == "left_to_right":
            if activities[i][0] >= last_activity_finish_time:
                selected_activities.append(activities[i])
                last_activity_finish_time = activities[i][1]
        elif direction == "right_to_left":
            if activities[i][1] <= selected_activities[-1][0]:  # Compare with the finish time of the last selected activity
                selected_activities.append(activities[i])

    return selected_activities

def display_input_and_selected_activities(activities, selected_activities):
    print("Input Activities:")
    for i, activity in enumerate(activities):
        print(f"Activity {i + 1}: ({activity[0]}, {activity[1]})")
    print("\nSelected Activities:")
    for activity in selected_activities:
        print(f"({activity[0]}, {activity[1]})", end=" ")
    print()

# Predefined activities
activities = [(0,6), (3,4), (1,2), (5,9), (5,7), (8,9)]

# Left to Right variant
selected_activities_left_to_right = activity_selection(len(activities), activities, "left_to_right")

# Right to Left variant
selected_activities_right_to_left = activity_selection(len(activities), activities, "right_to_left")

# Display input and selected activities for Left to Right variant
print("Left to Right Variant:")
display_input_and_selected_activities(activities, selected_activities_left_to_right)

# Display input and selected activities for Right to Left variant
print("\nRight to Left Variant:")
display_input_and_selected_activities(activities, selected_activities_right_to_left)
