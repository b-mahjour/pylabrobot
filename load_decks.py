from pylabrobot.resources import (
    MP_3Pos_Flat,
    Well,
    Coordinate,
    create_equally_spaced,
    TecanPlateCarrier,
    create_homogeneous_carrier_sites
)
from pylabrobot.resources.tecan.plates import (
    Microplate_96_Well,
    TecanPlate
)
from pylabrobot.resources.tecan.tecan_decks import (
    TecanDeck,
    EVO200_NUM_RAILS,
    EVO200_SIZE_X,
    EVO200_SIZE_Y,
    EVO200_SIZE_Z,
)


well_to_loc_map_96 = {
    "A1": "well_0_0",
    "B1": "well_0_1",
    "C1": "well_0_2",
    "D1": "well_0_3",
    "E1": "well_0_4",
    "F1": "well_0_5",
    "G1": "well_0_6",
    "H1": "well_0_7",
    "A2": "well_1_0",
    "B2": "well_1_1",
    "C2": "well_1_2",
    "D2": "well_1_3",
    "E2": "well_1_4",
    "F2": "well_1_5",
    "G2": "well_1_6",
    "H2": "well_1_7",
    "A3": "well_2_0",
    "B3": "well_2_1",
    "C3": "well_2_2",
    "D3": "well_2_3",
    "E3": "well_2_4",
    "F3": "well_2_5",
    "G3": "well_2_6",
    "H3": "well_2_7",
    "A4": "well_3_0",
    "B4": "well_3_1",
    "C4": "well_3_2",
    "D4": "well_3_3",
    "E4": "well_3_4",
    "F4": "well_3_5",
    "G4": "well_3_6",
    "H4": "well_3_7",
    "A5": "well_4_0",
    "B5": "well_4_1",
    "C5": "well_4_2",
    "D5": "well_4_3",
    "E5": "well_4_4",
    "F5": "well_4_5",
    "G5": "well_4_6",
    "H5": "well_4_7",
    "A6": "well_5_0",
    "B6": "well_5_1",
    "C6": "well_5_2",
    "D6": "well_5_3",
    "E6": "well_5_4",
    "F6": "well_5_5",
    "G6": "well_5_6",
    "H6": "well_5_7",
    "A7": "well_6_0",
    "B7": "well_6_1",
    "C7": "well_6_2",
    "D7": "well_6_3",
    "E7": "well_6_4",
    "F7": "well_6_5",
    "G7": "well_6_6",
    "H7": "well_6_7",
    "A8": "well_7_0",
    "B8": "well_7_1",
    "C8": "well_7_2",
    "D8": "well_7_3",
    "E8": "well_7_4",
    "F8": "well_7_5",
    "G8": "well_7_6",
    "H8": "well_7_7",
    "A9": "well_8_0",
    "B9": "well_8_1",
    "C9": "well_8_2",
    "D9": "well_8_3",
    "E9": "well_8_4",
    "F9": "well_8_5",
    "G9": "well_8_6",
    "H9": "well_8_7",
    "A10": "well_9_0",
    "B10": "well_9_1",
    "C10": "well_9_2",
    "D10": "well_9_3",
    "E10": "well_9_4",
    "F10": "well_9_5",
    "G10": "well_9_6",
    "H10": "well_9_7",
    "A11": "well_10_0",
    "B11": "well_10_1",
    "C11": "well_10_2",
    "D11": "well_10_3",
    "E11": "well_10_4",
    "F11": "well_10_5",
    "G11": "well_10_6",
    "H11": "well_10_7",
    "A12": "well_11_0",
    "B12": "well_11_1",
    "C12": "well_11_2",
    "D12": "well_11_3",
    "E12": "well_11_4",
    "F12": "well_11_5",
    "G12": "well_11_6",
    "H12": "well_11_7",
}


