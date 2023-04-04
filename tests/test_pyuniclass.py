from pyuniclass import UT
import pandas as pd

def test_ut():
    assert UT._Ac is None
    assert UT.Ac.code == "Ac"
    assert isinstance(UT.Ac.data, pd.DataFrame)