"""Module providing a function printing python version and cuda"""
import sys
import torch


def print_python_version():
    """Function printing python version."""
    print(f"\npython version is {sys.version}\n")
    
def print_cuda_status():
    """Function printing cuda status."""
    x = torch.rand(5, 3)
    print(f"\n{x}")
    print(f'\nIs Cuda available ---> {torch.cuda.is_available()}')

print_python_version()
print_cuda_status()
