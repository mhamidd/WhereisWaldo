test_data <- read.csv('short_train.csv', header=TRUE)

#delete fold column
test_data[4] <- NULL

#delete region column
test_data[3] <- NULL

#rename columns
names(test_data) <- c("User", "Tweet")

write.csv(test_data, file="test_clean.csv")