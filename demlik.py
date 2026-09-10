#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varolussal Cay Demligi - calisan, kustah, resmiyetle absurt."""

import random
import time
import base64

# gizli not: decode edilirse bir fincan soguk metafor cikar.
_GIZLI = base64.b64decode(
    b"aGVyIGd1YyBiaXIgZmluY2FuIGdpYmkgc29ndXIsIGhlciBrYXJhciBiaXIgZGVtIGdpYmkgZ2VjaWNpIG9sdXI="
).decode("utf-8")

SORULAR = [
    "Cay var midir, yoksa sadece sicak suyun kendini kandirmasi midir?",
    "Demlenmeden onceki cay, cay midir?",
    "Bardak yarim doluysa su mu kazandi, cay mi kaybetti?",
    "Eger kimse icmezse demligin varolusu gecersiz midir?",
    "Seker koymak ozgur irade midir yoksa gelenek midir?",
]

ANAHTAR = ["anladim", "var", "yok", "belki", "evet", "hayir", "bilmiyorum"]


def damga():
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH\n"
        "Kayyum Grok - Tentivory - 10 Eylul 2026\n"
        "Bu belge ciddiyetle yazilmistir; icerigi ciddi degildir.\n"
        "Resmiyet: yuksek. Anlam: tartismali.\n"
        "---\n"
    )


def demle():
    print("=== VAROLUSSAL CAY DEMLIGI v1.0 ===")
    print("Su kayniyor... hayir, su 'olma' halini tartisiyor.\n")
    time.sleep(0.4)
    print("DEMLIK:", random.choice(SORULAR))
    try:
        cevap = input("Siz: ").strip().lower()
    except EOFError:
        cevap = ""
    if not cevap:
        print("DEMLIK: Sessizlik de bircevaptir. Su sogudu. Cay yok.")
        print(damga())
        return 1
    if any(k in cevap for k in ANAHTAR) or len(cevap) > 8:
        print("DEMLIK: Kabul. Demleniyor...")
        for i in range(3):
            print("  " + "." * (i + 1) + " koku teorik olarak olusuyor")
            time.sleep(0.3)
        print("DEMLIK: Cay hazir. Icerseniz var olur; icmezseniz sadece sicak sudur.")
        print(damga())
        return 0
    print("DEMLIK: Bu cevap demligi ikna etmedi. Su kendi istegiyle sogudu.")
    print(damga())
    return 2


if __name__ == "__main__":
    raise SystemExit(demle())
# _GIZLI calistirilmaz; sadece durur. guc gibi.
