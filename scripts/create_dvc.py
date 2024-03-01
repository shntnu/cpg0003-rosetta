import os

# Read the file paths from file_list.txt into a list
with open("file_list.txt", "r") as file:
    file_paths = [line.strip() for line in file.readlines() if line.strip()]

# drop file_paths that end with /
file_paths = [file_path for file_path in file_paths if not file_path.endswith("/")]

# filter to those that contain normalized_variable_selected
file_paths = [
    file_path for file_path in file_paths if "normalized_variable_selected" in file_path
]

# Iterate over each file path and create a .dvc file using dvc import-url
for file_path in file_paths:
    command = f"dvc import-url s3://cellpainting-gallery/{file_path} {file_path}"

    # make the directory if it doesn't exist
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    # Execute the command
    os.system(command)
