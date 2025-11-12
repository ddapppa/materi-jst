# meet_07 - JST - INF - ALL.pptx

## Slide 1
- Jaringan Syaraf Tiruan ~ ~ Meet 07 ~ ~Program Studi InformatikaUniversitas Teknologi Yogyakarta
- Dr. Donny Avianto, S.T., M.T.

## Slide 2
- Deep Learning

## Slide 3
- Pertanyaan #1
- Apa sebenarnya deep learning itu?
- Deep learning berarti suatu neural network yang memiliki beberapa layer (layers of nodes) antara input dan output

## Slide 4
- Pertanyaan #2
- Jika deep learning adalah neural network yang terdiri dari banyak layer (multi layer) hal itu sudah ada sejak 25 tahun yang lalu. Apa yang baru dari deep learning sehingga bisa terkenal selama beberapa tahun terakhir ini?
- Kita sudah memiliki cara melatih yang baik untuk NN dengan 1 hidden layer
- Namun, cara ini tidak cukup baik untuk melatih NN dengan hidden layer yang banyak. Yang baru adalah Algoritma melatih NN -nya

## Slide 5
- Pertanyaan #3
- Mengapa fungsi aktivasi ReLu lebih sering digunakan dibandingkan Sigmoid di dalam penggunaan Deep Learning?
- Apa perbedaan fungsi aktivasi ReLu dan LeakyReLu?
- Sigmoid sangat berpotensi memicu masalah vanishing gradient selama proses pelatihan, sedangkan ReLu tidak

## Slide 6
_(tidak ada teks terdeteksi di slide ini)_

## Slide 7
_(tidak ada teks terdeteksi di slide ini)_

## Slide 8
_(tidak ada teks terdeteksi di slide ini)_

## Slide 9
_(tidak ada teks terdeteksi di slide ini)_

## Slide 10
_(tidak ada teks terdeteksi di slide ini)_

## Slide 11
- Pertanyaan #3
- Mengapa fungsi aktivasi ReLu lebih sering digunakan dibandingkan Sigmoid di dalam penggunaan Deep Learning?
- Apa perbedaan fungsi aktivasi ReLu dan LeakyReLu?
- LeakyReLu diciptakan untuk meminimalkan vanishing gradient pada saat input bernilai negative

## Slide 12
_(tidak ada teks terdeteksi di slide ini)_

## Slide 13
_(tidak ada teks terdeteksi di slide ini)_

## Slide 14
_(tidak ada teks terdeteksi di slide ini)_

## Slide 15
- Pertanyaan #4
- Apa yang dimaksud dengan Vanishing Gradient Problem? Bagaimana cara untuk meminimalkan efek Vanishing Gradient pada deep learning
- Memilih fungsi aktivasi yang meminimalkan Vanishing Gradient seperti ReLu atau LeakyReLu

## Slide 16
- Pertanyaan #4
- Apa yang dimaksud dengan Vanishing Gradient Problem? Bagaimana cara untuk meminimalkan efek Vanishing Gradient pada deep learning
- Tiru googleNet yang menghitung loss tidak hanya diakhir NN tetapi juga di tengah-tengah NN

## Slide 17
- Pertanyaan #4
- Apa yang dimaksud dengan Vanishing Gradient Problem? Bagaimana cara untuk meminimalkan efek Vanishing Gradient pada deep learning
- Skip Connection seperti pada Residual Network (ResNet)

## Slide 18
_(tidak ada teks terdeteksi di slide ini)_

## Slide 19
- ConvolutionalNeural Network(CNN)

## Slide 20
- CNN
- Salah satu jenis arsitektur deep learning yang sering digunakan untuk mengolah gambar / video
- Memiliki ciri khusus yaitu adanya lapisan konvolusi (Convolution Layer)

## Slide 21
- CNN
- Sebelumnya kita mengenal istilah fully connected layer  diterapkan pada hidden layer MLP

## Slide 22
- CNN
- Sebelumnya kita mengenal istilah fully connected layer  diterapkan pada hidden layer MLP

## Slide 23
- CNN
- Untuk mempersimple gambar,
- Hubungan input dengan node pada layer di depannya digambar seperti ini

## Slide 24
- CNN
- Convolution Layer

## Slide 25
- CNN
- Convolution Layer

## Slide 26
- CNN
- Convolution Layer

## Slide 27
- CNN
- Convolution Layer

## Slide 28
- CNN
- Convolution Layer

## Slide 29
- CNN
- Convolution Layer

## Slide 30
- CNN
- Convolution Layer

