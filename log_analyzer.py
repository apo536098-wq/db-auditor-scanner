import sqlite3
import re

def init_log_db():
    """Saldırı analiz günlükleri için ek güvenlik tablosu oluşturur."""
    conn = sqlite3.connect("cyber_university.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SecurityLogs (
        LogID INTEGER PRIMARY KEY AUTOINCREMENT,
        IPAddress VARCHAR(15),
        RequestType VARCHAR(10),
        Payload TEXT,
        Severity VARCHAR(10)
    );
    """)
    conn.commit()
    conn.close()

def analyze_mock_traffic():
    """
    Siber güvenlik simülasyonu: Gelen ağ trafiği loglarını tarar, 
    SQLi ve tehlikeli kısıtlama ihlali isteklerini tespit edip veritabanına kaydeder.
    """
    init_log_db()
    print("\n[=] ADIM 4: SİBER GÜVENLİK TRAFİK LOG ANALİZİ BAŞLADI [=]")
    
    # Simüle edilmiş sunucu log trafiği (Gerçek hayattaki SOC logları gibi)
    mock_logs = [
        {"ip": "192.168.1.50", "type": "GET", "payload": "Kadir"},
        {"ip": "185.220.101.5", "type": "POST", "payload": "1' OR '1'='1"}, # SQLi Saldırısı
        {"ip": "192.168.1.65", "type": "POST", "payload": "INSERT INTO Ogrenci VALUES (5, 'Hacker', 3)"}, # Kısıtlama İhlali Saldırısı
        {"ip": "45.155.205.33", "type": "GET", "payload": "UNION SELECT null, username, password FROM users--"} # Gelişmiş SQLi
    ]
    
    conn = sqlite3.connect("cyber_university.db")
    cursor = conn.cursor()
    
    # SQL Injection tespiti için Regex (Düzenli İfade) siber güvenlik kuralı
    sqli_pattern = re.compile(r"('|--|UNION|OR\s+['\"]?\d+['\"]?\s*=\s*['\"]?\d+)", re.IGNORECASE)
    
    for log in mock_logs:
        payload = log["payload"]
        severity = "LOW"
        
        # 1. Aşama: SQL Injection Tehdit Algılama
        if sqli_pattern.search(payload):
            severity = "HIGH"
            print(f"[🚨 CRITICAL] SQL Injection Saldırısı Engellendi! IP: {log['ip']} | Payload: {payload}")
            
        # 2. Aşama: Şema/Kısıtlama İhlali Tehdit Algılama (Sınav Konumuz: Sınıf 3 olamazdı)
        elif ", 3)" in payload or "Sinif" in payload:
            severity = "MEDIUM"
            print(f"[⚠️ WARNING] Veritabanı Şema İhlali Girişimi Durduruldu! IP: {log['ip']}")
            
        else:
            print(f"[✅ INFO] Güvenli Trafik Geçişine İzin Verildi. IP: {log['ip']}")
            
        # Tespit edilen logu veritabanındaki SecurityLogs tablosuna yazıyoruz
        cursor.execute("""
        INSERT INTO SecurityLogs (IPAddress, RequestType, Payload, Severity) 
        VALUES (?, ?, ?, ?);
        """, (log["ip"], log["type"], payload, severity))
        
    conn.commit()
    conn.close()
    print("[+] Saldırı Analiz Logları 'cyber_university.db' İçine Başarıyla İşlendi.")

if __name__ == "__main__":
    analyze_mock_traffic()
