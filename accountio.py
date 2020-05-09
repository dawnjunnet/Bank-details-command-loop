import json

# Function write_account writes the given balance and
# transaction history to an account file whose name is
# account_N.data, where N is replaced by the acctnum argument.
#
# NOTE that the account file will be created if it does not exist.
# NOTE that if the account file already exists, it will be overwritten.
#
# Arguments:
#   acctnum    An int or string representing the account number
#   balance    A float representing the current account balance
#   history    A list containing the transaction history
#
# Returns:
#   This function does not return anything.
#
# Exceptions:
#   This function will raise an exception if there is an error
#   writing to the account file.

def write_account(acctnum, balance, history):
    fname = 'account_' + str(acctnum) + '.data'
    f = open(fname, 'w')

    f.write(str(balance) + '\n')

    # Convert the history argument to a string in JSON format.
    historyline = json.dumps(history)

    f.write(historyline + '\n')
    f.close()


# Function read_account reads the account balance and
# transaction history from an account file whose name is
# account_N.data, where N is replaced by the acctnum argument.
#
# Arguments:
#   acctnum    An int or string representing the account number
#
# Returns:
#   This function returns a 2-element list:
#      - Element 0 is the account balance (as a float).
#      - Element 1 is the transaction history. It will be the same
#        kind of Python object that was passed as the history
#        argument to write_account().
#
# Exceptions:
#   This function will raise an exception if there is no account
#   file matching the given acctnum.

def read_account(acctnum):
    fname = 'account_' + str(acctnum) + '.data'
    f = open(fname, 'r')

    balance = float(f.readline().rstrip('\n'))

    historyline = f.readline().rstrip('\n')
    f.close()

    # The line we just read is in JSON format. Turn it back into
    # a Python object.
    history = json.loads(historyline)

    return [balance, history]

