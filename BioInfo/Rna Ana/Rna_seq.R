#installing and load libraries
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("DelayedArray")


if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("EnhancedVolcano")

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("RUVSeq")#may not work so download .zip file 

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("DESeq2") #may not work so download .zip file 
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("Rsubread")
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("Rqc")

library(Rsubread)
library(R.utils)
library(EnhancedVolcano)
library(pheatmap)
library(ggplot2)
library(RUVSeq)
library(data.table)
library(DESeq2)
library(RColorBrewer)
library(Rqc)


# Downlaod fastqc files

url<-"ftp.sra.ebi.ac.uk/vol1/fastq/SRR592/006/SRR5924196/SRR5924196_1.fastq.gz"
destination<-"SRR5924196_1.fastq.gz"
download.file(url,destination)

url<-"ftp.sra.ebi.ac.uk/vol1/fastq/SRR592/006/SRR5924196/SRR5924196_2.fastq.gz"
destination<-"SRR5924196_2.fastq.gz"
download.file(url,destination)

url<-"ftp.sra.ebi.ac.uk/vol1/fastq/SRR592/008/SRR5924198/SRR5924198_1.fastq.gz"
destination<-"SRR5924198_1.fastq.gz"
download.file(url,destination)

url<-"ftp.sra.ebi.ac.uk/vol1/fastq/SRR592/008/SRR5924198/SRR5924198_2.fastq.gz"
destination<-"SRR5924198_2.fastq.gz"
download.file(url,destination)

# Download Genome file here for yeast---

url<-"ftp://ftp.ensembl.org/pub/release-96/fasta/saccharomyces_cerevisiae/dna/Saccharomyces_cerevisiae.R64-1-1.dna_sm.toplevel.fa.gz"
destination<-"Saccharomyces_cerevisiae.R64-1-1.dna_sm.toplevel.fa.gz"
download.file(url,destination)
gunzip(destination)

#Downloading GTF file----
url<-"ftp://ftp.ensembl.org/pub/release-96/gtf/saccharomyces_cerevisiae/Saccharomyces_cerevisiae.R64-1-1.96.gtf.gz"
destination<-"Saccharomyces_cerevisiae.R64-1-1.96.gtf.gz"
download.file(url,destination)
gunzip(destination)

#Fastqc
rqc(path=getwd(),pattern=".fastq.gz")


#Building Index----
buildindex("Sc_full_index_rsubread",
           "Saccharomyces_cerevisiae.R64-1-1.dna_sm.toplevel.fa",
           indexSplit=F)

#check if all paired ends
reads1 <- list.files(pattern = "_1.fastq.gz$" )
reads2 <- list.files(pattern = "_2.fastq.gz$" )
all.equal(length(reads1),length(reads2))

#Performing Alignment----
align(index="Sc_full_index_rsubread",
      readfile1=reads1,
      readfile2=reads2,
      input_format="gzFASTQ",
      output_format="BAM",
      nthreads=10)

#Checking the BAM files generated----
bam.files <- list.files(pattern = ".BAM$", full.names = TRUE)
bam.files

#Checking Mapping quality
props <- propmapped(files=bam.files)
props

# Feature Counts 

fcLim <- featureCounts(files = bam.files,
                       annot.ext="Saccharomyces_cerevisiae.R64-1-1.96.gtf",
                       GTF.featureType="exon",
                       GTF.attrType="gene_id",
                       isGTFAnnotationFile=TRUE,
                       isPairedEnd = TRUE)
fc <- data.frame(fcLim[['counts']])
colnames(fc)<-c("Normal","Tumor")
View(fc)
