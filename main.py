import os

from scanner.data_loader import load_bhavcopy
from scanner.reports import save_report
from scanner.filters import (
    high_delivery,
    high_volume,
    gap_up,
    gap_down,
    bullish,
    bearish,
    high_delivery_volume,
    gap_up_high_volume
)


def main():

    print("=" * 60)
    print("               NSE STOCK SCANNER")
    print("=" * 60)

    # Path to Bhavcopy
    file_path = os.path.join(
        "Data",
        "sec_bhavdata_full_24062026.csv"
    )

    # Check if file exists
    if not os.path.exists(file_path):
        print("Bhavcopy file not found!")
        return

    # Load Data
    df = load_bhavcopy(file_path)

    print(f"\nTotal Stocks Loaded : {len(df)}")

    # Scanner Menu
    print("\nAvailable Scanners")
    print("--------------------------")
    print("1. High Delivery Scanner")
    print("2. High Volume Scanner")
    print("3. Gap Up Scanner")
    print("4. Gap Down Scanner")
    print("5. Bullish Candle Scanner")
    print("6. Bearish Candle Scanner")
    print("7. High Delivery & High Volume Scanner")
    print("8. Gap Up & High Volume Scanner")

    choice = input("\nEnter Scanner Number : ")

    # -------------------------------
    # High Delivery Scanner
    # -------------------------------
    if choice == "1":

        result = high_delivery(df)

        output_file = os.path.join(
            "Output",
            "High_Delivery.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "CLOSE_PRICE",
                    "DELIV_PER",
                    "TTL_TRD_QNTY"
                ]
            ].head(20)
        )

    # -------------------------------
    # High Volume Scanner
    # -------------------------------
    elif choice == "2":

        result = high_volume(df)

        output_file = os.path.join(
            "Output",
            "High_Volume.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "CLOSE_PRICE",
                    "TTL_TRD_QNTY",
                    "DELIV_PER"
                ]
            ].head(20)
        )

    # -------------------------------
    # Gap Up Scanner
    # -------------------------------
    elif choice == "3":

        result = gap_up(df)

        output_file = os.path.join(
            "Output",
            "Gap_Up.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "PREV_CLOSE",
                    "OPEN_PRICE",
                    "GAP_PERCENT"
                ]
            ].head(20)
        )

    # -------------------------------
    # Gap Down Scanner
    # -------------------------------
    elif choice == "4":

        result = gap_down(df)

        output_file = os.path.join(
            "Output",
            "Gap_Down.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "PREV_CLOSE",
                    "OPEN_PRICE",
                    "GAP_PERCENT"
                ]
            ].head(20)
        )

    # -------------------------------
    # Bullish Candle Scanner
    # -------------------------------
    elif choice == "5":

        result = bullish(df)

        output_file = os.path.join(
            "Output",
            "Bullish_Candles.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "OPEN_PRICE",
                    "CLOSE_PRICE",
                    "DELIV_PER"
                ]
            ].head(20)
        )

    # -------------------------------
    # Invalid Choice
    # -------------------------------
        # -------------------------------
    # Bearish Candle Scanner
    # -------------------------------
    elif choice == "6":

        result = bearish(df)

        output_file = os.path.join(
            "Output",
            "Bearish_Candles.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "OPEN_PRICE",
                    "CLOSE_PRICE",
                    "DELIV_PER"
                ]
            ].head(20)
        )
       # -------------------------------
    # High Delivery + High Volume
    # -------------------------------
    elif choice == "7":

        result = high_delivery_volume(df)

        output_file = os.path.join(
            "Output",
            "High_Delivery_High_Volume.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "DELIV_PER",
                    "TTL_TRD_QNTY",
                    "CLOSE_PRICE"
                ]
            ].head(20)
        )
       # -------------------------------
    # Gap Up + High Volume Scanner
    # -------------------------------
    elif choice == "8":

        result = gap_up_high_volume(df)

        output_file = os.path.join(
            "Output",
            "Gap_Up_High_Volume.xlsx"
        )

        print(f"\nStocks Found : {len(result)}\n")

        print(
            result[
                [
                    "SYMBOL",
                    "PREV_CLOSE",
                    "OPEN_PRICE",
                    "GAP_PERCENT",
                    "TTL_TRD_QNTY"
                ]
            ].head(20)
        )
    else:
        print("\nInvalid Choice!")
        return

    # Save Report
    save_report(result, output_file)


if __name__ == "__main__":
 main()