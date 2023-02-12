import matplotlib.pyplot as plt
import pandas as pd
from thefuzz import fuzz
import numpy as np

path = 'file://localhost/Users/user/fun-projects/flask-dataset-sharks/database/fatal_shark_attacks.xls'

df = pd.read_excel(io=path)
df = df.drop(columns=["Date", "Time"])

# By Gender
males = df['Sex'].tolist().count("Male")
females = df['Sex'].tolist().count("Female")
total_cases = len(df.index)
no_sex_info = total_cases - females - males

df2 = pd.DataFrame(
    data={"Males": males, "Females": females, "N/A": no_sex_info}, index=[0])
df2.index = ['Total']
fig1 = df2.plot(kind='bar', stacked=True, figsize=(
    6, 6), rot=0, xlabel='', ylabel='Cases')
for c in fig1.containers:
    lab = [v.get_height() if v.get_height() > 0 else '' for v in c]
    fig1.bar_label(c, labels=lab, label_type='center')
plt.savefig('./static/img/gender.png')
plt.close()

# By State
df3 = df.groupby(['state']).size()
fig2 = df3.plot(kind='bar', figsize=(
    6, 6), rot=0, xlabel='State', ylabel='Cases')
plt.setp(fig2.get_xticklabels(), fontsize=8,
         rotation=15, horizontalalignment='right')
plt.savefig('./static/img/state.png')
plt.close()

# By Activity
df4 = pd.read_excel(io=path)
df4 = df4.drop(columns=["Date", "Time", "Age", "Area",
               "Sex", "Age", "Injury", "Time", "Species", "state", "Year"])
df4["Activity"].fillna('no data', inplace=True)

# Option 1
# Levenshtein Distance metric
# for i in df4["Activity"].unique():
#     if len(i) != 0 or len(i) > 20:
#         df4[i] = df4["Activity"].apply(
#             lambda x: fuzz.ratio(x, i) >= 65
#         )
#         m = np.min(df4[df4[i] == True]["Activity"])
#         df4.loc[df4.Activity == i, 'group'] = m

# print(df4)
# print(df4.groupby('group').count())

# Option 2
activities = {"Swimming": 0, "Diving": 0, "Surfing": 0,
              "Sailing": 0, "Fishing": 0, "Other": 0}
act = []
for i in df4["Activity"]:
    i = i.lower()
    if 'sw' in i or i.startswith('sw') or 'bath' in i or "floa" in i:
        activities["Swimming"] += 1
    elif 'div' in i:
        activities["Diving"] += 1
    elif 'surf' in i or 'boarding' in i:
        activities["Surfing"] += 1
    elif 'sai' in i or 'ship' in i or 'boat' in i:
        activities["Sailing"] += 1
    elif 'fish' in i:
        activities["Fishing"] += 1
    else:
        activities["Other"] += 1

act = [k for item in [activities] for k, v in item.items()]
nums = [v for item in [activities] for k, v in item.items()]

df5 = pd.DataFrame({'activity': act, 'cases': nums})


df5.set_index('activity', inplace=True)
plt = df5.plot(kind='pie', y='cases', title="By activities",
               autopct='%1.1f%%', startangle=0, figsize=(6, 6))
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1), fontsize=8)
plt.figure.savefig('./static/img/act.png')
plt.figure.close()
