import  matplotlib.pyplot as plt
import os

def bar_chart(category_summary):
    plt.figure(figsize=(10, 5))
    category_summary.plot(kind='bar' , color='steelblue')
    plt.title('Spending by Catefory')
    plt.xlabel('Category')
    plt.ylabel('Amount (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('charts/category_chart.png')
    plt.show()
    print("Chart saved to charts/category_chart.png")

def line_chart(monthly_summary):
    plt.figure(figsize=(10, 5))
    monthly_summary.plot(kind='line', marker='o', color='green')
    plt.title('Monthly Spending Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount (₹)')
    plt.tight_layout()
    plt.savefig('charts/monthly_chart.png')
    plt.show()
    print("Chart saved to charts/monthly_chart.png")

