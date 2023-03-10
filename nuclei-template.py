import os

# Replace 'file_path' with the path to your file
file_path = 'url.txt'

# Open the file and read each line
with open(file_path, 'r') as file:
    urls = file.readlines()

# Loop through the URLs and clone each repository
for url in urls:
    # Remove whitespace and newlines from the URL
    url = url.strip()
    
    # Split the URL into parts to extract the repository name
    parts = url.split('/')
    repo_name = parts[-1].replace('.git', '')
    
    # Create a unique folder name based on the repository name
    folder_name = f'{repo_name}-{url.split("/")[-2]}'
    # Check if the folder already exists
    if os.path.exists(folder_name):
        # Change the working directory to the existing folder
        os.chdir(folder_name)
        
        # Pull the latest changes from the remote repository
        os.system('git pull')
        
        # Change the working directory back to the original directory
        os.chdir('..')
        
        # Print a message to indicate that the repository has been updated
        print(f'{repo_name} updated successfully in {folder_name}!')
    else:
        # Clone the repository into the unique folder using the 'os' module and the Git command
        os.system(f'mkdir {folder_name}')
        os.chdir(folder_name)
        os.system(f'git clone -q {url} .')
        os.chdir('..')
        
        # Print a message to indicate that the repository has been cloned
        print(f'{repo_name} cloned successfully into {folder_name}!')
