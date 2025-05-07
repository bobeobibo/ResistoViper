# ResistoViper

This pipeline creates resistome profiles from raw metagenomic sequencing reads.

It outputs relative abundance values for each ARG (antibiotics resistance gene) and sample, ARG richness values for each sample, and frequency values for each ARG. 
It also creates taxonomy profiles.

Input:
- Paired sequencing reads (.fq), organized in individual folders

Output («results» folder):
- Matrix with relative abundance values for each ARG (All.RPKM)
- Table with ARG richness values for each sample (All.adiv)
- Frequency table with the number of samples containing each ARG (All.ARsample_counts)
- Matrix with relative abundance values for each taxa (All.RPM_mph)

In order to run the pipeline, you will need:
- Snakemake (our version: 7.32.4)
- Cutadapt (our version: 4.9) You can adjust this step’s settings to fit your data (the current settings are set for DNBSEQ-G400)
- Trimmomatic (our version: 0.39)
- Biobloom (our version: 2.3.5-1-gfa70-dirty)
- Bowtie2 (our version: 2.5.3)
- Samtools (our version: 1.19.2)
- Bedtools (our version: 2.31.1)
- MetaPhlan (our version: 4.0.0)

All of these instruments can be installed with bioconda. Also see workflow/envs/environment.yml

You will also need the databases:
- Human genome in .fasta format (masked hg19, preferably)

Human genome can be downloaded at http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/
```bash
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.masked.gz
gunzip hg19.fa.masked.gz
```
After downloading, you need to create a BioBloom filter with the following command:
```bash
biobloommaker -p your_prefix /path/to/your/human/genome/hg19.fa
```
Biobloom filter (.bf) and an accessory .txt files will be created.

Make sure to add path to the both files to the config/config.yaml file!
- MEGARes database

We use a subset of MEGARes 3.0 database that is already present in the data/ folder.

However, if you would like to try full database or previous MEGARes versions, you need to download them from https://www.meglab.org/megares/download/

Then, you need to index the database:
```bash
bowtie2-build your_megares_version.fa your_prefix
```
Make sure to add path to the indexed MEGARes database to the config/config.yaml file!

Note: the scripts are designed to follow MEGARes database header structure, so replacing MEGARes with other databases will likely cause errors



A small test dataset for trying the pipeline can be found in workflow/test_data/reads/

