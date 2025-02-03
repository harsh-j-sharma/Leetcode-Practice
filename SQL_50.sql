--1757. Recyclable and Low Fat Products
select product_id from Products
where low_fats = 'Y' and recyclable = 'Y'

--584. Find Customer Referee
select name from Customer
where referee_id <> 2 or referee_id is null 
/* MySQL uses three-valued logic -- TRUE, FALSE and UNKNOWN. Anything compared to NULL evaluates to the third value: UNKNOWN. That “anything” includes NULL itself!
That’s why MySQL provides the IS NULL and IS NOT NULL operators to specifically check for NULL.
Thus, one more condition 'referee_id IS NULL' should be added to the WHERE clause as below. */

--595. Big Countries
select name,population,area from World
where area >= 3000000 or population >= 25000000

--1148. Article Views I
select distinct author_id as id from Views a
where author_id = viewer_id

--1683. Invalid Tweets
select tweet_id from Tweets
where len(content) > 15

--1378. Replace Employee ID With The Unique Identifier
select eu.unique_id,e.name from employees e
left join employeeUNI eu on e.id = eu.id

--1068. Product Sales Analysis I
select p.product_name,year,price from sales s
left join product p on s.product_id = p.product_id

--1581. Customer Who Visited but Did Not Make Any Transactions
select v.customer_id ,count(v.visit_id) as count_no_trans from visits v
left join Transactions t on v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
group by v.customer_id

--197. Rising Temperature


