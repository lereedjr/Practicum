library(RJSONIO)

info <- fromJSON("hotels.json")
info
info2 <- as.data.frame(info)
plot(info)
df <- data.frame(matrix(unlist(info), nrow=469, byrow=T),stringsAsFactors=FALSE)
df
str(df)

str(info)
library(qdap)
frequent_terms <- freq_terms(info, 25)
frequent_terms
plot(frequent_terms)
