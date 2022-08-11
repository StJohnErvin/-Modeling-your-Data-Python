## Data Analysis Steps

## 1. Define the questions.

# 1. What are the yearly sales trend?
# 2. Which product sild the most in 2016?
# 3. Among the three product categories which one had the lowest sale in 2018?
# 4. What is the yearly sales trend of the 3 customer group
# 5. Are we getting more corporate customers 

## Collect data
import pandas as pd

train = pd.read_csv('train.csv')
train.head()

train.info()

train.isnull().sum()

train[train['Postal Code'].isna()]

## fill in null values with non-null values
train['Postal Code'] = train['Postal Code'].fillna('05401')
train.info()
train.isnull().sum()

train.head()

# deleting a column
del train['Row ID']

train.head(2)

train.info()

# converting object to datetime
train['Order Date'] = pd.to_datetime(train['Order Date'], format='%d/%m/%Y')
train['Ship Date'] = pd.to_datetime(train['Ship Date'], format='%d/%m/%Y')

# Converting float to object
train['Postal Code'] = train['Postal Code'].astype(str)

train.info()

## Modeling Data Starts here
## Analyze the data
# What is the yearly sales trend?

train.head()

# Create order year column
train['Order Year']=train['Order Date'].dt.year

train.info()
train.head(2)

train['Order Year'] = train['Order Year'].astype(str)
train.info()

# Sum of sales by year

ysales= train.groupby('Order Year', as_index = False).agg({'Sales':'sum'})
ysales

## Q2 Which Product SOld the most in 2018

sales_2018=train[train['Order Year'] == '2018']
sales_2018.head()

# arrange data result

product = sales_2018.groupby('Product Name', as_index = False).agg({'Sales':'sum'})
p=sales_2018.sort_values(by = 'Sales', ascending = False)
p.head(10)

## Q3 lowest sales in 2018 ?

psales = sales_2018.groupby('Category', as_index = False).agg({'Sales':'sum'})
psales

## Q4 what is the yearly sales trend of the 3 customer groups

cons_segment= train[train['Segment'] == 'Consumer']
consumer = cons_segment.groupby('Order Year', as_index = False).agg({'Sales':'sum'})
consumer

home_segment = train[train['Segment'] == 'Home Office']
home = home_segment.groupby('Order Year', as_index = False).agg({'Sales':'sum'})
home

corp_segment = train[train['Segment'] == 'Corporate']
corporate = corp_segment.groupby('Order Year', as_index = False).agg({'Sales':'sum'})
corporate
sns.lineplot(x='Order Year', y='Sales', data = ysales, marker = "o")
plt.xlabel('')
plt.show()

p_top = p[(p['Sales']>=4416.174)]

sns.barplot(y="Product Name", x = "Sales", data = p_top, ci=False, orient='h', color='grey')
plt.title('Top Products in 2018')
plt.ylabel('')
plt.show()

sns.barplot(x="Category", y="Sales", data = psales, palette = 'Blues')
plt.title('Sales by Product Category')
plt.xlabel('')
plt.ylabel('')

plt.show()

sns.lineplot(x='Order Year', y='Sales', data = consumer, marker = "o")
sns.lineplot(x='Order Year', y='Sales', data = home, marker = "o")
sns.lineplot(x='Order Year', y='Sales', data = corporate, marker = "o")

plt.legend(['consumer','home','corporate'], fontsize=8)
plt.show()


