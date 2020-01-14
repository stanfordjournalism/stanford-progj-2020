#/bin/bash
# Download and wrangle some toy budget and population data.
# The script can be run by typing "sh city_budget_pops.sh".

### Step 1 - Get the Data ###

# Use curl or wget to download 3 data files.
# Below, we created shell variables to store the URLs. The
# variables can now be easily used in other commands.
# Below is a basic example (note the dollar
# sign in the reference to the variable name)
#   echo $BUDGET_2019
BUDGET_2019=https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/city_budgets_2019.xlsx
BUDGET_2020=https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/city_budgets_2020.xlsx
POPS=https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/city_pops.xlsx
echo "Downloading $BUDGET_2019"

echo "Downloading $BUDGET_2020"

echo "Downloading $POPS"

### Step 2 - Convert the Data ###
echo "Converting the data from Excel to CSV"

### Step 3 - Combine the budget files ###
echo "Combining the city budget CSVs"

### Step 4 - Merge the population data ###
echo "Merging pop. data with city budgets"

### Step 5 - Filter the data for only CA cities ###
echo "Filtering data for CA cities"

### Step 6 - Drop the state fields ###
echo "Dropping state fields from CA data"

### Step 7 - Sort the data using a csvkit utility built for sorting ###
echo "Sorting the CA data by year and amount in desdencing order"

### Step 8 - Sort the data using csvkit's utility for executing SQL on CSVs ###
echo "Sorting the CA data by year (lowest to highest) and by amount (highest to lowest)"
