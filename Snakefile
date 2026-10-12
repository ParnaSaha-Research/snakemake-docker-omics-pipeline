%cd /content/pipeline

snakefile_code = '''rule all:
    input:
        "results/its_summary_table.csv",
        "results/genus_distribution_plot.png",
        "results/length_distribution_plot.png",
        "results/its_aligned.fasta",
        "results/its_tree.nwk"

rule enrich_its:
    input:
        fasta="data/fungal_its_contigs.fasta"
    output:
        csv="results/its_summary_table.csv"
    shell:
        "python scripts/enrich_its.py"

rule visualize_its:
    input:
        csv="results/its_summary_table.csv"
    output:
        "results/genus_distribution_plot.png",
        "results/length_distribution_plot.png"
    shell:
        "python scripts/visualize_its.py"

rule align_and_tree:
    input:
        fasta="data/fungal_its_contigs.fasta"
    output:
        aligned="results/its_aligned.fasta",
        tree="results/its_tree.nwk"
    shell:
        "python scripts/align_its.py"
'''

with open("Snakefile", "w") as f:
    f.write(snakefile_code)

print("Snakefile created successfully in the project root!")
