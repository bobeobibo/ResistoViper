# AR-panel-snake

Snakemake workflow for processing targeted AR gene panel sequencing data

In order to run it, you need:
- trimmomatic (v. 0.39). Please write the path where the adapter sequences are stored to config/config.yaml
- bowtie2 (v. 2.5.3)
- human genome (bowtie2-indexed). Please write the path where it is stored to config/config.yaml
- reference AR gene sequences (bowtie2-indexed) (already present in data/ folder)
- samtools (v. 1.6)
- bedtools (v. 2.31.1)

A small test dataset for trying the pipeline can be found in workflow/test_data/

