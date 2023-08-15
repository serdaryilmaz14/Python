# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect("kullaniciVeritabani.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS kullanicilar (
        id INTEGER PRIMARY KEY,
        kullaniciAdi TEXT,
        sifre TEXT
    )
""")

kullanicilar = [
    ("ahmet", "ahmet6a"),
    ("mehmet", "mehmet23531"),
    ("ayse", "ayse785"),
    ("ali","12ali21"),
    ("burcu","burcu55w"),
    
]

cursor.executemany("INSERT INTO kullanicilar (kullaniciAdi, sifre) VALUES (?, ?)", kullanicilar)

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()