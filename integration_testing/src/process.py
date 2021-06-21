""" Data Processing Runner """

from typing import Tuple, Union

import numpy as np

from sklearn.datasets import make_blobs
from sklearn.metrics.pairwise import euclidean_distances


def make_dataset(
    n_samples: int, centers: int, n_features: int, random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """Pure wrapper for sklearn make_blobs.

    For this example, re-wrap make_blobs to output a tuple.

    Args:
        n_samples (int): number samples to output
        centers (int): number of blobs to output
        n_features (int): nubmer of 'columns'
        random_state (int, optional): set numpy random seed for reproducibility. Defaults to 42.

    Returns:
        Tuple: (X, y) numpy arrays of X=data and y=target class (centroid)
    """

    dataset = make_blobs(n_samples, centers, n_features, random_state)

    return dataset


def remove_outliers(dataset, stdev: Union[int, float]):
    """Remove datapoints at or greater than provided stdev threshold.

    Euclidian distance is used.

    Args:
        dataset (X,y): Any classification dataset
        stdev (int, float): stdev threshold from class centroid to remove

    Returns:
        cleaned_dataset: dataset with all outliers removed
    """

    # determine centroid of each class
    labels = set(dataset[1])
    centroids = {cls: None for cls in labels}
    for k, v in centroids:
        pass

    raise NotImplementedError