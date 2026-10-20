# ==========================================
# STUDI KASUS 5: Dasbor Analisis Kinerja & Interaksi Pengguna (HCI & Data Visualization)
# Berdasarkan Materi Praktisi oleh Dr. Arafat Febrian Dirza (BRIN)
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- Memulai Pemrosesan Data & Visualisasi Dasbor Interaktif ---")

# 1. Simulasi Data Metrik Penggunaan Aplikasi (User Engagement & Usability Metrics)
np.random.seed(42)
n_users = 200

user_data = pd.DataFrame({
    'user_id': [f"USR-{i:03d}" for i in range(1, n_users + 1)],
    'age_group': np.random.choice(['Remaja', 'Dewasa', 'Lansia'], size=n_users, p=[0.3, 0.5, 0.2]),
    'task_completion_time_sec': np.random.normal(45.0, 10.0, size=n_users), # Waktu penyelesaian tugas
    'error_count': np.random.poisson(lam=1.5, size=n_users),                # Jumlah kesalahan input pengguna
    'satisfaction_score': np.random.randint(1, 6, size=n_users)             # Skor kepuasan (1-5)
})

# Pastikan tidak ada nilai waktu negatif
user_data['task_completion_time_sec'] = np.maximum(user_data['task_completion_time_sec'], 5.0)

print("\n--- 5 Data Teratas Metrik Pengguna ---")
print(user_data.head())

# 2. Analisis Statistik Berdasarkan Kelompok Usia (Prinsip User Persona & Evaluasi UX)
print("\n--- Rata-Rata Performa Berdasarkan Kelompok Usia ---")
summary_group = user_data.groupby('age_group').agg({
    'task_completion_time_sec': 'mean',
    'error_count': 'mean',
    'satisfaction_score': 'mean'
}).reset_index()

summary_group.columns = ['Kelompok Usia', 'Rata-Rata Waktu (detik)', 'Rata-Rata Error', 'Skor Kepuasan Rata-Rata']
print(summary_group)

# 3. Visualisasi Data Sederhana & Efisien (Prinsip Data-Ink Ratio yang Bersih dari Chartjunk)
plt.figure(figsize=(10, 5))

# Grafik 1: Waktu Penyelesaian Tugas Berdasarkan Kelompok Usia
plt.subplot(1, 2, 1)
plt.bar(summary_group['Kelompok Usia'], summary_group['Rata-Rata Waktu (detik)'], color=['#4C72B0', '#55A868', '#C44E52'])
plt.title('Rata-Rata Waktu Penyelesaian Tugas')
plt.xlabel('Kelompok Usia Pengguna')
plt.ylabel('Waktu (detik)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafik 2: Hubungan Waktu vs Jumlah Error (Scatter Plot)
plt.subplot(1, 2, 2)
plt.scatter(user_data['task_completion_time_sec'], user_data['error_count'], alpha=0.6, color='purple')
plt.title('Korelasi Waktu vs Jumlah Error')
plt.xlabel('Waktu Tugas (detik)')
plt.ylabel('Jumlah Error')
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

# Simpan grafik visualisasi
output_chart_path = 'hci_visualization_report.png'
plt.savefig(output_chart_path, dpi=300)
print(f"\n[SUKSES] Grafik visualisasi berhasil disimpan ke '{output_chart_path}'.")

# 4. Ekspor Data Laporan Analisis
user_data.to_csv('hci_usability_metrics.csv', index=False)
print("[SUKSES] Data metrik usabilitas diekspor ke 'hci_usability_metrics.csv'.")