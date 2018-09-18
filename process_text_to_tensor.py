import torch

def letterToIndex(all_letters, letter):
    return all_letters.find(letter)

def letterToTensor(all_letters, letter, n_letters):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(all_letters, letter)] = 1
    return tensor

def lineToTensor(all_letters, line, n_letters):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(all_letters, letter)] = 1
    return tensor