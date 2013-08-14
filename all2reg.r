#script to separate training data into separate regions
train_data <- read.csv('tweet_reg_train.csv', header=TRUE)

#delete unnecessary columns
train_data[4] <- NULL

names(train_data) <- c("User", "Tweet", "Region")

#remove ngrams containing @user_
regexp <- "@[a-zA-Z0-9_]*"
gsubtry <- gsub(pattern = regexp, replacement = "", x = train_data$Tweet)

#merge gsubtry back into train_data, rename as Tweet
train_clean <- cbind(train_data, gsubtry)
train_clean[2] <- NULL
names(train_clean)[3] <- "Tweet"

#convert factor df to character df
train_clean_char <- data.frame(lapply(train_clean, as.character), stringsAsFactors=FALSE)

#split the data by row value
NewEngland <- subset(train_clean_char, Region=='New England')
MidAtlantic <- subset(train_clean_char, Region == 'Mid Atlantic')
South <- subset(train_clean_char, Region == 'The South')
Midland <- subset(train_clean_char, Region == 'The Midland')
Delmarva <- subset(train_clean_char, Region == 'Delmarva')
Appalachia <- subset(train_clean_char, Region == 'Appalachia')
TheNorth <- subset(train_clean_char, Region == 'The North')
Southwest <- subset(train_clean_char, Region == 'Southwest')
Northwest <- subset(train_clean_char, Region == 'Northwest') 
PacificWest <- subset(train_clean_char, Region == 'Pacific West')

#export each df to csv
write.csv(NewEngland, file="New_England.csv")
write.csv(MidAtlantic, file="Mid_Atlantic.csv")
write.csv(South, file="South.csv")
write.csv(Midland, file="Midland.csv")
write.csv(Delmarva, file="Delmarva.csv")
write.csv(Appalachia, file="Appalachia.csv")
write.csv(TheNorth, file="North.csv")
write.csv(Southwest, file="Southwest.csv")
write.csv(Northwest, file="Northwest.csv")
write.csv(PacificWest, file="Pacific_west.csv")

