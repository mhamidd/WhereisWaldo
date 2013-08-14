#script to get and plot tweets by location
library("maps")
map("state")
full_tweets <- read.table("full_text.txt", sep="\t", quote="", row.names=NULL, stringsAsFactors = FALSE)
names(full_tweets) <- c('User', 'Date', 'Loc', 'Lat', 'Long', 'Tweet')

#make map 
map("usa", col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05)
points(x=full_tweets$Long, y=full_tweets$Lat, col='red')

#plot coordinates onto map
library(sp)
coordinates(full_tweets) <- c("lat", "long")
map('usa')
plot(full_tweets$lat, full_tweets$long)