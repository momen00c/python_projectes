import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('traning/data/stde.csv')
mean = data['Grade'].mean()
std = data['Grade'].std()
less_than_mean = np.where(data['Grade']<mean,True,False)
grupped = data.groupby(['Department'])#.mean()
mean_for_each_dep = (grupped['Grade'].mean())
data['Status'] = np.where(data['Grade']>=50,'Pass','Fail')
degress_90_80 = (data.loc[(data['Grade'] >80) & (data['Grade']<90)])

dep_names = mean_for_each_dep.index
mean_deg = mean_for_each_dep.tolist()

pie_data = (data['Gender']).value_counts()
number = pie_data.tolist()
mylabel = ['Femal','Male']

dep_cate = data['Department'].unique()
dep_box  =[data[data['Department']==dep]['Grade']for dep in dep_cate]##


his_data = (data['Age']).tolist()
fig,axs = plt.subplots(2, 2, figsize=(12,10))
axs[0,0].bar(dep_names,mean_deg,width=.5)
axs[0,0].set_title('Mean Degree For Each Departments',fontsize=15)
axs[0,0].set_xlabel('Departments',fontsize=12)
axs[0,0].set_ylabel('Mean Of Degrees',fontsize=12)

axs[0,1].pie(number,labels=mylabel,colors = ['#FF9999', '#66B3FF'] )
axs[0,1].set_title('The Proportion For Each Gender',fontsize=15)

axs[1,0].hist(his_data,color='skyblue',edgecolor='black')
axs[1,0].set_title('Histogram For Students Ages',fontsize=15)
axs[1,0].set_xlabel('Ages',fontsize=12)
axs[1,0].set_ylabel('Frequnces',fontsize=12)
axs[1,1].boxplot(dep_box,tick_labels=dep_cate,)
axs[1,1].set_title('Grade Distribution by Department', fontsize=15)
axs[1,1].set_xlabel('Department', fontsize=12)
axs[1,1].set_ylabel('Grade', fontsize=12)

plt.tight_layout()
plt.show()
fig.savefig('student_analysis_dashboard.png')