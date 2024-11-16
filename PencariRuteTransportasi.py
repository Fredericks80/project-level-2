import networkx as nx
from geopy.distance import great_circle

class Transportasi:
    def __init__(self):
        self.graph = nx.Graph()
        self.tambahkan_rute()
        
    def tambahkan_rute(self):
        # Menambahkan rute sebagai (titik_awal, titik_tujuan, jarak)
        rute = [
            ("LRT", "Stasiun Kertapati", 5),
            ("Stasiun Kertapati", "Terminal BUS", 3),
            ("Terminal BUS", "Palembang", 10),
            ("Palembang", "Kayu Agung", 20),
            ("Stasiun Kertapati", "Lubuklinggau", 15)
        ]
        
        for awal, tujuan, jarak in rute:
            self.graph.add_edge(awal, tujuan, weight=jarak)
    
    def cari_rute(self, start, end):
        try:
            rute_terpendek = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            jarak = nx.shortest_path_length(self.graph, source=start, target=end, weight='weight')
            return rute_terpendek, jarak
        except nx.NetworkXNoPath:
            return "Tidak ada rute yang tersedia."
        except nx.NodeNotFound:
            return "Salah satu lokasi tidak ditemukan."

def main():
    transportasi = Transportasi()
    start = input("Masukkan titik awal: ")
    end = input("Masukkan titik tujuan: ")
    
    hasil = transportasi.cari_rute(start, end)
    if isinstance(hasil, tuple):
        rute, jarak = hasil
        print(f"Rute terpendek dari {start} ke {end} adalah: {' -> '.join(rute)} dengan jarak {jarak} unit.")
    else:
        print(hasil)

if __name__ == "__main__":
    main()
