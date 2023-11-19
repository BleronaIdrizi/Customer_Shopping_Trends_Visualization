# Customer Shopping Trends Dataset
Ky projekt në lendën: *Përgatitja dhe vizualizimi i të dhënave* analizon "Customer Shopping Trends Dataset", duke ofruar një pasqyrë të thellë mbi sjelljet dhe preferencat e blerjeve të konsumatorëve. Duke përdorur teknika të avancuara të parapërgatitjes dhe analizës së të dhënave, ne synojmë të paraqesim disa ide se si mund ti ndihmojmë bizneset të përshtaten në nevojat e klientëve të tyre. Projektim, ekzekutimi dhe analiza e të dhënave janë bërë me qëllim të përmirësimit të strategjive të marketingut dhe ofertave të bizneseve, duke kontribuar drejt një përvoje më të personalizuar për konsumatorin.

**[Customer Shopping Trends Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset/data)** from **[Kaggle](https://www.kaggle.com)**.

## Startimi i projektit
1. Se pari bëni instalimin e python-it në pajisjen e juaj.
2. Klonimi i projektit:  **[Customer Shopping Trends Dataset](https://github.com/BleronaIdrizi/Customer_Shopping_Trends_Visualization)**.
3. Ekzekutimi i komandës për instalimin e librarive në direktoriumin ku është i vendosur projekti:
```python
pip3 install -r requirements.txt
```

## Teknikat e Vizualizimit
- Boxplots për analizën e outliers dhe zhurmës.
- Pie Charts për të paraqitur shpërndarjen gjinore nëpër stinë.
- Grafikë me shtylla për të paraqitur shumat totale të blerjeve sipas kategorisë.

## Disa rezultate tona në priprocesimin e të dhënave
### 1. *Kualiteti i të dhënave*: 
#### 1.1 *Menaxhimi vlerave *null**: 
- Në dataset-in tonë janë gjetur disa lloje të ndryshme të kolonave me vlera *null*.

![Null Values](images/null_values_before.png)
- Vlerat *null* të kolonës "Age" i kemi trajtuar duke zevëndësuar me moshën mesatare, ndërsa vlerat null të kolonave tjera i kemi injoruar.

#### 1.2 *Menaxhimi i duplikateve*: 
- Në dataset-in tonë i janë gjetur disa duplikate:

![Duplicates](images/duplicates.png)
- Pas ekzektuimi të komandës për gjetjen e rreshtave duplikat e kemi ekzekutuar komandën për largimin e duplikateve.

#### 1.3 *Menaxhimi i Outliers*: 
- Në dataset-in tonë kolona Age është gjetur si Outlier dhe me përdorimin e paketës seaborn e kemi shfaqur datasetin se si duket me Ouliers:

![Outliers After](images/outliers_before.png)
- Mirepo me përdorimin e metodës Z-Score i kemi larguar Outliers. Rezultati pas largimit të Outliers:

![Outliers Before](images/outliers_after.png)
