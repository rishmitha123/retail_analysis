create database retail_hub;
use retail_hub;
select * from sales;

-- Total sales by category
-- consider one category and group all the rows of that category and print the total revenue
-- considering the category and total of sales from sales which would be group by category so that the total sales relateed to one category would be added and produce the result in total_revenue
SELECT category, SUM(total_sales) AS total_revenue
FROM sales
GROUP BY category;
-- top 5 products
-- it will consider the product by grouping one product all the sales of that product would be added and arranged in descending order from that the top 5 would be picked as we mention limit=5;
SELECT product, SUM(total_sales) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 5;

-- sales by location
-- we will consider one location it will group and add the sales of that location and arrange them in descending order
SELECT customer_location, SUM(total_sales) AS total_revenue
FROM sales
GROUP BY customer_location
ORDER BY total_revenue DESC;

-- sales by payment method
SELECT payment_method, SUM(total_sales) AS total_revenue
    FROM sales
    GROUP BY payment_method
    ORDER BY total_revenue DESC;
-- sales breakdown  by status
SELECT 
    status,
    COUNT(*) AS total_orders,
    SUM(total_sales) AS total_revenue
FROM sales
GROUP BY status
ORDER BY total_revenue DESC;
-- sales by product
SELECT 
    Product, 
    SUM(Total_Sales) AS Total_Revenue
FROM 
    sales
GROUP BY 
    Product
ORDER BY 
    Total_Revenue DESC;
    
    SELECT product, COUNT(*) AS order_count
FROM sales
GROUP BY product
ORDER BY order_count DESC;


    
    



