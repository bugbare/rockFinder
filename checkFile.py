import torch
x = torch.rand(5, 3)
print(x)
print(f'\n\n\tIs Cuda available ---> {torch.cuda.is_available()}')
