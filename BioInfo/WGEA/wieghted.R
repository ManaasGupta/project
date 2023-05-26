# setting direcctory
setwd("C:/Users/manas.DESKTOP-U6BNS3F/Desktop/Rpro/WGEA")

# installing and loading libraries
install.packages('WGCNA') #WGCNA

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("GO.db")

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("impute")

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("preprocessCore")

install.packages("remotes")
remotes::install_github("kevinblighe/CorLevelPlot")

installed.packages("gridExtra")

library(WGCNA)
library(DESeq2)
library(GEOquery)
library(tidyverse)
library(CorLevelPlot)
library(gridExtra)

allowWGCNAThreads()

#1 Fetch Data
list.files(path = ".")

data <- read.delim("GSE152418_p20047_Study1_RawCounts.txt.gz",header = T)

#2 Get MetaData
geo_id<-"GSE152418"
gse<- getGEO(geo_id,GSEMatrix = T)
phenoData<-pData(phenoData(gse[[1]]))
View(gse)

View(phenoData)
phenoData<-phenoData[,c(1,2,46:50)]
View(phenoData)

phenoData<-phenoData[,-c(6)]


View(data)


