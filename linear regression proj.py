
# # Linear Regression Model Project//

# PROJECT DESCCRIPTION:
# Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. 
#Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.  
# The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out! Let's get started!
 # Just follow the steps below to analyze the customer data (it's fake, don't worry I didn't give you real credit card numbers or emails).

#  Imports



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# 
# We'll work with the Ecommerce Customers csv file from the company. It has Customer info, suchas Email, Address, and their color Avatar. Then it also has numerical value columns:
# 
# * Avg. Session Length: Average session of in-store style advice sessions.
# * Time on App: Average time spent on App in minutes
# * Time on Website: Average time spent on Website in minutes
# * Length of Membership: How many years the customer has been a member. 



customers=pd.read_csv('Ecommerce Customers')


# **Check the head of customers;


customers.head()


customers.describe()


customers.info()


# ## Exploratory Data Analysis
# 
# **Let's explore the data!**

# **Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?**


sns.set_paletee('Gnbu_d')
sns.set_style('whitegrid')





sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)


# ** Do the same but with the Time on App column instead. **



sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)


# ** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**



sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)


# **Let's explore these types of relationships across the entire data set. 


sns.pairplot(customers)


# **Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?**

# In[x]:


#length of Membership


# **Create a linear model plot (using seaborn's lmplot) of  Yearly Amount Spent vs. Length of Membership. **

# In[16]:


sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)


# ## Training and Testing Data
# 
# Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
# ** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **

# In[21]:


y=customers['Yearly Amount Spent']


# In[27]:


X=customers[['Avg. Session Length','Time on App','Time on Website','Length of Membership']]


# ** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101**

# In[30]:


from sklearn.model_selection import train_test_split


# In[31]:


X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=101)


# ## Training the Model
# 
# Now its time to train our model on our training data!
# 
# ** Import LinearRegression from sklearn.linear_model **

# In[33]:


from sklearn.linear_model import LinearRegression


# **Create an instance of a LinearRegression() model named lm.**

# In[34]:


lm=LinearRegression()


# ** Train/fit lm on the training data.**

# In[35]:


lm.fit(X_train,y_train)


# **Print out the coefficients of the model**

# In[36]:


print('Coefficients: \n',lm.coef_)


# ## Predicting Test Data
# Now that we have fit our model, let's evaluate its performance by predicting off the test values!
# 
# ** Use lm.predict() to predict off the X_test set of the data.**

# In[39]:


predictions=lm.predict(X_test)


# ** Create a scatterplot of the real test values versus the predicted values. **

# In[41]:


plt.scatter(y_test,predictions)
plt.xlabel('Y test')
plt.ylabel('PREDICTED Y')


# ## Evaluating the Model

# Let's evaluate our model performance by calculating the residual sum of squares .

# ** Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. 

# In[43]:


from sklearn import metrics
print('MAE:',metrics.mean_absolute_error(y_test,predictions))
print('MSE:',metrics.mean_squared_error(y_test,predictions))
print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,predictions)))


# ## Residuals

# You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data. 

# **Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().**

# In[45]:


sns.displot((y_test-predictions),bins=50);


# ## Conclusion
# We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development?
#Or maybe that doesn't even really matter, and Membership Time is what is really important. 
#Let's see if we can interpret the coefficients at all to get an idea.
# 
# ** Recreate the dataframe below. **

# In[47]:


coeffecients=pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns=['Coeffecient']
coeffecients

#OUTPUT FOR PREDICTIVE ANALYSIS :
#Coeffecient
#Avg. Session Length	25.981550
#Time on App	38.590159
#Time on Website	0.190405
#Length of Membership	61.279097

#CONCLUSION FROM THE ANALYSIS AND MODELLING:
# ** How can you interpret these coefficients? **

# - Holding all other features fixed, a 1 unit increase in **Avg. Session Length** is associated with an **increase of 25.98 total dollars spent**.
#- Holding all other features fixed, a 1 unit increase in **Time on App** is associated with an **increase of 38.59 total dollars spent**.
#- Holding all other features fixed, a 1 unit increase in **Time on Website** is associated with an **increase of 0.19 total dollars spent**.
#- Holding all other features fixed, a 1 unit increase in **Length of Membership** is associated with an **increase of 61.27 total dollars spent**.

# **Do you think the company should focus more on their mobile app or on their website?**

# 

# ## Great Job!
# # #END
#THANK YOU
