# install lib
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("airway")
# load Libraries
library(DESeq2)
library(tidyverse)
library(airway)
data(airway)
View(airway)
library(ggplot2)

# Gettingg data from airway
sample_info <- as.data.frame(colData(airway))
sample_info <- sample_info[,c(2,3)]
sample_info$dex <- gsub('trt', 'treated', sample_info$dex)
sample_info$dex <- gsub('untrt', 'untreated', sample_info$dex)
names(sample_info) <- c('cellLine', 'dexamethasone')
write.table(sample_info, file = "sample_info.csv", sep = ',', col.names = T, row.names = T, quote = F)

countsData <- assay(airway)
write.table(countsData, file = "counts_data.csv", sep = ',', col.names = T, row.names = T, quote = F)

# preparing counts data
counts_data=read.csv("counts_data.csv")
View(counts_data)

#read sample_info
colData <- read.csv("sample_info.csv")
head(colData)
#make sure row names in ColData === rownnames in counts_data
all(colnames(counts_data) %in% rownames(colData))

# same order
all(colnames(counts_data) == rownames(colData))

#construct a DESeq dataset

dds<-DESeqDataSetFromMatrix(countData = counts_data,colData = colData,design= ~ dexamethasone)
dds

# filtering
keep<-rowSums(counts(dds)) >= 10

dds <- dds[keep,]
dds

# set factor level
dds$dexamethasone<-relevel(dds$dexamethasone,ref="untreated")
dds$dexamethasone



# run DESeq
dds<-DESeq(dds)
res <- results(dds)
res



# Explain
summary(res)
res1<-results(dds,alpha = 0.01)
summary(res1)


# contrast
resultsNames(dds)


#plots
plotMA(res)

#Volcano Plots
par(mfrow=c(1,1))
# Make a basic volcano plot
with(res, plot(log2FoldChange, -log10(pvalue), pch=20, main="Volcano plot"))

# Add colored points: blue if padj<0.01, red if log2FC>1 and padj<0.05)
with(subset(res, padj<.01 ), points(log2FoldChange, -log10(pvalue), pch=20, col="blue"))
with(subset(res, padj<.05 & abs(log2FoldChange)>2), points(log2FoldChange, -log10(pvalue), pch=20, col="red"))



