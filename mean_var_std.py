import numpy as np

def mean(data):
    axis1 = list(np.mean(data, axis=0))
    axis2 = list(np.mean(data, axis=1))
    flattened = np.mean(data.flatten())
    return [axis1, axis2, flattened]
    

def variance(data):
    axis1 = list(np.var(data, axis=0))
    axis2 = list(np.var(data, axis=1))
    flattened = np.var(data.flatten())
    return [axis1, axis2, flattened]


def std(data):
    axis1 = list(np.std(data, axis=0))
    axis2 = list(np.std(data, axis=1))
    flattened = np.std(data.flatten())
    return [axis1, axis2, flattened]

def amax(data):
    axis1 = list(np.amax(data, axis=0))
    axis2 = list(np.amax(data, axis=1))
    flattened = np.amax(data.flatten())
    return [axis1, axis2, flattened]


def amin(data):
    axis1 = list(np.amin(data, axis=0))
    axis2 = list(np.amin(data, axis=1))
    flattened = np.amin(data.flatten())
    return [axis1, axis2, flattened]

def sum_(data):
    axis1 = list(np.sum(data, axis=0))
    axis2 = list(np.sum(data, axis=1))
    flattened = np.sum(data.flatten())
    return [axis1, axis2, flattened]


def calculate(list):
    try:
      output = {}
      arr = np.reshape(np.array(list), (3,3))
      output['mean'] = mean(arr)
      output['variance'] = variance(arr)
      output['standard deviation'] = std(arr)
      output['max'] = amax(arr)
      output['min'] = amin(arr)
      output['sum'] = sum_(arr)
      return output
    except ValueError:
      raise ValueError("List must contain nine numbers.")