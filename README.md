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
#### 1.4 Menaxhimi i Zhurmës: 
- Në dataset-in tonë janë analizuar dy lloje të kolonave për zhurmë. Kolona e parë është: Purchase Amount. Rezultati i kësaj kolone me zhurmë duke përdorur boxplot është: 

![Purchase Noisy Before](images/purchase_noisy_before.png)
- Mirepo me përdorimin e metodës IQR(Interquartile Range) e kemi larguar zhurmën në këtë kolonë. Rezultati pas largimit të zhurmës:

![Purchase Noisy Before](images/purchase_noisy_after.png)

- Kolona e dytë është: Category. Rezultati i kësaj kolone me zhurmë duke përdorur boxplot është: 

![Purchase Noisy Before](images/category_noisy_before.png)

- Me reduktimin e zhurmës në këtë kolonë arrihet ky rezultat:

![Purchase Noisy Before](images/category_noisy_after.png)

### 2. Priprocesimi i të dhënave: 
#### 2.1 Reduktimi i dimensionalitetit: 
- Në dataset-in tonë janë përdorur dy kolona për të treguar nëse artikulli ka pasur zbritje dhe nese është përdorur kodi i zbritjës. Përdorimi i njerës afekton tjetrën, kështu që e kemi shtuar një kolonë të re që i përfaqson këto dy kolona, dhe rezultati i dataset-it duket kështu:

![Dimensinality Reduction](images/dimensinality_reduction.png)

#### 2.2 Mostrimi i të dhënave: 
- Ne kemi paraqitur gjininë më të shpeshtë për shitje gjatë stinëve të ndryshme për ta paraqitur mostrimin. Rezultati para mostrimit:

![Sampling Before](images/sampling_before.png)

- Ndërsa rezultati pas mostrimit, duke i marrur vetëm 500 rreshta duket kështu:

![Sampling After](images/sampling_after.png)

#### 2.3 Agregimi i të dhënave: 
- Një nga shembujt se si e kemi përdorur agregimin është shuma totale e blerjeve sipas kategorisë:

![Aggregation](images/aggregation.png)

#### 2.4 Zgjedhja e nën bashkësisë së vetive: 
- Rezultati i arritur në shembullin se si e kemi përdorur zgjedhjen e nën bashkësisë së vetive duket kështu:

![Exmplae of use](images/example_of_use.png)

#### 2.5 Krijimi i vetive: 
- Rezultati i arritur në shembullin se si e kemi përdorur krijimin e vetive duket kështu:

![Exmplae of use 1](images/example_of_use_1.png)

#### 2.6 Binarizimi: 
- Rezultati i arritur në shembullin se si e kemi përdorur binarizimin duket kështu:

![Binnings](images/binnings.png)

#### 2.6 Transformimi: 
- Rezultati i arritur në shembullin se si e kemi përdorur transformimin duket kështu:

![Tranfromation](images/tranfromation.png)

### 3. Krijimi i datasetit të procesuar: 
- Pasi qe e kemi përfunduar priprocesimin e të dhënave, rezultati përfundimtar ruhet tek folderi files me emrin "Preprocessed_Shopping_Trends_Dataset": 

![Tranfromation](images/preprocessed_df.png)

#### 3.1 Kompresimi: 
- Pasi qe e kemi përfunduar priprocesimin e të dhënave e kemi bërë edhe kompresimin e tyre: 

![Compresion](images/compresion.png)


## Kontributi
Blerona Idrizi

Vlora Gjoka