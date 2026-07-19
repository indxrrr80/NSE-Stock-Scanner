import pandas as pd
from scanner.logger import logger

def load_bhavcopy(file_path):

    logger.info(f"Loading bhavcopy file: {file_path}")

    df = pd.read_csv(file_path)

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Convert numeric columns
    numeric_columns = [
        "PREV_CLOSE",
        "OPEN_PRICE",
        "HIGH_PRICE",
        "LOW_PRICE",
        "LAST_PRICE",
        "CLOSE_PRICE",
        "AVG_PRICE",
        "TTL_TRD_QNTY",
        "TURNOVER_LACS",
        "NO_OF_TRADES",
        "DELIV_QTY",
        "DELIV_PER"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    logger.info(
        f"Bhavcopy loaded successfully. "
        f"Rows: {len(df)}, Columns: {len(df.columns)}"
    )

    return df


def load_delivery(file_path):
    return pd.read_csv(file_path)