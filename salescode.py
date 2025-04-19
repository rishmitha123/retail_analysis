import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Rishmitha@123",
    database="retail_hub"
)
cursor = conn.cursor()

def view_all_sales():
    cursor.execute("SELECT * FROM sales")
    results = cursor.fetchall()
    if results:
        print("\n All Sales Records:")
        print(tabulate(results, headers=[i[0] for i in cursor.description], tablefmt="simple"))
    else:
        print("No records found.")

def sales_by_category():
    cursor.execute("""
        SELECT category, SUM(total_sales) AS total_revenue
        FROM sales
        GROUP BY category
        ORDER BY total_revenue DESC;
    """)
    results = cursor.fetchall()
    print("\n Total Sales by Category:")
    print(tabulate(results, headers=["Category", "Total Revenue"], tablefmt="fancy_grid"))

    df = pd.DataFrame(results, columns=['Category', 'Total Revenue'])
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Total Revenue'], color='skyblue')
    plt.title('Total Sales by Category', fontsize=16)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Total Revenue', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def top_products():
    cursor.execute("""
        SELECT product, SUM(total_sales) AS total_revenue
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC
        LIMIT 5;
    """)
    results = cursor.fetchall()
    print("\n Top 5 Products by Sales:")
    print(tabulate(results, headers=["Product", "Total Revenue"], tablefmt="fancy_grid"))

    df = pd.DataFrame(results, columns=['Product', 'Total Revenue'])
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Product'], df['Total Revenue'], color='mediumseagreen')
    plt.title(' Top 5 Products by Total Sales', fontsize=16)
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Total Revenue ($)', fontsize=12)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 500, f"${yval:,.0f}", ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def sales_by_status():
    cursor.execute("""
        SELECT status, SUM(total_sales) AS total_revenue
        FROM sales
        GROUP BY status
        ORDER BY total_revenue DESC;
    """)
    results = cursor.fetchall()
    print("\n Sales Breakdown by Status:")
    print(tabulate(results, headers=["Status", "Total Revenue"], tablefmt="fancy_grid"))

    df = pd.DataFrame(results, columns=['Status', 'Total Revenue'])
    plt.figure(figsize=(8, 8))
    plt.pie(df['Total Revenue'], labels=df['Status'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(' Revenue by Order Status', fontsize=16)
    plt.axis('equal')
    plt.show()

def sales_by_location():
    cursor.execute("""
        SELECT customer_location, SUM(total_sales) AS total_revenue
        FROM sales
        GROUP BY customer_location
        ORDER BY total_revenue DESC;
    """)
    results = cursor.fetchall()
    print("\n Sales by Customer Location:")
    print(tabulate(results, headers=["Location", "Total Revenue"], tablefmt="fancy_grid"))

    df = pd.DataFrame(results, columns=['Location', 'Total Revenue'])
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Location'], df['Total Revenue'], color='cornflowerblue')
    plt.title(' Sales by Customer Location', fontsize=16)
    plt.xlabel('Customer Location', fontsize=12)
    plt.ylabel('Total Revenue ($)', fontsize=12)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height + 500, f"${height:,.0f}", ha='center', fontsize=10)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def sales_by_payment_method():
    cursor.execute("""
        SELECT payment_method, SUM(total_sales) AS total_revenue
        FROM sales
        GROUP BY payment_method
        ORDER BY total_revenue DESC;
    """)
    results = cursor.fetchall()
    print("\n Revenue by Payment Method:")
    print(tabulate(results, headers=["Payment Method", "Total Revenue"], tablefmt="fancy_grid"))

    df = pd.DataFrame(results, columns=['Payment Method', 'Total Revenue'])
    plt.figure(figsize=(8, 8))
    plt.pie(df['Total Revenue'], labels=df['Payment Method'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(' Revenue by Payment Method', fontsize=16)
    plt.axis('equal')
    plt.show()

def sales_by_product():
    cursor.execute("""
        SELECT product, SUM(total_sales) AS total_revenue
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC;
    """)
    results = cursor.fetchall()
    print("\n Total Sales by Product:")
    print(tabulate(results, headers=["Product", "Total Revenue"], tablefmt="fancy_grid"))

    df = pd.DataFrame(results, columns=['Product', 'Total Revenue'])
    plt.figure(figsize=(8, 8))
    plt.pie(
        df['Total Revenue'],
        labels=df['Product'],
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Set3.colors
    )
    plt.title(' Total Sales by Product', fontsize=16)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Menu mapping
actions = {
    '1': view_all_sales,
    '2': sales_by_category,
    '3': top_products,
    '4': sales_by_status,
    '5': sales_by_location,
    '6': sales_by_payment_method,
    '7': sales_by_product
}

# Menu
def main():
    while True:
        print("\n Retail Data Analysis Menu")
        print("1. View all sales records")
        print("2. Total sales by category")
        print("3. Top 5 products by sales")
        print("4. Sales by order status")
        print("5. Sales by customer location")
        print("6. Sales by payment method")
        print("7. Sales by product")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting... ")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()









































