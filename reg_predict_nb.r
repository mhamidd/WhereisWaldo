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

#make New England column
train_words$Is_New_England <- grepl('New England', train$Region)

#make Appalachia column
train_words$Is_Appalachia <- grepl('New England', train$Region)

#split train_ratio into two data frames, one for training and one for testing
set.seed(43)
train_words$fold <- sample(1:10, nrow(train_words), replace=TRUE)
train <- subset(train_words, fold != 3)
test <- subset(train_words, fold == 3)

#install the naive bayes library
install.packages('e1071')
library('e1071')

#build, test model
model_nb <- glm(Is_New_England ~ New.England.Words, data = train, family='binomial')
test.predict <- predict(model_nb, test, type="response")
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

model_glm_final <- glm(Is_New_England ~ New.England.Words, data = train_words)
predictions <- predict(model_final_nb, test_words, type="response")

