#predict region of tweets given word counts

#bring in train data
train_data <- read.csv('short_clean_train.csv')

#bring in region words 
ne_words <- read.csv('ne_wordcount.csv')
app_words <- read.csv('appalachia_wordcount.csv')

#bind the three dataframes columnwise
train_words <- cbind(train_data, ne_words, app_words)

#drop unnecessary columns 
train_words[1] <- NULL
train_words[1] <- NULL

#make New England column
train_words$Is_New_England <- grepl('New England', train_words$Region)

#make Appalachia column
train_words$Is_Appalachia <- grepl('Appalachia', train_words$Region)

#split train_words into two data frames, one for training and one for testing
set.seed(43)
train_words$fold <- sample(1:10, nrow(train_words), replace=TRUE)
train <- subset(train_words, fold != 3)
test <- subset(train_words, fold == 3)

#build, test model
model_glm <- glm(Is_New_England ~ New.England.Words, data = train, family='binomial')
test.predict <- predict(model_glm, test, type="response")
#get performance of predictions
install.packages('ROCR')
library('ROCR')
pred <- prediction(test.predict, test$Is_New_England)

#what % were right
perf <- performance(pred, measure='acc')
plot(perf)

#area under the curve
perf_auc <- performance(pred, measure='auc')

#try it on the test data
test <- read.csv('short_test.csv')
ne_words_test <- read.csv('ne_wordcount_test.csv')
test_words <- cbind(test, ne_words_test)
test_words$Is_New_England <- grepl('New England', test_words$Region)

model_glm_final <- glm(Is_New_England ~ New.England.Words, data = train_words)
predictions <- predict(model_glm_final, test_words, type="response")

