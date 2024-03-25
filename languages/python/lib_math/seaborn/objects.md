# OBJECTS

## plots

`heatmap(df: pandas.DataFrame, annot: bool, cmap, linewidths: float)` :  
*	e.g.: `sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)`

`pairplot(df: pandas.DataFrame, hue, palette)` :  
*	e.g.:  `sns.pairplot(df, hue="Targets", palette="Set1")`
