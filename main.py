import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi trapezoid
def trapezoid_integral(f, a, b, N):
    # Menghitung lebar setiap trapezoid
    h = (b - a) / N
    
    # Membuat array nilai x dari a sampai b dengan N+1 titik
    x = np.linspace(a, b, N+1)
    
    # Menghitung nilai fungsi pada setiap titik x
    y = f(x)
    
    # Menghitung integral menggunakan aturan trapezoid
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:N]) + y[N])
    return integral

# Menghitung galat RMS (Root Mean Square) antara nilai pi yang diestimasi dan nilai pi referensi
def rms_error(estimated_pi, reference_pi):
    return np.sqrt(np.mean((estimated_pi - reference_pi)**2))

# Referensi nilai pi yang sebenarnya
pi_ref = 3.14159265358979323846

# Daftar nilai N yang akan diuji
N_values = [10, 100, 1000, 10000]

# Melakukan pengujian untuk setiap nilai N
for N in N_values:
    # Mencatat waktu mulai eksekusi
    start_time = time.time()
    
    # Mengestimasi nilai pi menggunakan metode trapezoid
    estimated_pi = trapezoid_integral(f, 0, 1, N)
    
    # Menghitung waktu eksekusi
    execution_time = time.time() - start_time
    
    # Menghitung galat RMS antara nilai pi yang diestimasi dan nilai pi referensi
    error = rms_error(estimated_pi, pi_ref)
    
    # Menampilkan hasil pengujian
    print("Didapatkan:")
    print(f"N = {N}")
    print(f"Hasil Pi: {estimated_pi}")
    print(f"Galat RMS: {error}")
    print(f"Waktu Eksekusi: {execution_time} seconds")
    print("-" * 60)
