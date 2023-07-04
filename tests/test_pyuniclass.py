from pyuniclass import UT, get_table_from_code
import pandas as pd


def test_ut():
    assert UT._Ac is None
    assert UT.Ac.code == "Ac"
    assert isinstance(UT.Ac.data, pd.DataFrame)
    assert UT.get_title("Pr_65_53") == "Pump products"


class TestUniclassTables:
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
