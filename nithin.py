import random


# To move the conveyer belt one step
def move_conveyer_belt():
    global conveyer_belt
    # Empty slot + last value excluded
    conveyer_belt = [None] + conveyer_belt[:-1]


def simulate_step():
    global products_produced, components_missed

    # Randomly generate a floating number b/w 0 and 1
    random_value = random.random()

    # Randomly add components A, B, or nothing to the beginning of the belt
    if random_value < 1 / 3:
        conveyer_belt[0] = "A"
    elif random_value < 2 / 3:
        conveyer_belt[0] = "B"

    # Check for missed components
    for component_type in components_missed.keys():
        if conveyer_belt[0] == component_type:
            # Components missed A or B is incremented here
            components_missed[component_type] += 1

    # Process components by workers
    for i in range(num_worker_pairs):
        # Iterate through the pair of workers
        left_slot = i * 2
        right_slot = i * 2 + 1

        # Check if the worker pair can assemble a product
        if conveyer_belt[left_slot] == "A" and conveyer_belt[right_slot] == "B":
            products_produced += 1
            conveyer_belt[left_slot] = conveyer_belt[right_slot] = None
        elif conveyer_belt[left_slot] == "B" and conveyer_belt[right_slot] == "A":
            products_produced += 1
            conveyer_belt[left_slot] = conveyer_belt[right_slot] = None

        # Move components on the belt
        if conveyer_belt[left_slot] is not None:
            if conveyer_belt[left_slot + 1] is None:
                conveyer_belt[left_slot + 1] = conveyer_belt[left_slot]
                conveyer_belt[left_slot] = None
        if conveyer_belt[right_slot] is not None:
            if conveyer_belt[right_slot - 1] is None:
                conveyer_belt[right_slot - 1] = conveyer_belt[right_slot]
                conveyer_belt[right_slot] = None

    move_conveyer_belt()


# Work with fixed values of worker pairs, conveyer belt length and simulation steps
num_worker_pairs = 3
conveyer_belt_length = 20
num_sim_steps = 100

# Initialize the conveyer belt with empty slots
conveyer_belt = [None] * conveyer_belt_length
products_produced = 0
components_missed = {"A": 0, "B": 0}

# Run the simulation
for _ in range(num_sim_steps):
    simulate_step()

# Printing results
print("products produced: " + str(products_produced))
print("Component A missed: " + str(components_missed['A']))
print("Component B missed: " + str(components_missed['B']))


