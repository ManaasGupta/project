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


#loading file
f<-read.csv("GSE143630_RCC_htseq_counts.txt",sep = " ",row.names = 1)
View(f)
length(row.names(f))

#T1 Stage Count--
count_of_T1=length(grep(x = colnames(f),
                        pattern = "^T1."))
count_of_T1

#t2 Stage Count--
count_of_T2=length(grep(x = colnames(f),
                        pattern = "^T2."))
count_of_T2

#Filtering 
filter <- apply(f,1,function(x) length(x[x>0])>=2)
filtered <- f[filter,]
genes <- row.names(filtered)
length(genes)


t1<-rep(c("T1"),each=count_of_T1)
t2<-rep(c("T2"),each=count_of_T2)
x<-c(t1,t2)
x
x<-as.factor(x)
x
set <- newSeqExpressionSet(as.matrix(filtered),
                           phenoData = data.frame(x,
                                                  row.names=colnames(filtered)))
set

#Setting Color Theme
colors <- brewer.pal(3, "Set2")
plotPCA(set, col=colors[x], cex=1.2)
set <- betweenLaneNormalization(set, which="upper")
plotRLE(set, outline=FALSE, ylim=c(-4, 4), col=colors[x]) #
plotPCA(set, col=colors[x], cex=1.2)

differences <- makeGroups(x)
differences
set3 <- RUVs(set, genes, k=1, differences)
pData(set3)



#compute deferential analysis
dds <- DESeqDataSetFromMatrix(countData = counts(set3),
                              colData = pData(set3),
                              design= ~ W_1 + x)
dds <- DESeq(dds)

res <- results(dds)
View(res)
#saving results
write.table(res, file = "RUVseq_analysis.csv",
            sep = ",", col.names = NA,
            qmethod = "double")

df <- read.csv("RUVseq_analysis.csv")
View(df)

names(df)
#plot Data
#Volcano Plot
EnhancedVolcano(res,lab = row.names(res),x="log2FoldChange",y="pvalue")
