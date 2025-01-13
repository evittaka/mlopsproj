from project.data import corrupt_mnist
import torch
import os.path
import pytest

@pytest.mark.skipif(not os.path.exists('data/processed/test_images.pt'), reason = 'Data files fo not exits.')
def test_data():
    train, test = corrupt_mnist()
    assert len(train) == 30000, "Dataset did not have the correct number of samples"
    assert len(test) == 5000
    for dataset in [train, test]:
        for x, y in dataset:
            assert x.shape == (1, 28, 28)
            assert y in range(10)
    train_targets = torch.unique(train.tensors[1])
    assert (train_targets == torch.arange(0,10)).all()
    test_targets = torch.unique(test.tensors[1])
    assert (test_targets == torch.arange(0,10)).all()