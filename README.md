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

## Tipet e atributeve
1. Kategoriale(Kualitative)
    - Nominale: Gender, Item Purchased, Category, Location, Color, Season, Subscription Status, Shipping Type, Discout Applied, Promo Code Used, Payment Method.
    - Ordinale: Review Rating, Size, Frequency of Purchases.
2. Numerike(Kuantitative)
    - Interval: Age, Previous Purchases.
    - Ratio: Customer ID, Purchase Amount (USD).

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

# FAZA 2

## Outliers
Ky seksion përmban hapat e ndërmarrë për identifikimin dhe trajtimin e outliers në setin e të dhënave. Analiza e outliers është e rëndësishme për të siguruar saktësinë dhe cilësinë e modeleve statistikore dhe të nxjerrjes së përfundimeve.

### Shembulli i moshës

Metoda që përdorim për të identifikuar outliers është e bazuar në analizë statistikore, duke përdorur vizualizimin e boxplot. Ky lloj grafiku na ndihmon të shohim vlerat që shfaqen jashtë intervalit të zakonshëm të të dhënave.

```python
import seaborn as sns
import pandas as pd

# Kemi një DataFrame të quajtur 'df' që përmban kolonën 'Age'.
# Për të vizualizuar outliers në moshë, ekzekutojmë këtë kod:

sns.boxplot(df['Age'], orient='h')

# Kështu krijohet një boxplot horizontal që shfaq moshën.
# Vlerat e identifikuara si outliers janë të shënuara me pika të veçanta
# jashtë kutisë qendrore të grafikut.

```
### Analiza e Outliers

 DBSCAN është një algoritem klasifikimi bazuar në dendësi që ndihmon në identifikimin e grupeve (clusters) të dendura me pikat e jashtme si outliers.

![statistics before](images/outliers_statistics_before.png)

#### Procesi i përpunimit të të dhënave dhe aplikimi i DBSCAN

Fillimisht, kemi konvertuar kolonat e nevojshme në vlera numerike dhe kemi selektuar kolonat për grupim. Pastaj kemi standardizuar karakteristikat për të përmirësuar performancën e DBSCAN.

```python
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Konverto vlerat në vlera numerike
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Purchase Amount (USD)'] = pd.to_numeric(df['Purchase Amount (USD)'], errors='coerce')

# Selektimi i kolonave për grupim
X = df[['Age', 'Purchase Amount (USD)']]

# Standardizimi i karakteristikave
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.dropna())

# Aplikimi i DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)
```
![dbscan](images/outliers_dbscan.png)

### Identifikimi i Outliers me KMeans Clustering

KMeans është një algoritem i njohur i grumbullimit që ndan të dhënat në grupe bazuar në ngjashmërinë e tyre.

#### Procesi i përpunimit të të dhënave dhe aplikimi i KMeans

Ne fillim zgjodhëm kolonat e nevojshme dhe pastaj pastruam të dhënat për të hequr vlerat që mungojnë. Pas kësaj, ne inicializuam modelin KMeans me një numër të caktuar të qendrave të grupimeve dhe e trajnuam atë me të dhënat tona të pastruara.

```python
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import plotly.express as px

# Zgjedhja e kolonave të nevojshme nga DataFrame
data_selected = df[['Age', 'Purchase Amount (USD)']]

# Pastrimi i të dhënave dhe përdorimi i KMeans
data_selected_clean = data_selected.dropna()
kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(data_selected_clean)

# Llogaritja e distancës nga qendrat e grupimeve
distanca = cdist(data_selected, kmeans.cluster_centers_, 'euclidean')
distancia_minimale = np.min(distanca, axis=1)
df['distanca_deri_te_qendra'] = distancia_minimale
```

![Kmean](images/outliers_kmean.png)

### Identifikimi i Outliers me metodën Z-Score

Në këtë pjesë, kemi përdorur metoden Z-Score për të gjetur dhe larguar outliers në të dhënat e moshës. Metoda Z-Score përdor mesataren dhe devijimin standard për të përcaktuar kufijtë e vlerave normale dhe atyre anomale.

#### Gjetja e kufijve me Z-Score

Për të përcaktuar kufijtë, ne kemi llogaritur mesataren dhe devijimin standard të moshës dhe kemi vendosur kufijtë si mesatare plus ose minus tre herë devijimi standard. Ja si duket kodi i përdorur:

```python
import pandas as pd

# Llogaritja e kufijve të sipërm dhe të poshtëm
upper_limit = df['Age'].mean() + 3*df['Age'].std()
lower_limit = df['Age'].mean() - 3*df['Age'].std()
print('Limiti i sipërm:', upper_limit)
print('Limiti i poshtëm:', lower_limit)
```
#### Largimi i të dhënave që janë përcaktuar si Outliers

