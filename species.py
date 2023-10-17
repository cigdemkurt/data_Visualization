import seaborn as sns
from pandas.api.types import CategoricalDtype
iris = sns.load_dataset('iris')
df = iris.copy()
species_categories = ["virginica","setosa","versicolor"]
df.species = df.species.astype(CategoricalDtype(categories = species_categories, ordered = True))
df.head()

kat_df = df.select_dtypes(include = ["object"])
kat_df.head()

sns.catplot(x = "species", y = "sepal_length", data = df);

sns.barplot(x = "species", y = "sepal_length", hue = "sepal_width", data = df);