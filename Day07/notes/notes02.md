Here are **detailed notes on Pandas**, tailored specifically to help you **build and understand mini projects** like your **IoT telemetry analysis**.

---

## 🐼 Pandas Notes for Mini Projects

---

### 1. **What is Pandas?**

* **Pandas** is a Python library for data manipulation and analysis.
* It provides two core data structures:

  * `Series` – 1D labeled array
  * `DataFrame` – 2D labeled table

---

### 2. **Importing and Reading Data**

```python
import pandas as pd

# From CSV file or URL
df = pd.read_csv("filename.csv")
df = pd.read_csv("https://example.com/data.csv")

# Other formats
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
```

---

### 3. **Inspecting Data**

```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.shape            # Rows, Columns
df.columns          # Column names
df.info()           # Data types + non-null values
df.describe()       # Summary statistics (numeric)
df.dtypes           # Data types of each column
```

---

### 4. **Accessing Data**

```python
df['column_name']           # Access a column
df[['col1', 'col2']]        # Access multiple columns
df.iloc[0]                  # First row (by index)
df.loc[0]                   # First row (by label)
df.iloc[0:5, 1:3]           # Slicing rows and columns
```

---

### 5. **Filtering Rows**

```python
df[df['temperature'] > 30]       # Filter by condition
df[(df['humidity'] < 50) & (df['temperature'] > 30)]
df[df['device'] == 'sensor-1']
```

---

### 6. **Sorting Data**

```python
df.sort_values('temperature')               # Ascending
df.sort_values('humidity', ascending=False) # Descending
```

---

### 7. **Modifying / Adding Columns**

```python
df['temp_celsius'] = (df['temperature'] - 32) * 5/9
df['is_high'] = df['temperature'] > 30
df['time_bucket'] = pd.qcut(df['temperature'], 3)
```

---

### 8. **Handling Missing Data**

```python
df.isnull().sum()                 # Check missing
df.dropna()                       # Drop rows with missing
df.fillna(0)                      # Fill with value
df.fillna(method='ffill')         # Forward fill
```

---

### 9. **Group and Aggregate**

```python
df.groupby('device').mean()
df.groupby('device')['temperature'].max()
df.groupby('device').agg({'temperature': 'mean', 'humidity': 'min'})
```

---

### 10. **Apply and Lambda**

```python
df['status'] = df['temperature'].apply(lambda x: 'High' if x > 30 else 'Normal')
```

---

### 11. **Merging / Joining DataFrames**

```python
pd.merge(df1, df2, on='id')                      # Inner Join
pd.merge(df1, df2, how='left', on='id')          # Left Join
```

---

### 12. **Exporting Data**

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx")
df.to_json("output.json")
```

---

### 13. **Data Visualization with Pandas**

```python
df['temperature'].plot()
df.plot(x='temperature', y='humidity', kind='scatter')
df['device'].value_counts().plot(kind='bar')
```

> Tip: You can use `matplotlib` and `seaborn` for enhanced plotting.

---

### 14. **Time Series Support**

If your dataset has timestamps:

```python
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)
df.resample('1H').mean()      # Resample by hour
```

---

### ✅ Use Pandas For:

| Task                | Use This               |
| ------------------- | ---------------------- |
| Load + clean data   | `read_csv`, `dropna`   |
| Explore data        | `describe`, `info()`   |
| Filter conditions   | Boolean filtering      |
| Add new logic       | `apply`, `lambda`      |
| Plot trends         | `plot`, `value_counts` |
| Prepare data for ML | `groupby`, `merge`     |

---

### 🔧 Pandas Mini Project Ideas (based on this)

| Project Title                     | Dataset Feature Used     |
| --------------------------------- | ------------------------ |
| IoT Temperature Anomaly Detection | Filtering, lambda        |
| Device-wise Sensor Analysis       | `groupby`, `agg`         |
| Time Series Humidity Trend        | `datetime`, `resample`   |
| Top Devices with Max Temp         | `groupby`, `sort_values` |
| Exporting Cleaned Data            | `to_csv`, `fillna`       |

---

Would you like a **cheat sheet image** or a **printable PDF** of these Pandas notes?
Or should I now **embed these notes as markdown cells in your Jupyter notebook**?

Let me know how to proceed!