Pas identifikimit të outliers me metoden Z-Score, ne kemi vijuar me largimin e tyre nga dataseti për të përmirësuar cilësinë e analizave të mëtejshme.

```python
# Largimi i outliers dhe krijimi i një dataseti të pastër
new_df = df.loc[(df['Age'] <= upper_limit) & (df['Age'] >= lower_limit)]

# Shfaqja e numrit të rreshtave përpara dhe pas largimit të outliers
print('Para largimit të Outliers:', len(df))
print('Pas largimit të Outliers:', len(new_df))
print('Outliers:', len(df) - len(new_df))
```

![statistics after](images/outliers_statistics_after.png)

### Shembulli i analizës së ngjyrave

Në këtë pjesë të analizës, ne kemi shqyrtuar frekuencën e secilës ngjyrë në kolonën e ngjyrave të datasetit tonë. Ky hap është i rëndësishëm për të kuptuar shpërndarjen e të dhënave dhe për të identifikuar ndonjë tendencë ose anomali.

#### Llogaritja dhe vizualizimi i frekuencës së ngjyrave

Ne fillim llogaritëm frekuencën e secilës ngjyrë duke përdorur metoda `value_counts()` dhe më pas e vizualizuam këtë shpërndarje duke përdorur një barplot nga seaborn.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Llogaritja e frekuencës së secilës ngjyrë
color_counts = df['Color'].value_counts()

# Vizualizimi i frekuencës së ngjyrave
plt.figure(figsize=(10, 6))
sns.barplot(x=color_counts.index, y=color_counts.values)
plt.title("Frekuenca e ngjyrave")
plt.xlabel("Color")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
```
![statistics color before](images/outliers_before_color.png)

### Largimi i Outliers nga kolona e ngjyrave

Në këtë pjesë, ne kemi trajtuar outliers që janë identifikuar në kolonën e ngjyrave të datasetit tonë. Kemi krijuar një listë të ngjyrave të konsideruara si outliers dhe më pas kemi larguar të gjitha rreshtat ku ngjyra është pjesë e kësaj liste.

#### Procesi i largimit të Outliers

Kemi përdorur listën e ngjyrave outliers për të krijuar një DataFrame të ri pa këto outliers:

```python
# Krijimi i listës së ngjyrave outliers
outlier_colors = potential_outliers.index.tolist()

# Largimi i rreshtave ku 'Color' është në listën e ngjyrave outlier
df = df[~df['Color'].isin(outlier_colors)]
```

![statistics color after](images/outliers_after_color.png)

## Noisy Data

Pas trajtimit të outliers, një pjesë tjetër kritike e pastrimit të të dhënave është identifikimi dhe trajtimi i të dhënave me zhurmë. Në këtë seksion, kemi shtuar zhurmë të qëllimshme në kolonën numerike për të simuluar të dhënat me zhurmë dhe për të treguar metodat e pastrimit.

### Shtimi i zhurmës në një kolonë numerike

Për të simuluar të dhënat me zhurmë, kemi shtuar vlera të rastësishme nga një shpërndarje normale te vlerat e kolonës 'Purchase Amount (USD)'.

```python
import numpy as np
import pandas as pd

# Vendosja e seed për reproducueshmëri
np.random.seed(42)

# Shtimi i zhurmës
kolona_zhurme = 'Purchase Amount (USD)'
df[kolona_zhurme] = df[kolona_zhurme] + np.random.normal(0, 20, size=len(df))
```

![noisy data ex one](images/noisy_data_ex_one_before.png)

### Vizualizimi i të dhënave me zhurmë

Pas shtimit të zhurmës në të dhënat, është e rëndësishme të kryejmë vizualizime për të vlerësuar ndikimin e zhurmës në të dhënat. Këtu kemi përdorur një boxplot për të paraqitur shpërndarjen e vlerave në kolonën 'Purchase Amount (USD)' pas shtimit të zhurmës.

#### Krijimi i Boxplot

Kodi i mëposhtëm tregon si të dhënat e kolonës së përzgjedhur janë vizualizuar për të identifikuar ndryshimet e shkaktuara nga zhurma:

```python
import matplotlib.pyplot as plt