## Slide 31
- CNN
- Convolution Layer

## Slide 32
- CNN
- Convolution Layer
- Juga bisa memiliki 2 output yang berbeda

## Slide 33
- CNN
- Convolution Layer
- Juga bisa memiliki 2 output yang berbeda

## Slide 34
- Apa saja yang perlu di-setPada Convolution Layer
- Kernel Size
- Bertugas mengatur seberapa lokal kah convolution layer yang kita buat

## Slide 35
- CNN
- Bisa 1x1; 3x3; 5x5; atau lainnya

## Slide 36
- CNN
- Bagaimana jika ukuran kernel = input ??

## Slide 37
- Apa saja yang perlu di-setPada Convolution Layer
- Stride
- Mengatur seberapa jauh kernel akan digeser di setiap langkah konvolusinya
- Semakin banyak gesernya, makin banyak informasi dari input yang terlewatkan
- Dapat digunakan untuk mengurangi beban komputasi

## Slide 38
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 39
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 40
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 41
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 42
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 43
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 44
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 45
- Apa saja yang perlu di-setPada Convolution Layer

## Slide 46
- Apa saja yang perlu di-setPada Convolution Layer
- Input = … X …
- Kernel = … X …
- Stride = …

## Slide 47
- Apa saja yang perlu di-setPada Convolution Layer
- Padding
- Jika ingin ukuran feature hasil konvolusi tetap sama dengan ukuran inputnya

## Slide 48
- Apa saja yang perlu di-setPada Convolution Layer
- Ukuran dan nilai padding dapat
- Ditentukan sendiri

## Slide 49
- Pertanyaan #5
- Apa fungsi Pooling Layer yang ada pada arsitektur CNN?
- Apa perbedaan Max Pooling dengan Average Pooling pada CNN?
- Pooling layer berfungsi untuk mengecilkan ukuran / dimensi spasial
- Tujuannya agar beban komputasi dapat diminimalkan

## Slide 50
- Pooling Layer VS Conv Layer

## Slide 51
- Pooling Layer VS Conv Layer

## Slide 52
- JenisPooling Layer

## Slide 53
- JenisPooling Layer

## Slide 54
- Pertanyaan #5
- Apa fungsi Pooling Layer yang ada pada arsitektur CNN?
- Apa perbedaan Max Pooling dengan Average Pooling pada CNN?
- Max pooling menggunakan fungsi max untuk mencari nilai akhir hasil pooling sedangan average pooling menggunakan fungsi rata-rata untuk menentukan nilai akhir hasil pooling

## Slide 55
- RecurrentNeural Network(RNN)

## Slide 56
- Pertanyaan #6
- Apa perbedaan utama antara RNN dan CNN?
- CNN biasa digunakan pada data citra (input 2D)
- RNN  biasa digunakan pada data sekuensial (audio, video, sinyal, kalimat, dll) / data yang panjang nya berbeda-beda

## Slide 57
- Pertanyaan #6
- Apa perbedaan utama antara RNN dan CNN?
- CNN tidak memperhatikan keterurutan data input
- RNN memperhatikan keterurutan data input

## Slide 58
- Pertanyaan #7
- Jelaskan dari mana istilah “Recurrent” pada RNN muncul!
- Karena menggunakan weight yang berulang setiap kali menghitung hidden state

## Slide 59
_(tidak ada teks terdeteksi di slide ini)_

## Slide 60
_(tidak ada teks terdeteksi di slide ini)_

## Slide 61
_(tidak ada teks terdeteksi di slide ini)_

## Slide 62
_(tidak ada teks terdeteksi di slide ini)_

## Slide 63
_(tidak ada teks terdeteksi di slide ini)_

## Slide 64
_(tidak ada teks terdeteksi di slide ini)_

## Slide 65
_(tidak ada teks terdeteksi di slide ini)_

## Slide 66
_(tidak ada teks terdeteksi di slide ini)_

## Slide 67
_(tidak ada teks terdeteksi di slide ini)_

## Slide 68
_(tidak ada teks terdeteksi di slide ini)_

## Slide 69
_(tidak ada teks terdeteksi di slide ini)_

## Slide 70
_(tidak ada teks terdeteksi di slide ini)_

## Slide 71
- Pada RNN,
- Setiap output dipengaruhi oleh timestep sebelumnya

## Slide 72
- Sehingg RNN dianggap memiliki memori masa lalu yang didapatkan melalui hidden state sebelumnya

