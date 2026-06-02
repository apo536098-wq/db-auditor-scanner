import sqlite3

def audit_schema_constraints():
    print("\n[=] ADIM 1: VERİTABANI KISITLAMA DENETİMİ BAŞLADI [=]")
    conn = sqlite3.connect("cyber_university.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("PRAGMA table_info(Ogrenci);")
        columns = cursor.fetchall()
        for col in columns:
            print(f"[-] Sütun: {col[1]} | Tip: {col[2]} | Boş Kalabilir mi: {'HAYIR' if col[3] == 1 else 'EVET'}")
    except Exception as e:
        print(f"[!] Şema okuma hatası: {e}")
    
    # DÜZELTİLEN KISIM: 4 parametre yerine tablonun yapısı gibi 3 parametre gönderiyoruz (ID, Ad, Sinif)
    try:
        print("[!] Sınav Kuralı Test Ediliyor: Sınıfı '3' olan geçersiz veri ekleniyor...")
        cursor.execute("INSERT INTO Ogrenci VALUES (4, 'Hacker', 3);")
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"[✅ GÜVENLİ] Veritabanı CHECK kısıtlaması (CHECK (Sinif IN (1, 2))) ihlali yakaladı: {e}")
    except sqlite3.OperationalError as e:
        print(f"[❌ HATA] Tablo bulunamadı veya SQL hatası: {e}")
        
    conn.close()

def scan_sql_injection(user_input):
    conn = sqlite3.connect("cyber_university.db")
    cursor = conn.cursor()
    vulnerable_query = f"SELECT * FROM Ogrenci WHERE Ad = '{user_input}'"
    try:
        cursor.execute(vulnerable_query)
        return cursor.fetchall()
    except sqlite3.OperationalError as e:
        return f"[!] SQL Hatası: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    audit_schema_constraints()
    
    print("\n[=] ADIM 2: SQL INJECTION TACTICAL SCAN [=]")
    payload = "Kadir' OR '1'='1"
    print(f"[*] Test Edilen Girdi: {payload}")
    print(f"[!] Tarayıcı Çıktısı:\n{scan_sql_injection(payload)}")
