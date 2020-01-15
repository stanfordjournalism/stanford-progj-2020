# Bash drill

A basic drill for getting reps on shell commands. Instructors can prompt students with narrative and/or have them mimic the commands as they are typed.

Open a terminal.

```
# Print working directory
pwd

# Navigate to desktop
cd ~/Desktop

# Print working directory
pwd

# Create directory called bash-drill
mkdir bash-drill

# Navigate into the new directory
cd bash-drill

# Create an empty file animals.txt
touch animals.txt

# Echo "dog" to file
echo dog > animals.txt

# Print file contents to shell
cat animals.txt

# Append "bird" to animals.txt
echo bird >> animals.txt

# Append "cat" to animals.txt
echo cat >> animals.txt

# Count the lines in animals.txt
wc -l animals.txt

# Sort the words in the file
sort animals.txt

# Search the file for the word dog
grep dog animals.txt

# Sort the animals.txt and save the sorted list to animals_sorted.txt
sort animals.txt > animals_sorted.txt

# Rename animals.txt to pets.text
mv animals.txt pets.txt

# Copy animals_sorted.txt to a animals.txt
cp animals_sorted.txt animals.txt

# List the directory contents
ls

# List with file details
ls -l

# List file details in human-readable way
ls -lh

# Delete animals.txt
rm animals.txt

# List the directory contents
ls

# Navigate to the parent directory
cd ..

# Print working dir (should be on Desktop)
pwd

# List Desktop contents (should see bash-drill)
ls

# Delete the directory (this will fail)
rmdir bash-drill/

# List contents of bash-drill
ls bash-drill/

# Remove all contents of bash-drill
rm bash-drill/*

# Remove the dir
rmdir bash-drill/

# Print your env
env

# Print your env and filter the
# output for just the PATH variable
env | grep PATH
```
Explain/discuss shell environment variables