well_to_loc_map_24 = {
    "A1": "well_0_0",
    "B1": "well_0_1",
    "C1": "well_0_2",
    "D1": "well_0_3",
    "A2": "well_1_0",
    "B2": "well_1_1",
    "C2": "well_1_2",
    "D2": "well_1_3",
    "A3": "well_2_0",
    "B3": "well_2_1",
    "C3": "well_2_2",
    "D3": "well_2_3",
    "A4": "well_3_0",
    "B4": "well_3_1",
    "C4": "well_3_2",
    "D4": "well_3_3",
    "A5": "well_4_0",
    "B5": "well_4_1",
    "C5": "well_4_2",
    "D5": "well_4_3",
    "A6": "well_5_0",
    "B6": "well_5_1",
    "C6": "well_5_2",
    "D6": "well_5_3",
    "E6": "well_5_4",
}


def StockVial(name: str, location: tuple) -> Well:
    a = Well(
        name=name,
        size_x=9.00,
        size_y=9.00,
        size_z=38,
    )

    a.location = Coordinate(x=location[0], y=location[1], z=location[2])
    return a


def StockTrough(name: str) -> TecanPlate:
    return TecanPlate(
        name=name,
        size_x=127.4,
        size_y=85.5,
        size_z=44.0,
        items=[
            [StockVial(name="A1", location=(12.5, 70.6, 0.0))],
            [StockVial(name="B1", location=(12.5, 61.6, 0.0))],
            [StockVial(name="C1", location=(12.5, 52.6, 0.0))],
            [StockVial(name="D1", location=(12.5, 43.6, 0.0))],
            [StockVial(name="E1", location=(12.5, 34.6, 0.0))],
            [StockVial(name="F1", location=(12.5, 25.6, 0.0))],
            [StockVial(name="G1", location=(12.5, 16.6, 0.0))],
            [StockVial(name="H1", location=(12.5, 7.6, 0.0))],

            [StockVial(name="A2", location=(21.5, 70.6, 0.0))],
            [StockVial(name="B2", location=(21.5, 61.6, 0.0))],
            [StockVial(name="C2", location=(21.5, 52.6, 0.0))],
            [StockVial(name="D2", location=(21.5, 43.6, 0.0))],
            [StockVial(name="E2", location=(21.5, 34.6, 0.0))],
            [StockVial(name="F2", location=(21.5, 25.6, 0.0))],
            [StockVial(name="G2", location=(21.5, 16.6, 0.0))],
            [StockVial(name="H2", location=(21.5, 7.6, 0.0))],

            [StockVial(name="A3", location=(30.5, 70.6, 0.0))],
            [StockVial(name="B3", location=(30.5, 61.6, 0.0))],
            [StockVial(name="C3", location=(30.5, 52.6, 0.0))],
            [StockVial(name="D3", location=(30.5, 43.6, 0.0))],
            [StockVial(name="E3", location=(30.5, 34.6, 0.0))],
            [StockVial(name="F3", location=(30.5, 25.6, 0.0))],
            [StockVial(name="G3", location=(30.5, 16.6, 0.0))],
            [StockVial(name="H3", location=(30.5, 7.6, 0.0))],

            [StockVial(name="A4", location=(39.5, 70.6, 0.0))],
            [StockVial(name="B4", location=(39.5, 61.6, 0.0))],
            [StockVial(name="C4", location=(39.5, 52.6, 0.0))],
            [StockVial(name="D4", location=(39.5, 43.6, 0.0))],
            [StockVial(name="E4", location=(39.5, 34.6, 0.0))],
            [StockVial(name="F4", location=(39.5, 25.6, 0.0))],
            [StockVial(name="G4", location=(39.5, 16.6, 0.0))],
            [StockVial(name="H4", location=(39.5, 7.6, 0.0))],

            [StockVial(name="A5", location=(48.5, 70.6, 0.0))],
            [StockVial(name="B5", location=(48.5, 61.6, 0.0))],
            [StockVial(name="C5", location=(48.5, 52.6, 0.0))],
            [StockVial(name="D5", location=(48.5, 43.6, 0.0))],
            [StockVial(name="E5", location=(48.5, 34.6, 0.0))],
            [StockVial(name="F5", location=(48.5, 25.6, 0.0))],
            [StockVial(name="G5", location=(48.5, 16.6, 0.0))],
            [StockVial(name="H5", location=(48.5, 7.6, 0.0))],

            [StockVial(name="A6", location=(57.5, 70.6, 0.0))],
            [StockVial(name="B6", location=(57.5, 61.6, 0.0))],
            [StockVial(name="C6", location=(57.5, 52.6, 0.0))],
            [StockVial(name="D6", location=(57.5, 43.6, 0.0))],
            [StockVial(name="E6", location=(57.5, 34.6, 0.0))],
            [StockVial(name="F6", location=(57.5, 25.6, 0.0))],
            [StockVial(name="G6", location=(57.5, 16.6, 0.0))],
            [StockVial(name="H6", location=(57.5, 7.6, 0.0))],

            [StockVial(name="A7", location=(66.5, 70.6, 0.0))],
            [StockVial(name="B7", location=(66.5, 61.6, 0.0))],
            [StockVial(name="C7", location=(66.5, 52.6, 0.0))],
            [StockVial(name="D7", location=(66.5, 43.6, 0.0))],
            [StockVial(name="E7", location=(66.5, 34.6, 0.0))],
            [StockVial(name="F7", location=(66.5, 25.6, 0.0))],
            [StockVial(name="G7", location=(66.5, 16.6, 0.0))],
            [StockVial(name="H7", location=(66.5, 7.6, 0.0))],

            [StockVial(name="A8", location=(75.5, 70.6, 0.0))],
            [StockVial(name="B8", location=(75.5, 61.6, 0.0))],
            [StockVial(name="C8", location=(75.5, 52.6, 0.0))],
            [StockVial(name="D8", location=(75.5, 43.6, 0.0))],
            [StockVial(name="E8", location=(75.5, 34.6, 0.0))],
            [StockVial(name="F8", location=(75.5, 25.6, 0.0))],
            [StockVial(name="G8", location=(75.5, 16.6, 0.0))],
            [StockVial(name="H8", location=(75.5, 7.6, 0.0))],

            [StockVial(name="A9", location=(84.5, 70.6, 0.0))],
            [StockVial(name="B9", location=(84.5, 61.6, 0.0))],
            [StockVial(name="C9", location=(84.5, 52.6, 0.0))],
            [StockVial(name="D9", location=(84.5, 43.6, 0.0))],
            [StockVial(name="E9", location=(84.5, 34.6, 0.0))],
            [StockVial(name="F9", location=(84.5, 25.6, 0.0))],
            [StockVial(name="G9", location=(84.5, 16.6, 0.0))],
            [StockVial(name="H9", location=(84.5, 7.6, 0.0))],

            [StockVial(name="A10", location=(93.5, 70.6, 0.0))],
            [StockVial(name="B10", location=(93.5, 61.6, 0.0))],
            [StockVial(name="C10", location=(93.5, 52.6, 0.0))],
            [StockVial(name="D10", location=(93.5, 43.6, 0.0))],
            [StockVial(name="E10", location=(93.5, 34.6, 0.0))],
            [StockVial(name="F10", location=(93.5, 25.6, 0.0))],
            [StockVial(name="G10", location=(93.5, 16.6, 0.0))],
            [StockVial(name="H10", location=(93.5, 7.6, 0.0))],

            [StockVial(name="A11", location=(102.5, 70.6, 0.0))],
            [StockVial(name="B11", location=(102.5, 61.6, 0.0))],
            [StockVial(name="C11", location=(102.5, 52.6, 0.0))],
            [StockVial(name="D11", location=(102.5, 43.6, 0.0))],
            [StockVial(name="E11", location=(102.5, 34.6, 0.0))],
            [StockVial(name="F11", location=(102.5, 25.6, 0.0))],
            [StockVial(name="G11", location=(102.5, 16.6, 0.0))],
            [StockVial(name="H11", location=(102.5, 7.6, 0.0))],

            [StockVial(name="A12", location=(111.5, 70.6, 0.0))],
            [StockVial(name="B12", location=(111.5, 61.6, 0.0))],
            [StockVial(name="C12", location=(111.5, 52.6, 0.0))],
            [StockVial(name="D12", location=(111.5, 43.6, 0.0))],
            [StockVial(name="E12", location=(111.5, 34.6, 0.0))],
            [StockVial(name="F12", location=(111.5, 25.6, 0.0))],
            [StockVial(name="G12", location=(111.5, 16.6, 0.0))],
            [StockVial(name="H12", location=(111.5, 7.6, 0.0))],

        ],
        with_lid=False,
        lid_height=0,
        model="Stock_Trough",
        z_travel=1900.0,
        z_start=1957.0,
        z_dispense=1975.0,
        z_max=2005.0,
        area=33.2,
    )


