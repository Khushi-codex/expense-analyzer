from analyzer import load_data, category_summary, lowest_category, total_spending, monthly_summary
from charts.visualizer import bar_chart, line_chart

df = load_data('data/expenses.csv')

total_spending(df)
cat_summary = category_summary(df)
lowest_category(df)
mon_summary = monthly_summary(df)

bar_chart(cat_summary)
line_chart(mon_summary)

print(mon_summary)
