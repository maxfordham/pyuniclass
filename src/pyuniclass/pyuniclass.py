import pathlib
import os
import pandas as pd

# import immutables
# frozenmap = immutables.Map

FDIR_MODULE = pathlib.Path(__file__).parent
FDIR_UNICLASS = FDIR_MODULE / "data"

if "FDIR_UNICLASS" in os.environ:
    FDIR_UNICLASS = os.environ["FDIR_UNICLASS"]


MAP_TABLE_DESCRIPTIONS = dict(  # frozenmap(
    {
        "Ac": "Activities",
        "Co": "Complexes",
        "En": "Entities",
        "SL": "Spaces/locations",
        "EF": "Elements/functions",
        "Ss": "Systems",
        "Pr": "Products",
        "TE": "Tools and Equipment",
        "PM": "Project Management",
        "FI": "Form of information",
        "Ro": "Roles",
        "Zz": "CAD",
    }
)

MAP_CODE_LENGTH = dict({"groups": 5, "subgroups": 8, "objects": 11})  # frozenmap(


def table_from_file(table_code: str) -> pd.DataFrame:
    p = list(FDIR_UNICLASS.glob(pattern=f"*{table_code}*"))[0]
    return pd.read_excel(p, header=2)


def table_description_from_code(code):
    return f"{code} - {MAP_TABLE_DESCRIPTIONS[code]}"


class UniclassTable:
    def __init__(self, code, fn_getdata=table_from_file):
        self.code = code
        self.description = table_description_from_code(code)
        self.data = fn_getdata(self.code)
        self.data["description"] = self.data["Code"] + " - " + self.data["Title"]

    @property
    def codes(self):
        return self.data.Code.to_list()

    @property
    def groups(self):
        mask = self.data["Code"].str.len() == 5
        return self.data[mask]

    @property
    def li_groups(self):
        return self.groups.description.to_list()

    def subgroups(self, code):
        mask = self.data.query(f"Code == {code}")["Code"].str.len() == 8
        return self.data[mask]


def get_table_from_code(code):
    table = code[0:2]
    if table not in MAP_TABLE_DESCRIPTIONS.keys():
        raise ValueError(
            f"{table} must be in {str(list(MAP_TABLE_DESCRIPTIONS.keys()))}"
        )
    return table


class UniclassTables:
    def __init__(self, fn_getdata=UniclassTable) -> None:
        self.fn_getdata = fn_getdata
        self._Ac = None
        self._Co = None
        self._En = None
        self._SL = None
        self._EF = None
        self._Ss = None
        self._Pr = None
        self._TE = None
        self._PM = None
        self._FI = None
        self._Ro = None
        self._Zz = None

    def getdata(self, code):
        return self.fn_getdata(code)

    def get_description(self, code):
        table = get_table_from_code(code)
        return (
            getattr(self, table).data.set_index("Code")["description"].to_dict()[code]
        )

    def get_title(self, code):
        table = get_table_from_code(code)
        return getattr(self, table).data.set_index("Code")["Title"].to_dict()[code]

    def get_code_equal(self, code):
        table = get_table_from_code(code)
        for l in getattr(self, table).codes:
            if l == code:
                return [l]
        raise ValueError(f"{code} not found in {table}")

    def get_codes_not_equals(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if l != code]

    def get_codes_contains(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if code in l]

    def get_codes_not_contains(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if code not in l]

    def get_codes_begins_with(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if l.startswith(code)]

    def get_codes_not_begins_with(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if not l.startswith(code)]

    def get_codes_ends_with(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if l.endswith(code)]

    def get_codes_not_ends_with(self, code):
        table = get_table_from_code(code)
        return [l for l in getattr(self, table).codes if not l.endswith(code)]

    # NOTE:
    # implementation below is a bit verbose but the intention is that
    # only the tables that are required get loaded in, but once loaded
    # they don't need to be reloaded...

    # --------------------------------
    @property
    def Ac(self):
        if self._Ac is None:
            self.Ac = self.getdata("Ac")

        return self._Ac

    @Ac.setter
    def Ac(self, value):
        self._Ac = value

    # --------------------------------
    @property
    def Co(self):
        if self._Co is None:
            self.Co = self.getdata("Co")
        return self._Co

    @Co.setter
    def Co(self, value):
        self._Co = value

    # --------------------------------
    @property
    def En(self):
        if self._En is None:
            self.En = self.getdata("En")
        return self._En

    @En.setter
    def En(self, value):
        self._En = value

    # --------------------------------
    @property
    def SL(self):
        if self._SL is None:
            self.SL = self.getdata("SL")
        return self._SL

    @SL.setter
    def SL(self, value):
        self._SL = value

    # --------------------------------
    @property
    def EF(self):
        if self._EF is None:
            self.EF = self.getdata("EF")
        return self._EF

    @EF.setter
    def EF(self, value):
        self._EF = value

    # --------------------------------
    @property
    def Ss(self):
        if self._Ss is None:
            self.Ss = self.getdata("Ss")
        return self._Ss

    @Ss.setter
    def Ss(self, value):
        self._Ss = value

    # --------------------------------
    @property
    def Pr(self):
        if self._Pr is None:
            self.Pr = self.getdata("Pr")
        return self._Pr

    @Pr.setter
    def Pr(self, value):
        self._Pr = value

    # --------------------------------
    @property
    def TE(self):
        if self._TE is None:
            self.TE = self.getdata("TE")
        return self._TE

    @TE.setter
    def TE(self, value):
        self._TE = value

    # --------------------------------
    @property
    def PM(self):
        if self._PM is None:
            self.PM = self.getdata("PM")
        return self._PM

    @PM.setter
    def PM(self, value):
        self._PM = value

    # --------------------------------
    @property
    def FI(self):
        if self._FI is None:
            self.FI = self.getdata("FI")
        return self._FI

    @FI.setter
    def FI(self, value):
        self._FI = value

    # --------------------------------
    @property
    def Ro(self):
        if self._Ro is None:
            self.Ro = self.getdata("Ro")
        return self._Ro

    @Ro.setter
    def Ro(self, value):
        self._Ro = value

    # --------------------------------
    @property
    def Zz(self):
        if self._Zz is None:
            self.Zz = self.getdata("Zz")
        return self._Zz

    @Zz.setter
    def Zz(self, value):
        self._Zz = value

    # --------------------------------


UT = UniclassTables()