def WashPlate(name: str) -> TecanPlate:
    return TecanPlate(
        name=name,
        size_x=127.4,
        size_y=85.5,
        size_z=0.0,
        items=[
            [StockVial(name="A1", location=(12.5, 72.1, 0.0))],
            [StockVial(name="B1", location=(12.5, 63.1, 0.0))],
            [StockVial(name="C1", location=(12.5, 54.1, 0.0))],
            [StockVial(name="D1", location=(12.5, 45.1, 0.0))],
            [StockVial(name="E1", location=(12.5, 36.1, 0.0))],
            [StockVial(name="F1", location=(12.5, 27.1, 0.0))],
            [StockVial(name="G1", location=(12.5, 18.1, 0.0))],
            [StockVial(name="H1", location=(12.5, 9.1, 0.0))],

            [StockVial(name="A2", location=(21.5, 72.1, 0.0))],
            [StockVial(name="B2", location=(21.5, 63.1, 0.0))],
            [StockVial(name="C2", location=(21.5, 54.1, 0.0))],
            [StockVial(name="D2", location=(21.5, 45.1, 0.0))],
            [StockVial(name="E2", location=(21.5, 36.1, 0.0))],
            [StockVial(name="F2", location=(21.5, 27.1, 0.0))],
            [StockVial(name="G2", location=(21.5, 18.1, 0.0))],
            [StockVial(name="H2", location=(21.5, 9.1, 0.0))],

            [StockVial(name="A3", location=(30.5, 72.1, 0.0))],
            [StockVial(name="B3", location=(30.5, 63.1, 0.0))],
            [StockVial(name="C3", location=(30.5, 54.1, 0.0))],
            [StockVial(name="D3", location=(30.5, 45.1, 0.0))],
            [StockVial(name="E3", location=(30.5, 36.1, 0.0))],
            [StockVial(name="F3", location=(30.5, 27.1, 0.0))],
            [StockVial(name="G3", location=(30.5, 18.1, 0.0))],
            [StockVial(name="H3", location=(30.5, 9.1, 0.0))],

            [StockVial(name="A4", location=(39.5, 72.1, 0.0))],
            [StockVial(name="B4", location=(39.5, 63.1, 0.0))],
            [StockVial(name="C4", location=(39.5, 54.1, 0.0))],
            [StockVial(name="D4", location=(39.5, 45.1, 0.0))],
            [StockVial(name="E4", location=(39.5, 36.1, 0.0))],
            [StockVial(name="F4", location=(39.5, 27.1, 0.0))],
            [StockVial(name="G4", location=(39.5, 18.1, 0.0))],
            [StockVial(name="H4", location=(39.5, 9.1, 0.0))],

            [StockVial(name="A5", location=(48.5, 72.1, 0.0))],
            [StockVial(name="B5", location=(48.5, 63.1, 0.0))],
            [StockVial(name="C5", location=(48.5, 54.1, 0.0))],
            [StockVial(name="D5", location=(48.5, 45.1, 0.0))],
            [StockVial(name="E5", location=(48.5, 36.1, 0.0))],
            [StockVial(name="F5", location=(48.5, 27.1, 0.0))],
            [StockVial(name="G5", location=(48.5, 18.1, 0.0))],
            [StockVial(name="H5", location=(48.5, 9.1, 0.0))],

            [StockVial(name="A6", location=(57.5, 72.1, 0.0))],
            [StockVial(name="B6", location=(57.5, 63.1, 0.0))],
            [StockVial(name="C6", location=(57.5, 54.1, 0.0))],
            [StockVial(name="D6", location=(57.5, 45.1, 0.0))],
            [StockVial(name="E6", location=(57.5, 36.1, 0.0))],
            [StockVial(name="F6", location=(57.5, 27.1, 0.0))],
            [StockVial(name="G6", location=(57.5, 18.1, 0.0))],
            [StockVial(name="H6", location=(57.5, 9.1, 0.0))],

            [StockVial(name="A7", location=(66.5, 72.1, 0.0))],
            [StockVial(name="B7", location=(66.5, 63.1, 0.0))],
            [StockVial(name="C7", location=(66.5, 54.1, 0.0))],
            [StockVial(name="D7", location=(66.5, 45.1, 0.0))],
            [StockVial(name="E7", location=(66.5, 36.1, 0.0))],
            [StockVial(name="F7", location=(66.5, 27.1, 0.0))],
            [StockVial(name="G7", location=(66.5, 18.1, 0.0))],
            [StockVial(name="H7", location=(66.5, 9.1, 0.0))],

            [StockVial(name="A8", location=(75.5, 72.1, 0.0))],
            [StockVial(name="B8", location=(75.5, 63.1, 0.0))],
            [StockVial(name="C8", location=(75.5, 54.1, 0.0))],
            [StockVial(name="D8", location=(75.5, 45.1, 0.0))],
            [StockVial(name="E8", location=(75.5, 36.1, 0.0))],
            [StockVial(name="F8", location=(75.5, 27.1, 0.0))],
            [StockVial(name="G8", location=(75.5, 18.1, 0.0))],
            [StockVial(name="H8", location=(75.5, 9.1, 0.0))],

            [StockVial(name="A9", location=(84.5, 72.1, 0.0))],
            [StockVial(name="B9", location=(84.5, 63.1, 0.0))],
            [StockVial(name="C9", location=(84.5, 54.1, 0.0))],
            [StockVial(name="D9", location=(84.5, 45.1, 0.0))],
            [StockVial(name="E9", location=(84.5, 36.1, 0.0))],
            [StockVial(name="F9", location=(84.5, 27.1, 0.0))],
            [StockVial(name="G9", location=(84.5, 18.1, 0.0))],
            [StockVial(name="H9", location=(84.5, 9.1, 0.0))],

            [StockVial(name="A10", location=(93.5, 72.1, 0.0))],
            [StockVial(name="B10", location=(93.5, 63.1, 0.0))],
            [StockVial(name="C10", location=(93.5, 54.1, 0.0))],
            [StockVial(name="D10", location=(93.5, 45.1, 0.0))],
            [StockVial(name="E10", location=(93.5, 36.1, 0.0))],
            [StockVial(name="F10", location=(93.5, 27.1, 0.0))],
            [StockVial(name="G10", location=(93.5, 18.1, 0.0))],
            [StockVial(name="H10", location=(93.5, 9.1, 0.0))],

            [StockVial(name="A11", location=(102.5, 72.1, 0.0))],
            [StockVial(name="B11", location=(102.5, 63.1, 0.0))],
            [StockVial(name="C11", location=(102.5, 54.1, 0.0))],
            [StockVial(name="D11", location=(102.5, 45.1, 0.0))],
            [StockVial(name="E11", location=(102.5, 36.1, 0.0))],
            [StockVial(name="F11", location=(102.5, 27.1, 0.0))],
            [StockVial(name="G11", location=(102.5, 18.1, 0.0))],
            [StockVial(name="H11", location=(102.5, 9.1, 0.0))],

            [StockVial(name="A12", location=(111.5, 72.1, 0.0))],
            [StockVial(name="B12", location=(111.5, 63.1, 0.0))],
            [StockVial(name="C12", location=(111.5, 54.1, 0.0))],
            [StockVial(name="D12", location=(111.5, 45.1, 0.0))],
            [StockVial(name="E12", location=(111.5, 36.1, 0.0))],
            [StockVial(name="F12", location=(111.5, 27.1, 0.0))],
            [StockVial(name="G12", location=(111.5, 18.1, 0.0))],
            [StockVial(name="H12", location=(111.5, 9.1, 0.0))],

        ],
        with_lid=False,
        lid_height=0,
        model="Stock_Trough",
        z_travel=1930.0,
        z_start=2020.0,
        z_dispense=1800.0,
        z_max=2025.0,
        area=33.2,
    )


