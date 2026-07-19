from scanner.config import MIN_DELIVERY, MIN_VOLUME, GAP_PERCENT
def high_delivery(df, min_delivery=MIN_DELIVERY):
    """
    Returns stocks with delivery percentage
    greater than or equal to min_delivery.
    """
    result = df[df["DELIV_PER"] >= min_delivery]
    return result.sort_values(by="DELIV_PER", ascending=False)


def high_volume(df, min_volume=MIN_VOLUME):
    """
    Returns stocks with traded quantity
    greater than or equal to min_volume.
    """
    result = df[df["TTL_TRD_QNTY"] >= min_volume]
    return result.sort_values(by="TTL_TRD_QNTY", ascending=False)


def gap_up(df, gap_percent=GAP_PERCENT):
    """
    Returns stocks with Gap Up greater than or equal to gap_percent.
    """

    # Calculate Gap %
    df = df.copy()

    df["GAP_PERCENT"] = (
        (df["OPEN_PRICE"] - df["PREV_CLOSE"])
        / df["PREV_CLOSE"]
    ) * 100

    result = df[df["GAP_PERCENT"] >= gap_percent]

    return result.sort_values(
        by="GAP_PERCENT",
        ascending=False
    )
def gap_down(df, gap_percent=GAP_PERCENT):
    """
    Returns stocks with Gap Down greater than or equal to gap_percent.
    """

    # Create a copy
    df = df.copy()

    # Calculate Gap Down %
    df["GAP_PERCENT"] = (
        (df["PREV_CLOSE"] - df["OPEN_PRICE"])
        / df["PREV_CLOSE"]
    ) * 100

    # Filter stocks
    result = df[df["GAP_PERCENT"] >= gap_percent]

    # Sort by highest gap
    return result.sort_values(
        by="GAP_PERCENT",
        ascending=False
    )
def bullish(df):
    """
    Returns all bullish candles.
    Close Price > Open Price
    """

    result = df[df["CLOSE_PRICE"] > df["OPEN_PRICE"]]

    return result.sort_values(
        by="DELIV_PER",
        ascending=False
    )
def bearish(df):
    """
    Returns all bearish candles.
    Close Price < Open Price
    """

    result = df[df["CLOSE_PRICE"] < df["OPEN_PRICE"]]

    return result.sort_values(
        by="DELIV_PER",
        ascending=False
    )
def high_delivery_volume(
    df,
    min_delivery=MIN_DELIVERY,
    min_volume=MIN_VOLUME
):
    """
    Returns stocks having both
    High Delivery and High Volume.
    """

    result = df[
        (df["DELIV_PER"] >= min_delivery)
        &
        (df["TTL_TRD_QNTY"] >= min_volume)
    ]

    return result.sort_values(
        by=["DELIV_PER", "TTL_TRD_QNTY"],
        ascending=False
    )
def gap_up_high_volume(
    df,
    gap_percent=GAP_PERCENT,
    min_volume=MIN_VOLUME
):
    """
    Returns stocks with
    Gap Up and High Volume.
    """

    df = df.copy()

    df["GAP_PERCENT"] = (
        (df["OPEN_PRICE"] - df["PREV_CLOSE"])
        / df["PREV_CLOSE"]
    ) * 100

    result = df[
        (df["GAP_PERCENT"] >= gap_percent)
        &
        (df["TTL_TRD_QNTY"] >= min_volume)
    ]

    return result.sort_values(
        by=["GAP_PERCENT", "TTL_TRD_QNTY"],
        ascending=False
    )