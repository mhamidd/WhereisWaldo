#load in full tweet text file
full_tweets <- read.table("full_text.txt", sep="\t", quote="", row.names=NULL, stringsAsFactors = FALSE)

View(full_tweets)

#convert latlong to states to regions
#first, I'm just going to make a new df of what will be the X,Y coordinates
splitUTM <- full_tweets[,4:5]

#rename column headers as lat/long
names(splitUTM) <- c("Y", "X")

#these columns are mixed up. V5 is longitude, or X. V4 is latitude, or Y
#reorder 
splitUTM_fixed <- splitUTM[,c("X", "Y")]

#create data frame wherein col 1 is longitude and col 2 is latitude
#prepare spatial polygons object with one sp / state
library(sp)
library(maps)
library(maptools)
latlong2state <- function(pointsDF) {
states <- map('state', fill=TRUE, col = "transparent", plot=FALSE)
IDs <- sapply(strsplit(states$names, ":"), function(x) x[1])
states_sp <- map2SpatialPolygons(states, IDs=IDs, proj4string=CRS("+proj=longlat +datam=wgs84"))

#convert pointsDF to a SpatialPoints object
points_sp <- SpatialPoints(pointsDF, proj4string=CRS("+proj=longlat + datum=wgs84"))

# get indices of the Polygons object containing each point
indices <- over(points_sp, states_sp)

# get state names of the PO
stateNames <- sapply(states_sp@polygons, function(x) x@ID)
stateNames[indices]
}

#run latlong2state over data
states <- latlong2state(splitUTM_fixed)

#convert states to regions
#New England: ME, NH, VT, MA, RI, CT
#Mid-Atlantic: NJ, District of Columbia, NY
#Delmarva: MR, DE
#The North: ND, SD, MI, WI, MN
#The Midland: OH, IN, IL, IA, MO, NE, KS, PA
#Appalachia: WV, KT
#The South: SC, MI, FL, AL, GA, LA, TX, VA, AR, NC, TN
#Southwest: AZ, NM, CO, UT, NV
#Northwest: MT, WY, ID
#Pacific West: CA, OR, WA

states2reg <- gsub("maine|vermont|massachusetts|connecticut|new hampshire|rhode island", "New England", states)
states2reg <- gsub("new jersey|district of columbia|new york", "Mid Atlantic", states2reg)
states2reg <- gsub("maryland|delaware", "Delmarva", states2reg)
states2reg <- gsub("north dakota|south dakota|michigan|wisconsin|minnesota", "The North", states2reg)
states2reg <- gsub("ohio|indiana|illinois|iowa|missouri|nebraska|kansas|pennsylvania", "The Midland", states2reg)
states2reg<- gsub("west virginia|kentucky", "Appalachia", states2reg)
states2reg <- gsub("south carolina|north carolina|virginia|florida|mississippi|georgia|alabama|louisiana|texas|arkansas|tennessee|oklahoma","The South", states2reg)
states2reg <- gsub("arizona|new mexico|colorado|utah|nevada", "Southwest", states2reg)
states2reg <-gsub("montana|wyoming|idaho", "Northwest", states2reg)
states2reg <-gsub("california|oregon|washington", "Pacific West", states2reg)
names(states2reg) <- c(,"Region")

#merge regions into full tweets df
#first make it a df
states2reg <- as.data.frame(states2reg)
full_tweets_reg <- cbind(full_tweets, states2reg)

#drop unnecessary columns
full_tweets_reg[2:5] <- list(NULL)

#ok, now I think I need to split this df into test and train and write both to csv
set.seed(50)
full_tweets_reg$fold <- sample(1:10, nrow(full_tweets_reg), replace=TRUE)
train <- subset(full_tweets_reg, fold != 3)
test <- subset(full_tweets_reg, fold==3)
write.csv(test, "tweet_reg_test.csv", row.names=FALSE)
write.csv(train, "tweet_reg_train.csv", row.names=FALSE)

