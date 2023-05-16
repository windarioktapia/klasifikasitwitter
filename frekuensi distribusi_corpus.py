import nltk
from nltk import FreqDist, word_tokenize



# tokenisasi korpus
corpus = "Ini adalah contoh korpus. Korpus ini berisi beberapa kalimat."

f0 = open("filesumber.txt", "r") #corpustrain.txt
tekskalimat=" "
for baris in f0 :
    kal = baris.strip()
    tekskalimat=tekskalimat+" "+kal
    #print(tekskalimat)
tokenskalimat = word_tokenize(tekskalimat)
# hitung frekuensi kemunculan kata pada korpus
fdist = FreqDist(tokenskalimat)
print(fdist)
jumlahkatalatih=0
jumlahfreq_dict=0
print("distribusi frekuensi kata latih")
for x in fdist:
    print(f"{jumlahkatalatih+1}.  {x} = {fdist[x]}")
    jumlahkatalatih=jumlahkatalatih+1
    jumlahfreq_dict = jumlahfreq_dict+fdist[x]
print(f"jumlah kata latih(telah digabung/unik) ={jumlahkatalatih}, total frekdict/jumlah total kata latih ={jumlahfreq_dict}")

print("kata frek tertinggi ", fdist.max()," = ", fdist[fdist.max()])
# ambil 10 kata yang paling sering muncul
top_words = fdist.most_common()  # top_words = fdist.most_common(50)  #isi 50

# tampilkan hasil
print("Frekuensi distribusi kata pada korpus:")
print(fdist.tabulate(10)) # print(fdist.tabulate(50)) # isi 50

# gambarkan grafik frekuensi distribusi
fdist.plot(70,cumulative=False) #fdist.plot(50, cumulative=False)