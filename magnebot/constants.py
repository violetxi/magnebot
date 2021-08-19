# The radius of the Magnebot as defined by its longer axis.
MAGNEBOT_RADIUS: float = 0.22
# The cell size on the occupancy map. This is slightly bigger than diameter of the Magnebot.
OCCUPANCY_CELL_SIZE: float = (MAGNEBOT_RADIUS * 2) + 0.05
# The required version of TDW.
TDW_VERSION: str = "1.8.24"
