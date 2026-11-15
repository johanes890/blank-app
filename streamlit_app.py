
import datetime
import os

# Database produk sederhana (Kode: [Nama Barang, Harga])
PRODUK_DB: dict[str, tuple[str, int]] = {
    "001": ("Beras Ramos 5kg", 72000),
    "002": ("Minyak Goreng 2L", 35000),
    "003": ("Gula Pasir 1kg", 17500),
    "004": ("Indomie Goreng", 3200),
    "005": ("Susu UHT Full Cream 1L", 19000),
    "006": ("Kopi Kapal Api 165g", 15500),
    "007": ("Telur Ayam 1kg", 28000),
    "008": ("Sabun Mandi Cair 450ml", 24000),
}

def bersihkan_layar() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def format_rupiah(nominal: int | float) -> str:
    return f"Rp{nominal:,.0f}".replace(",", ".")

def tampilkan_katalog() -> None:
    print("\n" + "=" * 45)
    print(f"{'KODE':<6} | {'NAMA BARANG':<24} | {'HARGA':>10}")
    print("-" * 45)
    for kode, (nama, harga) in PRODUK_DB.items():
        print(f"{kode:<6} | {nama:<24} | {format_rupiah(harga):>10}")
    print("=" * 45)

def cetak_struk(keranjang: list[dict], total_belanja: int, diskon: int, bayar: int, kembalian: int) -> None:
    waktu_sekarang = datetime.datetime.now()
    no_transaksi = waktu_sekarang.strftime("TRX-%Y%m%d-%H%M%S")
    tanggal_str = waktu_sekarang.strftime("%d/%m/%Y %H:%M:%S")
    
    garis = "=" * 42
    sub_garis = "-" * 42
    
    isi_struk = [
        garis,
        "          MINIMARKET BERKAH JAYA          ",
        "      Jl. Merdeka No. 45, Indonesia       ",
        garis,
        f"No. TRX : {no_transaksi}",
        f"Tanggal : {tanggal_str}",
        sub_garis,
    ]
    
    for item in keranjang:
        nama = item['nama'][:22]
        qty = item['qty']
        harga = format_rupiah(item['harga'])
        subtotal = format_rupiah(item['subtotal'])
        isi_struk.append(f"{nama}")
        isi_struk.append(f"  {qty} x {harga:<12} = {subtotal:>14}")
        
    isi_struk.extend([
        sub_garis,
        f"{'Total Belanja':<22} : {format_rupiah(total_belanja):>17}",
        f"{'Diskon':<22} : {format_rupiah(diskon):>17}",
        f"{'Total Bayar':<22} : {format_rupiah(total_belanja - diskon):>17}",
        f"{'Tunai':<22} : {format_rupiah(bayar):>17}",
        f"{'Kembalian':<22} : {format_rupiah(kembalian):>17}",
        garis,
        "   TERIMA KASIH ATAS KUNJUNGAN ANDA!      ",
        "   Barang yang sudah dibeli tidak dapat   ",
        "        ditukar atau dikembalikan         ",
        garis
    ])
    
    struk_final = "\n".join(isi_struk)
    
    # Tampilkan di terminal
    print("\n" + struk_final)
    
    # Simpan ke file txt
    nama_file = f"{no_transaksi}.txt"
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(struk_final)
    print(f"\n[Info] Struk berhasil disimpan ke file: {nama_file}")

def jalankan_kasir() -> None:
    while True:
        bersihkan_layar()
        print("=== SISTEM KASIR MINIMARKET (PYTHON 3.13) ===")
        keranjang: list[dict] = []
        
        while True:
            tampilkan_katalog()
            kode = input("\nMasukkan KODE barang (ketik 'bayar' untuk checkout, 'keluar' untuk tutup): ").strip().lower()
            
            if kode == 'keluar':
                print("Menutup aplikasi kasir...")
                return
            elif kode == 'bayar':
                if not keranjang:
                    print("[!] Keranjang masih kosong. Silakan pilih barang terlebih dahulu.")
                    continue
                break
            elif kode not in PRODUK_DB:
                print(f"[!] Kode '{kode}' tidak ditemukan!")
                input("Tekan Enter untuk melanjutkan...")
                bersihkan_layar()
                continue
                
            try:
                qty = int(input(f"Jumlah beli ({PRODUK_DB[kode][0]}): "))
                if qty <= 0:
                    raise ValueError
            except ValueError:
                print("[!] Jumlah harus berupa angka bulat lebih dari 0.")
                input("Tekan Enter untuk melanjutkan...")
                bersihkan_layar()
                continue
                
            nama_barang, harga_satuan = PRODUK_DB[kode]
            
            # Cek apakah barang sudah ada di keranjang
            barang_ada = False
            for item in keranjang:
                if item['kode'] == kode:
                    item['qty'] += qty
                    item['subtotal'] = item['qty'] * harga_satuan
                    barang_ada = True
...                     break
...                     
...             if not barang_ada:
...                 keranjang.append({
...                     'kode': kode,
...                     'nama': nama_barang,
...                     'harga': harga_satuan,
...                     'qty': qty,
...                     'subtotal': qty * harga_satuan
...                 })
...                 
...             bersihkan_layar()
...             print("--- KERANJANG SAAT INI ---")
...             for idx, item in enumerate(keranjang, 1):
...                 print(f"{idx}. {item['nama']} ({item['qty']}x) - {format_rupiah(item['subtotal'])}")
... 
...         # Proses Checkout
...         total_belanja = sum(item['subtotal'] for item in keranjang)
...         
...         # Promo otomatis: Diskon 5% jika belanja di atas Rp150.000
...         diskon = int(total_belanja * 0.05) if total_belanja >= 150000 else 0
...         total_akhir = total_belanja - diskon
...         
        print("\n" + "=" * 35)
        print(f"Total Belanja : {format_rupiah(total_belanja)}")
        if diskon > 0:
            print(f"Diskon (5%)   : -{format_rupiah(diskon)}")
        print(f"Total Tagihan : {format_rupiah(total_akhir)}")
        print("=" * 35)
        
        while True:
            try:
                bayar = int(input("Masukkan Uang Tunai Pelanggan: Rp"))
                if bayar < total_akhir:
                    print(f"[!] Uang kurang {format_rupiah(total_akhir - bayar)}!")
                else:
                    break
            except ValueError:
                print("[!] Masukkan nominal angka yang valid.")
                
        kembalian = bayar - total_akhir
        bersihkan_layar()
        cetak_struk(keranjang, total_belanja, diskon, bayar, kembalian)
        
        lagi = input("\nTransaksi baru? (y/n): ").strip().lower()
        if lagi != 'y':
            print("Terima kasih telah menggunakan sistem kasir!")
            break

if __name__ == "__main__":
