from mpi4py import MPI
import numpy as np
import pandas as pd

from acceptance import get_sample_model
from acceptance.simulate import simulate_many

def parallel_sim():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()


    recvbuf = None
    sendbuf = None

    combi = get_sample_model()
    np.random.shuffle(combi)
    per_data_num = 3
    per_num = len(combi)//size


    simulate_n = 10000
    col = 20

    if rank == 0:
        recvbuf = np.zeros((per_data_num * len(combi), col), 
                                                dtype=np.float)
    if rank < size - 1:
        sendbuf = simulate_many(
                    combi[rank * per_num:(rank + 1)*per_num], 
                    simulate_n=simulate_n)

    if rank == size - 1 :
        sendbuf = simulate_many(
                    combi[rank * per_num:], 
                    simulate_n=simulate_n)
        print(len(combi))
        print(per_num)

    comm.Gather(sendbuf, recvbuf, root=0)
    if rank == 0:
        sim_data = pd.DataFrame(recvbuf)
        sim_data.to_csv('z.csv')

if __name__ == '__main__':
    parallel_sim()
    