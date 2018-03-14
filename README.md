# Iris

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".
Dataset is present in the file "iris.data.txt" in the current directory.
Training on 80% of data and validation on 20% of data 


**Results observed:**

```
Accuracy: 0.933333333333``
```
```
Confusion matrix: 
 [[ 7  0  0]
 [ 0 10  2]
 [ 0  0 11]]
```
**classification_report::**
```
              precision    recall  f1-score   support

Iris-setosa       1.00      1.00      1.00         7
Iris-versicolor   1.00      0.83      0.91        12
Iris-virginica    0.85      1.00      0.92        11

avg / total       0.94      0.93      0.93        30
```
