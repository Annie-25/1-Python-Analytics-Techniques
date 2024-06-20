

# Python-Analytics-Techniques
Demo project

## Table of Contents

- [About the project](#about-the-project)
- [Data Description](#data-description)
- [Techniques Applied](#techniques-applied)
- [Detailed Report](#detailed-report)

## About the project

AtliQo is a top telecom company in India, and it announced its 5G intentions in May 2022, alongside other telecom operators.
Following a decline in the growth of their users and revenue after the launch of their 5G plans in May 2022, AtliQo's business director requested a comparative report in order to obtain insights that would allow them to make informed decisions in order to recover their active user rate and other key metrics. They also question if they might improve their internet plans in order to attract more active consumers.
The aim of this project is to construct a data frame that provides a comprehensive look at the KPIs before and after the 5G Launch and perform data visualization and analytics for it using Python software.

## Data Description

The dataset contains the following; date, generation, city and city code, Atliqo’s revenue (crores), arpu, active and unsubscribed users, time period etc.

## Techniques Applied

Data preprocessing,
Data visualizations, and
Geographical visualizations

## Detailed Report

Print () used to view

Shape of Data

The shape attribute, which returns a tuple with two integers (one for column, one for row), displays how many elements are present in each dimension.

<img width="96" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/ea457caf-befe-4510-8223-74b584cde3d0">
 
Size of Data

The size on the other hand basically tells us how many cells are present.

<img width="99" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/f0ec0d3f-872d-4e31-b684-d85d81022d08">
 
Data Cleaning
1.	 <img width="116" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/dd4408ee-7518-4208-a45f-c1893378c7c7">
2.	 <img width="150" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/b64cc87a-cfdd-4fa6-8ed9-b35eaa561e20">

Isnull()
It searches the dataframe for missing values and returns a Boolean value for each element and the sum() function computes the total number of True values The data set was obtained as a cleaned data set from Kaggle.

Data Visualization

Revenue

Code Snippet 1: Revenue before and after 5G

<img width="495" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/b9eb98ed-6ffe-4137-b20d-57ece8f36541">

Output 1

<img width="324" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/354002f2-3e6f-40e6-8259-30ce96797899">

Findings 1

The line graph shows the trend in revenue before and after 5G. The horizontal axis is labeled as “Month” and the vertical axis as “Revenues/crores. Note that, from January to April is ‘before 5G’ while from June to September is ‘after 5G’. As shown in the graph, we see a decrease in the revenue right after the 5G is introduced. However, the revenue significantly increased in the month of August only to fall again in the month of September

Code Snippet 2: City with highest revenue before and after 5G

<img width="492" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/b40bca11-126c-4a8b-91dc-a3eb6512b7e7">

Output 2

<img width="314" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/7447f7d6-5e16-41e6-b335-c27fff9d5819">
 
Findings 2

The scatter plot above shows the revenue made per city. The horizontal axis of the graph is labeled with “City”, and the vertical axis of the graph is labeled with “Revenue/Crores”. By analyzing the scatter plot, we see that the clustering of data points seems to move upwards from left to right. This shows that there is a strong positive relationship between the values.  It is important to know that the plot does not prove causation between revenue and city – they are just correlated. For example; there is a tighter clustering of data points for Lucknow compared to the other cities. Thus, Lucknow recorded the highest revenue both before and after 5G.

Average Revenue Per User (ARPU)

Code Snippet: ARPU before and after 5G
 
<img width="477" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/5ad77c3f-f012-4467-a0cb-d38913f604c9">

Output

ARPU before and after 5G

<img width="321" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/ed51d7c3-16f9-4465-9436-d6c5e8e9d5f3">

Findings  

The horizontal bar graph above indicates the average revenue per user (ARPU) before and after 5G. The horizontal axis is labeled with “ARPU”, and the vertical axis is labeled with “Gen”. From the above graph, we see that, Atliqo recorded its highest average revenue per user (i.e. 250) after 5G. This might be due to the high cost of 5G product/service.

Active Users

Code Snippet 1: Active users before and after 5G

 <img width="479" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/0823c3d9-6385-4f5d-b691-39ce2e64911e">

Output 1

Active users before and after 5G

 <img width="303" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/94affa65-5288-4af9-ae9a-a48508fcefcb">

Findings 1
The bar graph above indicates the number of active users per month. The horizontal axis is labeled with “Month” and the vertical axis with “Active Users”. By looking at the graph, we noticed that the months of February and March (before 5G) recorded the highest number of active users while July (after 5G) recorded the least number of active users.

Code Snippet 2: City with highest number of active users

<img width="468" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/de4311a9-7f3f-4069-9751-a5f94a977712">

Output 2: 

City with highest number of active users

<img width="329" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/d6bff32b-1892-41cd-bd28-5fa79d0ec1bf">

Findings 2
The horizontal bar graph above indicates the number of active users in each city. The horizontal axis is labeled with “Active Users/Lakhs” and the vertical axis with “City”. From the graph, we found that two cities: Raipur and Lucknow recorded the highest number of active users/lakhs.  While Coimbatore recorded the least number of active users/lakhs.

Unsubscribers (Churn Rate)

Code Snippet 1: Number of unsubscribers per city

<img width="492" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/3b7ff5ed-3e96-4049-bdcf-75721e0cc7fd">

Output 1

Number of unsubscribers per city

<img width="385" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/991c5fc7-cf63-4b45-8e7e-6913dcb7b400">

Findings 1
The pie chart shows the number of unsubscribers per city. The variables are; Lucknow, Delhi, Raipur, Ahmedabad and Coimbatore. From the pie chart we see that;
•	Lucknow recorded the highest number of unsubscribers being 40%
•	The next highest number of unsubscribers is found in Delhi, being 33%
•	Following suite is Raipur with 13% of unsubscribers.
•	Ahmedabad and Coimbatore both had 7% each of unsubscribers 

Code Snippet 2: 

Number of unsubscribers before and after 5G

<img width="468" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/a57698b3-b696-4154-942b-602142d0b3b3">

Output 2

Number of unsubscribers before and after 5G

 <img width="300" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/6157cc13-da96-4eca-8617-8abd36ae8385">

Findings 2
The bar graph depicts the number of unsubscribers/lakhs before and after 5G. The horizontal axis is labeled with “Gen” and the vertical axis is labeled with “Unsubscribers/Lakhs”.  The graph revealed that the number of unsubscribers/lakhs increased after 5G.         
 
Geographical Visualization

Code Snippet

<img width="348" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/1c4b1f9b-a6a8-4a40-b364-8639f6d93ce4">

These are the software packages needed to plot the map.

<img width="330" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/b5e98ef6-0090-4b87-8d81-e5be0bf9ff78">

This code is to read and run the file to show its headings and first five rows.
 
<img width="279" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/c9799254-83d9-4151-b263-3a7bfaa14bf5">

<img width="228" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/050ea587-ab66-47d9-87ac-5b8c65c93500">

This code is to merge two data sets.

<img width="488" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/655dfb76-da4e-4467-84ee-3538f3a56125">

Fig – figure
xy – latitude and longitude of the geo spatial data
ax -  single object of the axes
Markersize – to create the size of the stars in the map.
plt.show() – to display the map 

Output
 
<img width="381" alt="image" src="https://github.com/Annie-25/Python-Analytics-Techniques/assets/173366226/cb17aa90-881a-4add-a7b5-684ca90fa789">

Findings

The map above shows the geographical locations of Atliqo’s branches in India. The red stars show the various demarcations on the map: Delhi, Lucknow, Raipur, Coimbatore and Ahmedabad.  
Recommendation    
1.	Atliqo should conduct an in-depth market research to find out the preferences of its customers with regards to the 5G network. The findings can then be used to develop internet/subscribing plans for each customer segment. It can be daily, weekly, monthly or 2months subscription plans/packages at affordable plans for each customer segment. 
2.	Atliqo can also add more value by not just providing their technical service but also offering some augmented services like injecting AI and ML into the operational field businesses to help improve their customer experience and overall business operation.            
3.	Atliqo should direct most of their globalized advertising and marketing efforts to locations with their largest customer base, that is, Lucknow and Raipur.                                                                                                            

