import os


def save_report(df, output_file):
    """
    Save scanner result into Excel.
    """

    # Create Output folder if it doesn't exist
    os.makedirs("Output", exist_ok=True)

    # Save Excel
    df.to_excel(output_file, index=False)

    print("\nresults saved successfully!")
    print(f"Location : {output_file}")