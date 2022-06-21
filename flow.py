# Tubes Pemodelan dan Simulasi
# Moh. Adi ikfini (1301194160)
# Retno Diah Ayu N (1301194460)
# Windy Ramadhanti (1301194002)


import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
from matplotlib import animation
import operator as op

def car_model(car):
    # Inisiasi variabel untuk pemodelan
    M = 100
    p = float(0.3)
    v = 0
    N = 20
    tmax = 1000
    vmax = 5
    D = 2
    car_in_circle = []
    c_antri = [i for i in range(N)]
    time = 0
    c_dens = {}
    c_Max = [0 for i in range(tmax)]
    avg0 = 0
    # Proses iterasi pemodelan
    for x in range(tmax):
        x_row = []
        iterasi_car = 0
     
        for i in c_antri:
            s_car = car[i]
            next_c = car[i+1 if i+1 < N else 0]

            #Mengupdate Kecepatan
            v = np.min([v+1, vmax])
            
            # Mengambil Jarak Antar Mobil
            if (i == 0):
                d = D
            elif (next_c[0] < s_car[0]):
                d = M - next_c[0]
            else: 
                d = (next_c[0]-s_car[0])

            # Peluang Kecenderungan pengemudi mengerem
            rem = random.rand()
            if(rem < p):
                v = np.max([np.min([v+1, vmax, d-1]) - 1, 0])
            else :
                v = np.min([v+1, vmax, d-1])

            
            # Update Posisi
            x = s_car[0] # Mengambil nilai x dari mobil ke - i
            x = x + v

            # Pengecekan jika nilai x lebih dari M, maka kembali ke awal
            if (x >= M):
                temp = []
                for i in range(N):
                    order = c_antri[i] + N-1
                    if (order + N-1 > N):
                        order = order - N
                    temp.append(order)
                c_antri = temp
                x = x - M
                car[i][2] += 1
            x_row.append([x,s_car[1],car[i][2]])

            # Update Posisi
            if x >= 80 and x <= 90:
                iterasi_car += 1

        # Menghitung kepadatan lalulintas
        c_dens[time] = ((iterasi_car/10)*100)
        time += 1

        # Menyimpan dan menampung posisi terbaru dari mobil
        car = x_row
        car_in_circle.append(x_row)

    # Iterasi untuk Mencari nilai kepadatan pada tiap internal waktu, dengan ketentuan 5 unit posisi
    for i in range(len(car_in_circle)):
        for j in range(len(car_in_circle[0])):
            if(j < N-1):
                select = car_in_circle[i][j][0]
                next = car_in_circle[i][j+1][0]
                if(next - select <= 5 and next - select >= 0):
                    c_Max[i] += 1

    

    # Menghitung nilai Rata-Rata mobil kembali ke posisi awal
    sum = 0
    for i in range(len(car)):
        sum += car[i][2]
        
    avg0 = sum/N/tmax*100

    return car_in_circle, c_dens, avg0, c_Max

#Fungsi render
def animate(i):
    cars_p = car_Move[i]
    car_marker.set_offsets(cars_p)
    return car_marker

#main program
if __name__ == "__main__":
    #inisialisasi variabel pemodelan
    M = 100
    p = float(0.3)
    v = 0
    N = 20
    tmax = 1000
    vmax = 5
    d = 2

    #Set Visualisasi Jalan
    road_fig = np.array( [ [[0,M+0.5], [3,3]], [[0,M+0.5], [7,7]] ] )
    #Random Posisi Mobil
    car = np.array([[random.randint(1,M), 5, 0] for i in range(1,N+1)])
    #Sorting Posisi mobil
    car = np.array(sorted(car, key=op.itemgetter(0)))

    car_Move, c_dens, avg, c_Max = car_model(car)

    # Menampilkan kepadatan di posisi 80-90
    print(' Kepadatan Kendaraan di posisi X80 ~ X90:')
    for x in c_dens:
        print(f'Kepadatan Kendaraan di waktu ke-{x+1} adalah sebesar {c_dens[x]}')

    # Menampilkan Figure kepadatan di posisi 80-90
    plt.figure(1, figsize= (14,6))
    plt.bar(range(len(c_dens)), list(c_dens.values()), width=0.6)
    plt.title("Kepadatan Kedaraan di posisi X80 ~ X90")
    plt.xlabel("Satuan Waktu")
    plt.ylabel("Banyak Kendaraan")

     # Menampilkan kepadatan Maksimum tiap internal dengan ketentuan 5 unit posisi
    print("kepadatan Maksimum ketentuan 5 Unit Posisi")
    for x in c_Max:
        print(f'Kepadatan Kendaraan Maks di waktu ke-{x+1} adalah sebesar {c_Max[x]}')

    # Menampilkan Figure kepadatan di posisi 80-90
    plt.figure(2, figsize= (14,6))
    plt.bar(range(len(c_Max)), c_Max, width=0.6)
    plt.title("kepadatan Maksimum ketentuan 5 Unit Posisi")
    plt.xlabel("Satuan Waktu")
    plt.ylabel("Banyak Kendaraan")

    # Menampilkan Nilai Rata rata Mobil kembali ke posisi awal
    print('Waktu Rata Rata Kendaraan:')
    print('Waktu rata-rata mobil kembali ke posisi awal adalah', format(avg, '.3f'))

    # Figure Titik Semua Mobil
    a = np.zeros(shape=(tmax,M))
    for i in range(tmax):
      index = 0
      for j in range(M):
        temp = np.array(sorted(car_Move[i], key=op.itemgetter(0)))
        if(j == temp[index][0] and index < N-1):
          index +=1
          a[i,j] = 0
        else :
          a[i,j] = -1

    plt.figure(3, figsize= (15,25))
    plt.xlabel("Satuan Poisis")
    plt.ylabel("Satuan Waktu")
    plt.imshow(a, cmap="Greys", interpolation="nearest")

    # Menampilkan Simulasi 
    fig = plt.figure(4)
    plot_axes = plt.axes(ylim=(0,10), xlim=(0,M+0.5))
    plt.plot([90,90],[3,7],color='blue')
    plt.plot([80,80],[3,7],color='blue')
    plt.title("Simulasi Traffic Flow")
    for road in road_fig:
        plt.plot(road[0], road[1], color="black")
    car_marker = plot_axes.scatter([], [], s=75, marker="s")

    anim = animation.FuncAnimation(fig, animate, frames=len(car_Move), interval=300, repeat=False)
    plt.show()




