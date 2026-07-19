import os

# ==========================================
# NSE Scanner Configuration
# ==========================================

# Folders
DATA_FOLDER = "Data"
OUTPUT_FOLDER = "Output"

# Data File
DATA_FILE = os.path.join(
    DATA_FOLDER,
    "sec_bhavdata_full_24062026.csv"
)

# Scanner Thresholds
MIN_DELIVERY = 70
MIN_VOLUME = 1000000
GAP_PERCENT = 2