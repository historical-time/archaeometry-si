# Periodo output
library(dplyr)

file.in <- "docs/periodo-dataset.csv"
# metadata
file.metadata <- file.info(file.in)
file.metadata.cdate <- as.Date(file.metadata$ctime)
# data
df <- read.csv(file.in, stringsAsFactors = FALSE)
all.dates <- c(as.numeric(df$start), as.numeric(df$stop))
today <- as.numeric(format(Sys.Date(), "%Y"))
yesterday <- -10000
all.dates <- all.dates[all.dates >= yesterday]
all.dates <- all.dates[all.dates <= today]
ggplot2::ggplot() +
  ggplot2::labs(title = paste0("Counts of Period0's periods 'start' and 'stop' dates (n= ", length(all.dates), ", limited to the interval ", yesterday, " to ", today, ")"),
                subtitle = paste0("dataset accessed the ", file.metadata.cdate)) +
  ggplot2::aes(all.dates) +
  ggplot2::geom_histogram(binwidth = 100, colour="black", fill="white") +
  ggplot2::xlim(yesterday, today)  +
  ggplot2::theme_bw()
