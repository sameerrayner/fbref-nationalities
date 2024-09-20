import pandas as pd

df = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2023-2024/nations/2023-2024-Premier-League-Nationalities')[0])
df.drop(range(25, df.shape[0]+1, 26), inplace = True)
df.dropna(inplace = True)
df.drop(['Rk','Min','List'], axis = 1, inplace = True)
df.Nation = df.Nation.str.split(' ', n = 1).str[-1]
df.insert(2, column = 'Season', value = '2023-2024')
df.reset_index(drop = True, inplace = True)

df2 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2022-2023/nations/2022-2023-Premier-League-Nationalities')[0])
df2.drop(range(25, df2.shape[0]+1, 26), inplace = True)
df2.dropna(inplace = True)
df2.drop(['Rk','Min','List'], axis = 1, inplace = True)
df2.Nation = df2.Nation.str.split(' ', n = 1).str[-1]
df2.insert(2, column = 'Season', value = '2022-2023')
df2.reset_index(drop = True, inplace = True)

df3 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2021-2022/nations/2021-2022-Premier-League-Nationalities')[0])
df3.drop(range(25, df3.shape[0]+1, 26), inplace = True)
df3.dropna(inplace = True)
df3.drop(['Rk','Min','List'], axis = 1, inplace = True)
df3.Nation = df3.Nation.str.split(' ', n = 1).str[-1]
df3.insert(2, column = 'Season', value = '2021-2022')
df3.reset_index(drop = True, inplace = True)

df4 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2020-2021/nations/2020-2021-Premier-League-Nationalities')[0])
df4.drop(range(25, df4.shape[0]+1, 26), inplace = True)
df4.dropna(inplace = True)
df4.drop(['Rk','Min','List'], axis = 1, inplace = True)
df4.Nation = df4.Nation.str.split(' ', n = 1).str[-1]
df4.insert(2, column = 'Season', value = '2020-2021')
df4.reset_index(drop = True, inplace = True)

df5 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2019-2020/nations/2019-2020-Premier-League-Nationalities')[0])
df5.drop(range(25, df5.shape[0]+1, 26), inplace = True)
df5.dropna(inplace = True)
df5.drop(['Rk','Min','List'], axis = 1, inplace = True)
df5.Nation = df5.Nation.str.split(' ', n = 1).str[-1]
df5.insert(2, column = 'Season', value = '2019-2020')
df5.reset_index(drop = True, inplace = True)

df6 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2018-2019/nations/2018-2019-Premier-League-Nationalities')[0])
df6.drop(range(25, df6.shape[0]+1, 26), inplace = True)
df6.dropna(inplace = True)
df6.drop(['Rk','Min','List'], axis = 1, inplace = True)
df6.Nation = df6.Nation.str.split(' ', n = 1).str[-1]
df6.insert(2, column = 'Season', value = '2018-2019')
df6.reset_index(drop = True, inplace = True)

df7 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2017-2018/nations/2017-2018-Premier-League-Nationalities')[0])
df7.drop(range(25, df7.shape[0]+1, 26), inplace = True)
df7.dropna(inplace = True)
df7.drop(['Rk','Min','List'], axis = 1, inplace = True)
df7.Nation = df7.Nation.str.split(' ', n = 1).str[-1]
df7.insert(2, column = 'Season', value = '2017-2018')
df7.reset_index(drop = True, inplace = True)

df8 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2016-2017/nations/2016-2017-Premier-League-Nationalities')[0])
df8.drop(range(25, df8.shape[0]+1, 26), inplace = True)
df8.dropna(inplace = True)
df8.drop(['Rk','Min','List'], axis = 1, inplace = True)
df8.Nation = df8.Nation.str.split(' ', n = 1).str[-1]
df8.insert(2, column = 'Season', value = '2016-2017')
df8.reset_index(drop = True, inplace = True)

df9 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2015-2016/nations/2015-2016-Premier-League-Nationalities')[0])
df9.drop(range(25, df9.shape[0]+1, 26), inplace = True)
df9.dropna(inplace = True)
df9.drop(['Rk','Min','List'], axis = 1, inplace = True)
df9.Nation = df9.Nation.str.split(' ', n = 1).str[-1]
df9.insert(2, column = 'Season', value = '2015-2016')
df9.reset_index(drop = True, inplace = True)

df10 = pd.DataFrame(pd.read_html('https://fbref.com/en/comps/9/2014-2015/nations/2014-2015-Premier-League-Nationalities')[0])
df10.drop(range(25, df10.shape[0]+1, 26), inplace = True)
df10.dropna(inplace = True)
df10.drop(['Rk','Min','List'], axis = 1, inplace = True)
df10.Nation = df10.Nation.str.split(' ', n = 1).str[-1]
df10.insert(2, column = 'Season', value = '2014-2015')
df10.reset_index(drop = True, inplace = True)

all_seasons = pd.concat([df,df2,df3,df4,df5,df6,df7,df8,df9,df10])

print(all_seasons)
