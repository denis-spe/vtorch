import sys
sys.path.append(sys.path[0].replace("tests", ""))

import unittest
import torch
from torch import nn
from torchmodel import Sequential
from metrics import Accuracy
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
from data_generator import DataGenerator

"""
class TestSequential(unittest.TestCase):
    
    def setUp(self):
        # Create a Dataset.
"""
dataset = DataGenerator(100, 1)
print(dataset[0])
        
    
