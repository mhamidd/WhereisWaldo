short_train <- read.csv('short_train.csv', header=TRUE)

#delete unnecessary columns
short_train[1] <- NULL

#remove ngrams containing @user_
regexp <- "@[a-zA-Z0-9_]*"
gsubtry <- gsub(pattern = regexp, replacement = "", x = short_train$Tweet)

#merge gsubtry back into short_train, rename as Tweet
short_train_clean <- cbind(short_train, gsubtry)
short_train_clean[2] <- NULL
names(short_train_clean)[3] <- "Tweet"