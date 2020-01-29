"""
This script downloads the list of FDIC failed
banks and generates a new file containing
just the CA banks. It also prints out
the number of failed banks in CA.

USAGE:

    python failed_banks_ca.py

"""
# TODO: IMPORT MODULES HERE

# URL TO THE FDIC BANKS DATA
url = 'https://www.fdic.gov/bank/individual/failed/banklist.csv'

# TODO: Use requests to fetch the FDIC data


# TODO: Use the "with" statement and "open" function,
# along with the CSV module, to write file
# contents (returned by requests)
# to a local file caled "banklist.csv"


# TODO: Use "with" and "open" to read the CSV module
# to read the local "banklist.csv"


# TODO: Perform the following actions on each row of "banklist.csv"
# - filter the data for just California banks
# - reformat the Closing Date value in each row to YYYY-MM-DD format
#   using the datetime module's strptime and strftime functions
# - Save the updated data (so you can create a new file below)


# TODO: Use the "with" statement and "open" function,
# along with the CSV module, to write a new file called failed_banks_ca.csv
# The new file must contain the same header row as the original file!


# TODO: print the sentence "There are X failed banks in CA.",
# making sure to replace the X dynamically with a count of the
# CA banks.
