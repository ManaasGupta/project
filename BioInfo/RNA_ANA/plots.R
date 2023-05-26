# Script - GGplot and visualize gene expression data
# loading libs
setwd("C:/Users/manas.DESKTOP-U6BNS3F/Desktop/Rpro/RNA_ANA")
library(tidyverse)
library(ggplot2)

# read file 
dat_long <- read.delim("GSE183947_data_long.txt", header = T,sep = ",")
dat_long
View(dat_long)

# barPlot
dat_long %>%
  filter(gene == "BRCA1") %>%
  ggplot(.,aes(x=samples , y=FPKM , fill= tissue))+
  geom_col()