def StockPlate_2Dram_24(name: str) -> TecanPlate:
    return TecanPlate(
        name=name,
        size_x=127.8,
        size_y=85,
        size_z=24.0,
        items=create_equally_spaced(
            Well,
            num_items_x=6,
            num_items_y=4,
            dx=3.0,
            dy=6.5,
            dz=0.0,
            item_dx=21.0,
            item_dy=19.6,
            size_x=18.0,
            size_y=18.0,
        ),
        with_lid=False,
        lid_height=0,
        model="StockPlate_2Dram_24",
        z_travel=1975.0,
        z_start=1975.0,
        z_dispense=1550.0,
        z_max=2000.0,
        area=33.2,
    )


def Analysis_Plate(name: str, with_lid: bool = False) -> TecanPlate:
  return TecanPlate(
    name=name,
    size_x=127.8,
    size_y=85.4,
    size_z=37.0,
    with_lid=with_lid,
    lid_height=8,
    model="DeepWell_square_96_Well",
    z_travel=1590.0,
    z_start=1670.0,
    z_dispense=1760.0,
    z_max=2060.0,
    area=64.0,
    items=create_equally_spaced(Well,
      num_items_x=12,
      num_items_y=8,
      dx=12.5,
      dy=6.7,
      dz=0.0,
      item_dx=9.0,
      item_dy=9.0,
      size_x=9.0,
      size_y=9.0
    ),
  )


