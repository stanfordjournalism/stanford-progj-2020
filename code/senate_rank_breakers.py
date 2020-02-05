"""
A script to find senators most likely to break
ranks on impeachment votes.

We use the ProPublica Congress Members API
to find senators most likely to vote
against their own party.


USAGE:

From the command-line:

    python senate_rank_breakers.py

OUTPUT:

    A list of top 5 most likely to break ranks
    from each major party.

"""
import os
import requests


# The entry point for our script, which calls
# other functions defined below. The "main" function
# is also commonly placed at the end the script, but
# I like putting it at the top to improve readability.
# See the bottom of the script for a common
# Python "idiom" for invoking the "main" function.
def main():
    api_key = os.environ["PROPUBLICA_API_KEY"]
    members = get_members(api_key)
    # TODO: invoke the other functions
    # you create to download, sort candidates
    # based on how often they vote against their
    # party, and print the top 5 (aka most likely
    # to vote against party) for Democrats and Republicansk

### TASK-SPECIFIC FUNCTIONS GO HERE ###



# Use the standard convention for triggering
# the "main" function when the script is
# invoked on the command line:
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    main()
