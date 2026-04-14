import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def preview_data(df):
    print("Shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumn Types:")
    print(df.dtypes)

def category_summary(df):
    summary = df.groupby('category')['amount'].sum()
    summary = summary.sort_values(ascending=False)
    print("\n Spending by Category:")
    print(summary)
    return summary
def lowest_category(summary):
    top = summary.idxmin()
    amount = summary.min()
    print(f"\nLowest Spending: {top} → ₹{amount}")
    return top
def total_spending(df):
    total = df['amount'].sum()
    print(f"\n Total spending: ₹{total}")
def monthly_summary(df):
    df['month'] = df['date'].dt.strftime('%Y-%m')
    monthly = df.groupby('month')['amount'].sum()
    print("\n Monthly Spending:")
    print("peak month:", monthly.idxmax())
    print(monthly)
    return monthly