def Reaction_96_Plate(name: str, with_lid: bool = False) -> TecanPlate:
  """
  """

  return TecanPlate(
    name=name,
    size_x=127.8,
    size_y=87.4,
    size_z=7.6,
    with_lid=with_lid,
    lid_height=8,
    model="Microplate_96_Well",
    z_travel=1750.0,
    z_start=1800.0,
    z_dispense=1710.0,
    z_max=2005.0,
    area=33.2,
    items=create_equally_spaced(Well,
      num_items_x=12,
      num_items_y=8,
      dx=11.0,
      dy=7.6,
      dz=0.0,
      item_dx=9.0,
      item_dy=9.0,
      size_x=9.0,
      size_y=9.0
    ),
  )


def ReactionCarrier(name: str) -> TecanPlateCarrier:
  """ Tecan part no. 10612624

  Coley:

  .. code-block:: python

      return TecanPlateCarrier(
        name=name,
        size_x=149.0,
        size_y=295.0,
        size_z=6.0,
        off_x=12.0,
        off_y=11.0,
        sites=create_homogeneous_carrier_sites(locations=[
            Coordinate(11.7, 10.5, 6.0),
            Coordinate(11.0, 106.4, 6.0),
            Coordinate(11.0, 202.8, 6.0),
          ],
          site_size_x=127.0,
          site_size_y=85.5,
        ),
        model="MP_3Pos_Flat"
      )
  """

  return TecanPlateCarrier(
    name=name,
    size_x=149.0,
    size_y=295.0,
    size_z=6.0,
    off_x=12.0,
    off_y=11.0,
    roma_x=2056,
    roma_y=444,
    roma_z_safe=600,
    roma_z_travel=2418,
    roma_z_end=2503,
    sites=create_homogeneous_carrier_sites(locations=[
        Coordinate(10.4, 8.0, 60.0),
        Coordinate(10.4, 200.0, 60.0),
      ],
      site_size_x=127.0,
      site_size_y=87.5,
    ),
    model="MP_Reactor_Carrier"
  )



