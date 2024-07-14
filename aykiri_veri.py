import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Veri setini oluştur
data = {
    'Bellek Hızı': ['1066 MHz', '1066 MHz', '1066 MHz', '3200 MHz', '3200 MHz', '2933 MHz', '2933 MHz','1066 MHz'],
    'Cihaz Ağırlığı': [None, None, None, '1 - 2 kg', '1 - 2 kg', '2 - 4 kg', '2 - 4 kg','1 - 2 kg'],
    'Ekran Boyutu': [10, 10, 10, 15.6,15.6, 15.6, 15.6,189.6],
    'Ekran Kartı Bellek Tipi': [None, None, None, 'GDDR4', 'GDDR5', 'GDDR6', 'GDDR6','GDDR6'],
    'Ekran Kartı Hafızası': ['1 GB', '1 GB', '1 GB', '2 GB', '2 GB', '4 GB', '4 GB','4 GB'],
    'Ekran Kartı Tipi': ['Harici Ekran Kartı', 'Harici Ekran Kartı', 'Harici Ekran Kartı', 'Harici Ekran Kartı', 'Harici Ekran Kartı', 'Yüksek Seviye Harici Ekran Kartı', 'Yüksek Seviye Harici Ekran Kartı', 'Harici Ekran Kartı'],
    'Ekran Panel Tipi': ['LED', 'LED', 'LED', 'LED', 'LED', 'IPS', 'IPS', 'IPS'],
    'İşlemci Nesli': ['1.Nesil', '1.Nesil', '1.Nesil', '10. Nesil', '10. Nesil', '10. Nesil', '10. Nesil', '10. Nesil'],
    'İşlemci': ['1000M', '1000M', '1000M', '1035G1', '1035G1', '10300H', '10300H', '10300H'],
    'İşletim Sistemi': ['Android', 'Android', 'Android', 'Windows 10 Home', 'Windows 10 Home', 'Yok (Free Dos)', 'Yok (Free Dos)', 'Yok (Free Dos)'],
    'Kart Okuyucu': [None, None, None, 'Var', 'Yok', 'Yok', None, 'Var'],
    'Aydınlatma': [0,0,0,0,0,0,1,1],
    'Maksimum İşlemci Hızı': ['1,05 GHz', '1,05 GHz', '1,05 GHz', '3,6 GHz', '3,6 GHz', '4,5 GHz', '4,5 GHz', '4,5 GHz'],
    'Max Ekran Çözünürlüğü': [None, None, None, '1920 x 1080', '1920 x 1080', '1920 x 1080', '1920 x 1080', '1920 x 1080'],
    'Parmak İzi Okuyucu': [None, None, None, 'Yok', 'Yok', 'Yok', 0, 'Yok',],
    'Ram (Sistem Belleği)': [None, None, None, '8 GB', '12 GB', '16 GB', '8 GB', '16 GB'],
    'SSD Kapasitesi': ['1 TB', '1 TB', '1 TB', '512 GB', '1 TB', '512 GB', '512 GB', '512 GB'],
    'Ürün Modeli': ['Notebook', 'Notebook', 'Notebook', 'Notebook', 'Notebook', 'Oyun Bilgisayarları', 'Oyun Bilgisayarları', 'Notebook'],
    'Fiyat': ['Çok Yüksek', 'Çok Yüksek', 'Orta', 'Düşük', 'Düşük', 'Düşük', 'Düşük', 'Orta']
}
df = pd.DataFrame(data)
#excel_file_path = 'C:\\Users\\mlkce\\OneDrive\\Masaüstü\\veri_bilimi_final_projesi\\data.xlsx'  # Veri setinin bulunduğu dosya yolu
#df = pd.read_excel(excel_file_path)
numeric_columns = df.select_dtypes(include='number').columns
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')
for column in numeric_columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot - {column}')
    plt.show()
Q1 = df[numeric_columns].quantile(0.25)
Q3 = df[numeric_columns].quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = (df[numeric_columns] < (Q1 - 1.5 * IQR)) | (df[numeric_columns] > (Q3 + 1.5 * IQR))
outliers_count = outliers_iqr.sum().sum()
print("Toplam Aykırı Değer Sayısı:", outliers_count)
outliers_data = df[outliers_iqr.any(axis=1)]
print("Aykırı Değerler (IQR):")
print(df[outliers_iqr.any(axis=1)])
df_cleaned_mean = df.copy()
for column in numeric_columns:
    mean_value = df_cleaned_mean[column].mean()
    df_cleaned_mean.loc[outliers_iqr[column], column] = mean_value
'''
# Aykırı değerleri medyan ile doldurma yöntemi
df_cleaned_median = df.copy()
for column in numeric_columns:
    median_value = df_cleaned_median[column].median()
    #df_cleaned_median[column] = df_cleaned_median[column].replace(df_cleaned_median[outliers_iqr[column]], median_value)
    df_cleaned_median.loc[outliers_iqr[column],column]=median_value
'''

print("\nAykırı Değerleri Ortalama ile Doldurma Sonucu:")
print(df_cleaned_mean)