from redis_connection import get_redis_connection
import random

# Estbalish Redis Connection
redis_conn = get_redis_connection()

# Three Databases
    # Database #0 --> EMPI
    # Database #1 --> Accession

# Set Key-Value Pairs

redis_conn.select(0) # EMPI DataFrame
redis_conn.set('OrigEMPI_00000000', 'AnonEMPI_00000001')

redis_conn.select(0) # Accession DataFrame
redis_conn.set('OrigACC_11111111', 'AnonACC_11111110')

# TEST: Generate many different values in DB

for i in range(15):
    redis_conn.select(0) # EMPI DataFrame
    orig_value = random.randrange(10**7, 10**8)
    anon_value = random.randrange(10**7, 10**8)
    redis_conn.set(f'OrigEMPI_{orig_value}', f'AnonEMPI_{anon_value}')

for i in range(15):
    redis_conn.select(0) # Accession DataFrame
    orig_value = random.randrange(10**7, 10**8)
    anon_value = random.randrange(10**7, 10**8)
    redis_conn.set(f'OrigACC_{orig_value}', f'AnonACC_{orig_value}')

# Look into URI Creation