def MP_3Pos_FlatTest(name: str) -> TecanPlateCarrier:
  """ Tecan part no. 10612624

  Coley:

  .. code-block:: python

      return TecanPlateCarrier(
        name=name,
        size_x=149.0,
        size_y=295.0,
        size_z=6.0,
        off_x=12.0,
        off_y=11.0,
        sites=create_homogeneous_carrier_sites(locations=[
            Coordinate(11.7, 10.5, 6.0),
            Coordinate(11.0, 106.4, 6.0),
            Coordinate(11.0, 202.8, 6.0),
          ],
          site_size_x=127.0,
          site_size_y=85.5,
        ),
        model="MP_3Pos_Flat"
      )
  """

  return TecanPlateCarrier(
    name=name,
    size_x=149.0,
    size_y=295.0,
    size_z=6.0,
    off_x=12.0,
    off_y=11.0,
    roma_x=2056,
    roma_y=441,
    roma_z_safe=610,
    roma_z_travel=2418,
    roma_z_end=2503,
    sites=create_homogeneous_carrier_sites(locations=[
        Coordinate(10.4, 11.5, 10.0),
        Coordinate(10.4, 107.5, 10.0),
        Coordinate(10.4, 203.5, 10.0),
        Coordinate(10.4, 299.5, 110.0),
        Coordinate(10.4, 395.5, 110.0),
        Coordinate(10.4, 491.5, 110.0),
      ],
      site_size_x=127.0,
      site_size_y=85.5,
    ),
    model="MP_3Pos_Flat"
  )





