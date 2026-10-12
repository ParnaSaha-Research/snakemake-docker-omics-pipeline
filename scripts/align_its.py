import os
import subprocess

os.makedirs("results", exist_ok=True)

fasta_input = "data/fungal_its_contigs.fasta"
aligned_output = "results/its_aligned.fasta"
tree_output = "results/its_tree.nwk"

print("Step 3.1: Running Multiple Sequence Alignment with MAFFT...")
mafft_cmd = f"mafft --auto {fasta_input} > {aligned_output}"
result = subprocess.run(mafft_cmd, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print(f"Alignment saved successfully to {aligned_output}")
else:
    print("Error during MAFFT alignment:")
    print(result.stderr)

print("Step 3.2: Building Phylogenetic Tree with FastTree...")
tree_cmd = f"FastTree -nt {aligned_output} > {tree_output}"
tree_result = subprocess.run(tree_cmd, shell=True, capture_output=True, text=True)

if tree_result.returncode == 0:
    print(f"Phylogenetic tree saved successfully to {tree_output}")
else:
    print("Error during FastTree execution:")
    print(tree_result.stderr)

print("Step 3 downstream analysis complete!")