## Slide 73
- Pertanyaan #8
- Sebutkan 1 contoh kegunaan dari jenis RNN berikut:
- 1.       RNN dengan arsitektur One-to-Many
- 2.      RNN dengan arsitektur Many-to-One
- 3.      RNN dengan arsitektur Many-to-Many dimana
- Panjang Input = Panjang Output
- 4.     RNN dengan arsitektur Many-to-Many dimana
- Panjang Input ≠ Panjang Output

## Slide 74
_(tidak ada teks terdeteksi di slide ini)_

## Slide 75
_(tidak ada teks terdeteksi di slide ini)_

## Slide 76
_(tidak ada teks terdeteksi di slide ini)_

## Slide 77
_(tidak ada teks terdeteksi di slide ini)_

## Slide 78
_(tidak ada teks terdeteksi di slide ini)_

## Slide 79
_(tidak ada teks terdeteksi di slide ini)_

## Slide 80
- Mana yang merupakan kata biasa dan mana yang merupakan “nama”

## Slide 81
_(tidak ada teks terdeteksi di slide ini)_

## Slide 82
- Pertanyaan #9
- Jelaskan perbedaan antara RNN dan LSTM!
- …

## Slide 83
_(tidak ada teks terdeteksi di slide ini)_

## Slide 84
_(tidak ada teks terdeteksi di slide ini)_

## Slide 85
_(tidak ada teks terdeteksi di slide ini)_

## Slide 86
_(tidak ada teks terdeteksi di slide ini)_

## Slide 87
_(tidak ada teks terdeteksi di slide ini)_

## Slide 88
_(tidak ada teks terdeteksi di slide ini)_

## Slide 89
_(tidak ada teks terdeteksi di slide ini)_

## Slide 90
_(tidak ada teks terdeteksi di slide ini)_

## Slide 91
_(tidak ada teks terdeteksi di slide ini)_

## Slide 92
_(tidak ada teks terdeteksi di slide ini)_

## Slide 93
_(tidak ada teks terdeteksi di slide ini)_

## Slide 94
- Pertanyaan #9
- Jelaskan perbedaan antara RNN dan LSTM!
- RNN tidak memiliki Cell State
- LSTM memiliki Cell State

## Slide 95
_(tidak ada teks terdeteksi di slide ini)_

## Slide 96
_(tidak ada teks terdeteksi di slide ini)_

## Slide 97
_(tidak ada teks terdeteksi di slide ini)_

## Slide 98
_(tidak ada teks terdeteksi di slide ini)_

## Slide 99
_(tidak ada teks terdeteksi di slide ini)_

## Slide 100
_(tidak ada teks terdeteksi di slide ini)_

## Slide 101
_(tidak ada teks terdeteksi di slide ini)_

## Slide 102
_(tidak ada teks terdeteksi di slide ini)_

## Slide 103
_(tidak ada teks terdeteksi di slide ini)_

## Slide 104
- Pertanyaan #10
- Jelaskan perbedaan antara LSTM dan GRU!
- GRU memiliki jumlah parameter yang lebih sedikit dibandingkan LSTM
- Lebih cocok untuk data yang kecil

## Slide 105
_(tidak ada teks terdeteksi di slide ini)_

## Slide 106
_(tidak ada teks terdeteksi di slide ini)_

## Slide 107
_(tidak ada teks terdeteksi di slide ini)_

## Slide 108
_(tidak ada teks terdeteksi di slide ini)_

## Slide 109
_(tidak ada teks terdeteksi di slide ini)_

## Slide 110
_(tidak ada teks terdeteksi di slide ini)_

## Slide 111
_(tidak ada teks terdeteksi di slide ini)_

## Slide 112
_(tidak ada teks terdeteksi di slide ini)_

## Slide 113
_(tidak ada teks terdeteksi di slide ini)_

## Slide 114
_(tidak ada teks terdeteksi di slide ini)_

## Slide 115
_(tidak ada teks terdeteksi di slide ini)_

## Slide 116
_(tidak ada teks terdeteksi di slide ini)_

## Slide 117
_(tidak ada teks terdeteksi di slide ini)_

## Slide 118
_(tidak ada teks terdeteksi di slide ini)_

## Slide 119
_(tidak ada teks terdeteksi di slide ini)_

## Slide 120
- Terima Kasih
- Ada Pertanyaan…???

## Slide 121
- Jadwal UTS

## Slide 122
- Datang maksimal 15 menit sebelum
- Pakaian
- Penampilan
- Kecurangan

## Slide 123
- Pertemuan Setelah UTS
