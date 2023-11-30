import pandas as pd
from redis_connection import get_redis_connection
from enum import Enum

# Estbalish Redis Connection
redis_conn = get_redis_connection()

# ENUM Defined to Know 'Look-Up Type
class FieldTypes(Enum):
    EMPI = 'OrigEMPI_'
    ACC = 'AnonACC_'

def look_up(field_type, orig_empis):

    type_tag = field_type.value # Used to determine Specific Pulls... alter way database is structured

    cache = {} # Dictionary to store values previous values found in specific pull
    anon_values = {}

    for i in orig_empis:
        if i in cache:                      # Search Cache... store value if found
            anon_values[i] = cache[i] # If Identical Key is Already in Anon_Values, does not add new entry... ASK HARI ABOUT LOGIC!!!
                ## HOW SHOULD I BE STRUCTURING DATABASE???
            print('Value Found in Cache!')
            print(f"Key: {i} | Anon: {cache[i]}")
        elif redis_conn.get(i):             # Search Database... store value if found and add to cache
            value_from_redis = redis_conn.get(i)
            cache[i] = value_from_redis
            anon_values[i] = value_from_redis
            print('Value Found in Database!')
            print(f"Key: {i} | Anon: {redis_conn.get(i)}")
        else:                               # Generate New Value... add to cache and database
            print('Value Not Found in Cache or Database. Generating Anonymized Value Now!')
            # Generate Anon Value

    print('')
    for key, value in anon_values.items():
        print(f"{key} -- {value}")


#################

# Overall Thought Process...
 # Three Steps
    # Check Local Cache... not there go Database, if there use it
    # Check Databse, not there = generate new one, if there use it and add to local cache


# Method calls 'look_up' and in 'look_up' call 'anon' method if not found