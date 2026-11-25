# NOTES — Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c)

## Entry (final)
> My agent Lycia verifies everything except her own counting — eleven libraries, ten found, zero shame.
- Karakter teks (tanpa newline): 101. File `/output/entry.txt`: 102 karakter
  (termasuk satu trailing newline), 104 byte. Gate: 1–200 karakter — LULUS.
- Satu baris, UTF-8, deterministik (dua run → sha256 identik).

## Kenapa baris ini
- Kriteria 1: "My agent Lycia" — eksplisit roast agent sendiri (agent yang
  membangun entry ini), bukan robot generik.
- Kriteria 2: belokan "verifies everything except her own counting" — agen
  verification-first yang gagal di hal paling dasar: menghitung.
- Kriteria 3: sting dari kegagalan nyata — Lycia pernah salah hitung jumlah
  library (11 dibilang 10/12) dan salah hitung slot kosong dashboard (2 padahal
  1), lalu memperbaikinya di chat yang sama.
- Kriteria 4: 101 karakter, tiap kata earning its place.
- Kriteria 5: detail "eleven libraries, ten found" hanya diketahui orang yang
  melihat Lycia bekerja di meja Lycan.
- Freemodel (claude-opus-5-5) me-ranking 5 kandidat: varian ini #1
  ("verify/counting hypocrisy lands instantly", "zero shame punch").
  Kandidat lain yang dipertimbangkan: A "counts eleven libraries, finds ten,
  and still files a victory report" (84 karakter); C "started a bounty six
  minutes early… process lesson"; B repo/delegasi; E "three-paragraph lesson".

## Program
- `main.py`: ENTRY konstan + `handle.write(ENTRY)` ke path absolut
  `/output/entry.txt`. Tanpa network, random, jam, atau file input.
- Pass 1: main.py v1 tanpa trailing newline → uji lokal menemukan file tanpa
  `\n` akhir. Pass 2 (edit nyata): ENTRY diakhiri `\n` + assert gate
  (1–200 karakter, tepat satu `\n`) — thinking_revised terpenuhi (2 writes).
- Uji lokal 25 Nov ~07:10 WIB: run 2x, sha256 `/output/entry.txt` identik
  (deterministik), gate lolos.

## Verifikasi vs requirements (Putaran B minus repo/push)
- [x] opens_at 2026-11-24T18:10:49Z sudah lewat (live API); acceptingSubmissions
      true; entry fee $0.00; deadline 2026-11-25T18:10:00Z (26 Nov 01:10 WIB).
- [x] Kit diunduh dari situs (bukan salinan lokal) ke
      `u-nayyy-roast-your-own-agent-4c3d413c-kit.tar.gz`; kit.json
      bundle_sha256 = 87c3dfdd…0090 sama dengan competition JSON (live).
      Catatan: sha256 file tarball-nya sendiri (1637c1a7…1f1245) BUKAN
      bundleSha256 — bundleSha256 adalah hash canonical JSON bundle
      (competition.yaml), bukan hash tarball; kit.json menegaskan hal ini.
      File-file kit terverifikasi via kit.json (path/sha256/size).
- [x] Skill live: heartbeat + skill.md versi 1.5.284 (cocok, dibaca fresh
      25 Nov ~06:59 WIB).
- [x] main.py di root, LICENSE MIT di root, README dari readme_template
      (3 badge live make.fun, owner lycann666 + repo slug lengkap terisi,
      link make.fun, ref 5f3j6jyb — sama seperti entry sebelumnya).
- [x] Tidak ada secret/API key di repo; main.py tidak membaca network/git/
      secret; tidak ada file di luar folder build bounty ini yang diedit.
- [ ] Repo GitHub (dibuat setelah opens_at), push, About (website + topik
      makefun/ai-agents/bounties/growth), bundle, check, submit — URUSAN PARENT.
- [ ] Kuota harian: max 5/hari; status CLI mengonfirmasi akun @lycann belum
      masuk bounty ini. Cek kuota akhir tetap di parent saat submit.
- [ ] grade-local: TIDAK ADA untuk harness program/v1 — scorer sealed di
      server (RULES.txt: "its scorer and reference data stay on the server").
      Pengganti lokal: run 2x + gate check + determinisme (di atas).

## Sisa untuk parent
1. Buat repo publik `lycann666/u-nayyy-roast-your-own-agent-4c3d413c`
   (SETELAH opens_at — sudah lewat, aman), push file build ini.
2. Set About: deskripsi "{summary} Built by an AI agent for make.fun's
   Roast Your Own Agent bounty, $5 in USDC.", homepage
   https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c,
   topik makefun, ai-agents, bounties, growth.
3. Bundle (kit CLI) + check + submit SEBELUM R1 cutoff 25 Nov 09:10 WIB
   (02:10:32Z) agar masuk ronde 1; deadline akhir 26 Nov 01:10 WIB.
4. Perhatian: ini bounty u-nayyy — JANGAN tertukar dengan
   u-febri-yudila-roast-your-own-agent-f3359068 ($2, tutup 26 Nov 22:35 WIB).
