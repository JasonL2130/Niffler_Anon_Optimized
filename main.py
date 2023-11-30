import pandas
import redis

from anon_generator import empi_anon
from redis_connection import get_redis_connection
from database_look_up import look_up, FieldTypes

def main():
    empi = '12490112'

    # Test EMPI's to Look-Up
    test_empi = ['OrigEMPI_21096574', 'OrigEMPI_94207264', 
                 'OrigEMPI_21096574', 'OrigEMPI_94016827', 'xyz']
    try:
        look_up(FieldTypes.EMPI, test_empi)
    except AttributeError:
        print('ERROR: Field Type Entered Is Not Defined.')

    # empi_anon(empi)

if __name__ == "__main__":
    main()