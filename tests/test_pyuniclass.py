import pytest
import pandas as pd
from pyuniclass import UT


def test_ut():
    assert UT._Ac is None
    assert UT.Ac.code == "Ac"
    assert isinstance(UT.Ac.data, pd.DataFrame)
    assert UT.get_title("Pr_65_53") == "Pump products"


class TestUniclassTables:
    def test_get_code_equal(self):
        """Test that we can get the codes that equal a given code.
        Also test that if a code is not found, we raise a ValueError."""
        assert UT.get_code_equal("Pr_60_45_03") == ["Pr_60_45_03"]
        with pytest.raises(ValueError) as err:
            UT.get_code_equal("Pr_99_99_99")
        assert str(err.value) == "Pr_99_99_99 not found in Pr"

    def test_get_codes_not_equal(self):
        """With an example code, get the codes that do not equal that given code,
        and get the code that does equal that code.
        The EQUAL code should not be in the codes that DO NOT EQUAL the given code.
        """
        assert UT.get_code_equal("Pr_60_45_03") not in UT.get_codes_not_equals(
            "Pr_60_45_03"
        )

    def test_get_codes_contains(self):
        """Test that we can get the codes that contain a given code."""
        assert UT.get_codes_contains("Pr_60_45_03") == [
            "Pr_60_45_03",
            "Pr_60_45_03_12",
            "Pr_60_45_03_55",
            "Pr_60_45_03_72",
            "Pr_60_45_03_73",
            "Pr_60_45_03_78",
            "Pr_60_45_03_90",
        ]

    def test_get_codes_not_contains(self):
        """With an example code, get the codes that do not contain that given code,
        and get the codes that do contain that code.
        The codes that CONTAIN the given code should not be in the codes that DO NOT CONTAIN the given code.
        """
        assert UT.get_codes_contains("Pr_60_45_03") not in UT.get_codes_not_contains(
            "Pr_60_45_03"
        )

    def test_get_codes_begins_with(self):
        """Test that we can get the codes that begin with a given code."""
        assert UT.get_codes_begins_with("Pr_60_45_03") == [
            "Pr_60_45_03",
            "Pr_60_45_03_12",
            "Pr_60_45_03_55",
            "Pr_60_45_03_72",
            "Pr_60_45_03_73",
            "Pr_60_45_03_78",
            "Pr_60_45_03_90",
        ]

    def test_get_codes_not_begins_with(self):
        """With an example code, get the codes that do not begin with that given code,
        and get the codes that do begin with that code.
        The codes that BEGIN WITH the given code should not be in the codes that DO NOT BEGIN WITH the given code.
        """
        assert UT.get_codes_begins_with(
            "Pr_60_45_03"
        ) not in UT.get_codes_not_begins_with("Pr_60_45_03")

    def test_get_codes_ends_with(self):
        """Test that we can get the codes that end with a given code."""
        assert UT.get_codes_ends_with("Pr_60_45_03") == ["Pr_60_45_03"]

    def test_get_codes_not_ends_with(self):
        """With an example code, get the codes that do not end with that given code,
        and get the codes that do end with that code.
        The codes that END WITH the given code should not be in the codes that DO NOT END WITH the given code.
        """
        assert UT.get_codes_ends_with("Pr_60_45_03") not in UT.get_codes_not_ends_with(
            "Pr_60_45_03"
        )
