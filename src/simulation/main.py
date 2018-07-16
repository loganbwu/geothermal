import pickle
from assets import Well, Pipe, Separator
from scipy.stats import norm

if __name__ == "__main__":
    with open('../model.pkl', 'rb') as input:
        model  = pickle.load(input)

    wells = []
    pipes = []
    separators = []

    wells.append(Well(model, norm()))
