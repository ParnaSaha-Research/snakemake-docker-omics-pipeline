import csv
import os

fasta_path = "data/fungal_its_contigs.fasta"
csv_output = "results/its_summary_table.csv"
report_output = "results/its_summary_report.txt"

os.makedirs("results", exist_ok=True)

records = []
current_id = ""
current_header = ""
current_seq = []

with open(fasta_path, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                seq = "".join(current_seq)
                length = len(seq)
                gc_count = seq.upper().count("G") + seq.upper().count("C")
                gc_pct = (gc_count / length) * 100 if length > 0 else 0
                records.append((current_id, current_header, length, round(gc_pct, 2)))
            
            current_header = line[1:].strip()
            parts = current_header.split()
            current_id = parts[0] if parts else current_header
            current_seq = []
        else:
            current_seq.append(line)

if current_id:
    seq = "".join(current_seq)
    length = len(seq)
    gc_count = seq.upper().count("G") + seq.upper().count("C")
    gc_pct = (gc_count / length) * 100 if length > 0 else 0
    records.append((current_id, current_header, length, round(gc_pct, 2)))

# Write CSV Table
with open(csv_output, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Isolate_ID", "Full_Header", "Length_bp", "GC_Content_Pct"])
    for rec in records:
        writer.writerow(rec)

# Write Enhanced Text Report
with open(report_output, "w") as repfile:
    repfile.write("=== Fungal ITS Contig Summary & GC Report ===\n")
    repfile.write(f"Input File: {fasta_path}\n")
    repfile.write("-" * 65 + "\n")
    repfile.write(f"{'Isolate ID':<12} | {'Length (bp)':<11} | {'GC (%)':<6} | {'Description'}\n")
    repfile.write("-" * 65 + "\n")
    for rec in records:
        repfile.write(f"{rec[0]:<12} | {rec[2]:<11} | {rec[3]:<6} | {rec[1]}\n")
    repfile.write("-" * 65 + "\n")
    repfile.write(f"Total isolates processed: {len(records)}\n")

print("Enrichment script executed successfully!")
