#predict region of tweets given word counts

#bring in train data
train_data <- read.csv('short_clean_train.csv')

#bring in region words 
ne_words <- read.csv('ne_wordcount.csv')

#bind the two dataframes columnwise
train_words <- cbind(train_data, ne_words)

#drop unnecessary columns 
train_words[1] <- NULL
train_words[1] <- NULL

#make model matrix of Region/Not Region boleean columns
train_words_mm <- model.matrix(~factor(train_words$Region)-1, data=train_words)

#bind mmodel matrix to train data
train_words_numbers <- cbind(train_words, train_words_mm)

#rename boolean columns
names(train_words_numbers) <- c('User', 'Tweet', 'Region', 'New.England.Words', 'Unnamed_Reg', 'Appalachia', 'Delmarva', 'Mid_Atlantic', 'New_England', 'Northwest', 'Pacific_West', 'Southwest', 'The_Midland', 'The_North', 'The_South') 

#make threshold column
median(train_words_numbers$New.England.Words)
train_words_numbers$WordAverage <- train_words_numbers$New.England.Words > 5

#split train_ratio into two data frames, one for training and one for testing
set.seed(43)
train_words_numbers$fold <- sample(1:10, nrow(train_words_numbers), replace=TRUE)
train <- subset(train_words_numbers, fold != 3)
test <- subset(train_words_numbers, fold == 3)

#build, test model
model <- lm(New_England ~ New.England.Words, data = train)
test.model <- predict(model, test)

#define evaluation function (mean absolute error)
mae <- function(x, y) {
  return(mean(abs(x - y)))
}

#get training and test error
mae(fitted(model), train$New_England)
mae(predict(model, test), test$New_England)


#time to bring in actual test data 
test <- read.csv('short_test.csv')
ne_words_test <- read.csv('ne_wordcount_test.csv')
test_words <- cbind(test, ne_words_test)

names(test_words)[6] <- "New_England"
test_words$New_England <- as.logical(test_Words$New_England)

#build final lm model
model_final <- lm(New_England ~ New.England.Words, data = train_words_numbers)
predictions <- predict(model_final, test_words)

#try glm, since lm didn't work so well

#make New England column
train_words$Is_New_England <- grepl('New England', train$Region)

#build, test model
model_glm <- glm(Is_New_England ~ New.England.Words, data = train, family='binomial')
test.predict <- predict(model_glm, test, type="response")
#get performance of predictions
install.packages('ROCR')
library('ROCR')
pred <- prediction(test.predict, test$Is_New_England)

#what % were right
perf <- performance(pred, measure='acc')
plot perf

# % of elements I thought were in the class
perf_thought <- performance(pred, measure="prec")
plot perf_thought

# % of elements that are actually in class that I predicted to be in class
perf_actual <- performance(pred, measure='recall')
plot perf_actual

#area under the curve
perf_auc <- performance(pred, measure='auc')

#try it on the test data
test <- read.csv('short_test.csv')
ne_words_test <- read.csv('ne_wordcount_test.csv')
test_words <- cbind(test, ne_words_test)
test_words$Is_New_England <- grepl('New England', test$Region)

model_final_glm <- glm(Is_New_England ~ New.England.Words, data = train_words)
predictions <- predict(model_final_glm, test_words, type="response")

submission <- data.frame(User=test_words$User, New_England_Probability=predictions)
write.csv(submission, "twitter_predictions_new_england.csv", row.names=FALSE)


#time to predict Appalachia
app_words <- read.csv('appalachia_wordcount.csv')
#bind the two dataframes columnwise
train_words <- cbind(train_data, app_words)

#drop unnecessary columns 
train_words[1] <- NULL
train_words[1] <- NULL

#make New England column
train_words$Is_New_England <- grepl('New England', train$Region)
