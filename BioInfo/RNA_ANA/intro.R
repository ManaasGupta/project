library("tidyverse")
library("dplyr")
df=mpg
attach(df)
head(df)
ggplot(dota = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy))
filter(mpg, cyl == 8)