def build_layout() -> TecanDeck:

    deck = TecanDeck(
        num_rails=EVO200_NUM_RAILS,
        size_x=EVO200_SIZE_X,
        size_y=EVO200_SIZE_Y,
        size_z=EVO200_SIZE_Z,
    )

    wash_station = deck.get_resource("wash_station")
    deck.unassign_child_resource(wash_station)


    plt_car1 = MP_3Pos_FlatTest(name="plate_carrier_1")
    plt_car2 = MP_3Pos_Flat(name="plate_carrier_2")
    plt_car3 = ReactionCarrier(name="plate_carrier_3")


    stock_solvent_plate = StockTrough(name="solvent_trough") # 12 column stock solution trough
    plt_car1[2] = stock_solvent_plate


    stock_solvent_plate2 = StockPlate_2Dram_24(name="stock_plate")  # 24 well 2 dram vials
    # for k in stock_solvent_plate2:
        # print(k[0].name)
    plt_car1[1] = stock_solvent_plate2


    reaction_96 = Reaction_96_Plate(name="reaction_setup") # reactor block
    plt_car1[0] = reaction_96


    wash_plate = WashPlate(name="quench_trough") # 4 column solvent trough
    plt_car2[2] = wash_plate

    analysis_96 = Analysis_Plate(name="analytical_plate") # UPLC-MS plate
    plt_car2[1] = analysis_96


    deck.assign_child_resource(plt_car1, rails=7)
    deck.assign_child_resource(plt_car2, rails=13)
    deck.assign_child_resource(plt_car3, rails=35)

    # for k in deck.children:
    #    print(k.roma_x)

    return deck
