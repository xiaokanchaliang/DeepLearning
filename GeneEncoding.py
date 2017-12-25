import numpy as np

def geneEncoding(input_size, output_size, data_size):
    result = np.empty((data_size, input_size * output_size))
    for i in range(data_size):
        temp = np.random.normal(size = (input_size, output_size))
        for m in range(input_size):
            for n in range(output_size):
                result[i][(m + 1)*(n + 1) - 1] = temp[m][n]
    return result
