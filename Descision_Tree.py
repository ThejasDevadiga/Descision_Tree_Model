import pandas as pd
import numpy as np
from Training_Model import training_Model as tm 
from Testing_Model import testing_model as ts
from sklearn.model_selection import train_test_split

	

# from Training_Model import Train_Model

data = pd.read_csv('Data.csv')
 
data['obese'] = (data.Index >= 4).astype('int')
data.drop("Index" , axis=1 , inplace = True)


data['Gender'] = (data["Gender"] =='Male').astype('int')
print(data.info)
# print(np.array(data))

X_train,X_test = train_test_split(data,test_size=0.1,random_state=0)



trained_model = tm(np.array(X_train),45)
trained_model.build_tree(show_tree=False)
testing_model = ts(np.array(X_test),trained_model.root)
testing_model.predict()

# 0.1 : 96 : 45 depth
# 0.2 : 92 : 45th depth
# 0.3 : 91.3 : 43th depth
# 0.4 : 91 : 34th depth
# 0.5 : 91.2 : 38th depth

Height = 173
Weight = 49.93
 
print("Whether Male/Female <Height :",Height,"cm weight :",Weight ,"kg>  is obese ??")
prd = testing_model.predictor(trained_model.root,[1,Height,Weight,1])
obese ="No"
if prd ==1:
    obese ="yes"
print("Excepted :  Yes" ," Got :", obese )
print("Accuracy :",testing_model.accuracy)


