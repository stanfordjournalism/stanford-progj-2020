"""
This script should download the list of FDIC failed
banks and generate a new file containing
just the CA banks. It should also print out
the number of failed banks in CA.

See the TODO notes below for detailed requirements
on each step of the code.

USAGE:

    python failed_banks_ca.py

"""
# TODO: IMPORT MODULES HERE

# URL TO THE FDIC BANKS DATA
url = 'https://www.fdic.gov/bank/individual/failed/banklist.csv'

# TODO: Use the requests library to fetch the FDIC data


# TODO: Use the "with" statement and "open" function,
# (you don't need to use CSV for this step) to write the file contents
# (as returned by requests) to a local file caled "banklist.csv"


# TODO: Use "with" and "open" along with the CSV module
# to read the local "banklist.csv"

    # TODO: Perform the following actions on each row of "banklist.csv"
    # - filter the data for just California banks
    # - reformat the Closing Date value in each row to YYYY-MM-DD format
    #   using the datetime module's strptime and strftime functions
    # - Save the updated data (so you can create a new file below)


# TODO: Use the "with" statement and "open" function,
# along with the CSV module, to write a new file called "failed_banks_ca.csv"
# The new file must contain the same header row and columns as the original file!


# TODO: print the sentence "There are X failed banks in CA.",
# replacing the X dynamically with a count of the CA banks.
