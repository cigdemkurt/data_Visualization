import seaborn as sns
exercise = sns.load_dataset('exercise')
df =exercise.copy() #gerçeği üzerinde değişim olmaması için kopya al

df.info()

df.describe().T #transpose alarak tanımına bakmak

df.head() #ilk 5 elemanı gözlemle

df["time"].value_counts() #time içeriğinin sayıları

from pandas.api.types import CategoricalDtype #sırasal

df.time.head()

df.cut = df.time.astype(CategoricalDtype(ordered = True)) #sıraya izin ver

df.dtypes

time_categories= ["30 min", "15 min", "1 min"] #indexleri değiştir

df.time.head(1)

df["time"].value_counts().plot.barh().set_title("Time Değişkeninin Sınıf Frekansları");


sns.barplot(x = "time", y = df.time.index, data= df);