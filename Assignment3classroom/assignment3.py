from mpi4py import MPI
import numpy as np

def distribute_elements(array, comm):
    n = len(array)
    local_n = n // comm.Get_size() # Compute the local size of the array
    local_array = np.empty(local_n, dtype=int) # Create an empty array to store the local elements
    comm.Scatter(array, local_array, root=0) # Scatter the elements from the root process to all processes
    local_sum = np.sum(local_array) # Compute the local sum of the elements
    return local_sum

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank() # Get the rank of the current process
    
    if rank == 0:
        array = np.array([1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12]) # Specify an array with 8 elements (divisible by 4 processes)
    else:
        array = None
    
    array = comm.bcast(array, root=0) # Broadcast the array from the root process to all processes
    local_sum = distribute_elements(array, comm) # Compute the local sum of elements for each process
    all_sums = comm.gather(local_sum, root=0) # Gather all the local sums to the root process
    
    if rank == 0:
        total_sum = np.sum(all_sums) # Compute the total sum by adding all the individual sums
        print("Total sum:", total_sum) # Print the total sum

