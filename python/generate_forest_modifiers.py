import os
import re

# Define the path to the history/states folder
states_folder = "D:/Dokumenty/Paradox Interactive/Hearts of Iron IV/mod/piu/history/states"

# Define the path to the forest.txt file
forest_file_path = "D:/Dokumenty/Paradox Interactive/Hearts of Iron IV/mod/piu/forest.txt"

# Read the list of forest province IDs from the forest.txt file
try:
    with open(forest_file_path, 'r', encoding='utf-8') as forest_file:
        forest_province_ids = [int(line.strip()) for line in forest_file if line.strip()]
    print(f"Loaded {len(forest_province_ids)} forest province IDs from forest.txt.")
    print(f"Forest province IDs: {forest_province_ids}")
except FileNotFoundError:
    print(f"Error: The file {forest_file_path} does not exist.")
    exit()
except ValueError:
    print(f"Error: The file {forest_file_path} contains non-numeric values.")
    exit()

# Dictionary to store province to state mapping
province_to_state = {}

# Regular expression to extract state ID and provinces
state_id_pattern = re.compile(r'id\s*=\s*(\d+)')
provinces_pattern = re.compile(r'provinces\s*=\s*{([^}]+)}')

# Iterate over each file in the history/states folder
for filename in os.listdir(states_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(states_folder, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Extract state ID
                state_id_match = state_id_pattern.search(content)
                if state_id_match:
                    state_id = int(state_id_match.group(1))
                    print(f"\nProcessing state ID {state_id} in file {filename}.")

                    # Extract provinces
                    provinces_match = provinces_pattern.search(content)
                    if provinces_match:
                        provinces = list(map(int, provinces_match.group(1).split()))
                        print(f"Found {len(provinces)} provinces in state {state_id}.")
                        print(f"Province IDs in state {state_id}: {provinces}")

                        # Map each province to the state
                        for province in provinces:
                            if province in forest_province_ids:
                                province_to_state[province] = state_id
                                print(f"MATCH: Province {province} belongs to state {state_id}.")
                    else:
                        print(f"Warning: No provinces found in state {state_id}.")
                else:
                    print(f"Warning: No state ID found in file {filename}.")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Overwrite forest.txt with the generated output
if province_to_state:
    try:
        with open(forest_file_path, 'w', encoding='utf-8') as forest_file:
            for province, state in province_to_state.items():
                forest_file.write(f"if = {{\n")
                forest_file.write(f"    limit = {{ \n")
                forest_file.write(f"        ROOT = {{ controls_province = {province} }}\n")
                forest_file.write(f"    }}\n")
                forest_file.write(f"    {state} = {{\n")
                forest_file.write(f"        add_province_modifier = {{\n")
                forest_file.write(f"            static_modifiers = {{ animate_forest }}\n")
                forest_file.write(f"            province = {{ id = {province} }}\n")
                forest_file.write(f"        }}\n")
                forest_file.write(f"    }}\n")
                forest_file.write(f"}}\n")
                forest_file.write("\n")
        print(f"\nOutput saved to {forest_file_path}.")
        print(f"Number of matches: {len(province_to_state)}")
    except Exception as e:
        print(f"Error saving output to {forest_file_path}: {e}")
else:
    print("\nNo matching provinces found.")

# Pause at the end
input("Press Enter to exit...")