# Vizualizimi i boxplot për kolonën me zhurmë
plt.boxplot(df[kolona_zhurme])
plt.title(f'Boxplot i {kolona_zhurme} (Para Pastrimit)')
plt.show()
```
![noisy data ex one](images/noisy_data_ex_one_boxplot.png)

### Trajtimi i të dhënave me zhurmë duke përdorur metodën IQR

Një metodë efektive për trajtimin e të dhënave me zhurmë është përdorimi i interquartile range (IQR), e cila ndihmon në identifikimin dhe heqjen e outliers që mund të konsiderohen si zhurmë.

#### Heqja e Outliers me IQR

Fillimisht, kemi llogaritur vlerat e parë dhe të tretë të quartilit (Q1 dhe Q3) dhe më pas kemi përcaktuar kufijtë për outliers si më poshtë:

```python
# Llogaritja e IQR dhe kufijve për outliers
Q1 = df[kolona_zhurme].quantile(0.25)
Q3 = df[kolona_zhurme].quantile(0.75)
IQR = Q3 - Q1
limiti_i_ulët = Q1 - 1.5 * IQR
limiti_i_lartë = Q3 + 1.5 * IQR
```

![noisy data ex one](images/noisy_data_ex_one_after.png)

### Shtimi i zhurmës dhe pastrimi në një kolonë string

Në përpjekjen tonë për të menaxhuar të dhënat me zhurmë, kemi aplikuar një funksion që shton zhurmë në një kolonë string. Kjo metodë simulon të dhënat reale që mund të përmbajnë gabime ose vargje të rastësishme.

#### Shtimi i zhurmës në kolonën "Category"

Kemi përdorur një funksion të përcaktuar paraprakisht për të shtuar zhurmë në kolonën "Category". Kjo zhurmë mund të jetë në formën e kategorive të rastësishme që imitojnë të dhënat jo të sakta.

```python
# Funksioni për shtimin e zhurmës është thirrur këtu
shto_zhurme_ne_kategori(df)
```
![noisy data ex two](images/noisy_data_ex_two_before.png)

### Heqja e të dhënave me zhurmë nga kolona kategorike

Në këtë seksion, ne trajtojmë të dhënat me zhurmë në kolonën kategorike 'Category'. Kemi aplikuar një metodë për të zëvendësuar të dhënat e zhurmshme me një vlerë të zbrazët dhe më pas kemi larguar rreshtat me këto vlera të zbrazëta.

#### Zëvendësimi dhe largimi i të dhënave me zhurmë

Për të larguar të dhënat me zhurmë, fillimisht zëvendësojmë çdo instancë të listës së vlerave të zhurmshme me vlera të zbrazëta, dhe më pas heqim rreshtat që përmbajnë këto vlera të zbrazëta nga DataFrame.

```python
# Zëvendësimi i të dhënave me zhurmë me vlera të zbrazëta
df['Category'] = df['Category'].replace('|'.join(lista_e_kategorive_zhurme), '')

# Largimi i rreshtave ku 'Category' është zbrazët
df = df[df['Category'] != '']
```
![noisy data ex two](images/noisy_data_ex_two_after.png)

### Analiza e SMOTE Algoritmit

Paraqitje e SMOTE Algoritmit:

![smote analyze befroe](images/smote_analyze_before.png)
![smote analyze befroe 3d](images/smote_analyze_3d_before.png)

Paraqitje e datasetit me KMeans algoritmin

Para:
![kmeans before](images/kmeans_before.png)

Pas:
![kmeans after](images/kmeans_after.png)

### Analiza e Skewness në të dhënat

Në këtë seksion, demonstruam si të analizojmë shpërndarjen e të dhënave që nuk janë simetrike, duke përdorur një shembull të të dhënave të shtrembëruara. Kjo shpërndarje është zakonisht karakteristike e të dhënave reale dhe mund të ndikojë në zbatimin e teknikave statistikore.

Për qëllime demonstrative, kemi gjeneruar një set të dhënash eksponenciale me një shtrembërim të caktuar:

```python
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(0)
data = np.random.exponential(scale=2.0, size=1000)

```

Para:
![Skewness data before](images/skewness_before.png)

Pas:
![Skewness data before](images/skewness_after.png)

# Saktësia e modelit

Për të balancuar të dhënat në një problem të klasifikimit ku ekziston një mospërputhje mes klasave, është përdorur teknika e Synthetic Minority Over-sampling Technique (SMOTE). Kjo teknikë lejon krijimin e mostrave sintetike për klasën minoritare. Ky qasja përmirëson saktësinë e modelit duke siguruar që modeli trajnohet në një mënyrë më të balancuar dhe më të drejtë për të gjitha klasat.


```python
# Pjesa ku ndajmë të dhënat në trajnuese dhe testuese
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Zbatimi i SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# Trajnimi i modelit
model = RandomForestClassifier(random_state=42)
model.fit(X_resampled, y_resampled)

# Parashikimi dhe vlerësimi i modelit
predictions = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, predictions))
```

![Acurrency](images/acurrency.png)

# Faza 3

# Kontributi
Blerona Idrizi

Vlora Gjoka