#script to compare words used in two regions, using the text mining library and ggplot2

#load data
#starting with Appalachia and Mid Atlantic, two regions which are 
#geographically fairly close, but historically have had very different dialects
#had to make a corpus for the tm package, so copied the region feature word files

my.path <- ('~/GeoTwit/visualizations/')
library(tm)
library(ggplot2)

#create corpus
my.corpus <- Corpus(DirSource(my.path), readerControl= list (reader=readPlain))
summary(my.corpus)

#create shared term document matrix
my_corpus.matrix <- TermDocumentMatrix(my.corpus)

#create df from matrix
my_corpus.df <- as.data.frame(inspect(my_corpus.matrix))

#add column that displays term freq differences between appalachia and mid atlantic
my_corpus.df <- transform(my_corpus.df, freq.dif=mid_atlantic_words_viz.txt-appalachia_words_viz.txt)

#create separate dfs for words said more often in Mid Atlantic vs Appalachia
#and one for words said equally
mid_atlantic.df <- subset(my_corpus.df, freq.dif>0)
appalachia.df <- subset(my_corpus.df, freq.dif<0)
equal.df <- subset(my_corpus.df, freq.dif==0)

#function that returns vector of continuous values for even spacing
optimal.spacing <- function(spaces) {
	if(spaces>1) {
        spacing<-1/spaces
        if(spaces%%2 > 0) {
            lim<-spacing*floor(spaces/2)
            return(seq(-lim,lim,spacing))
        }
        else {
            lim<-spacing*(spaces-1)
            return(seq(-lim,lim,spacing*2))
        }
    }
    else {
        return(0)
    }
}

#apply spacing function to frequencies
mid_atlantic.spacing <- sapply(table(mid_atlantic.df$freq.dif), function(x) optimal.spacing(x))
appalachia.spacing <- sapply(table(appalachia.df$freq.dif), function(x) optimal.spacing(x))
equal.spacing<-sapply(table(equal.df$freq.dif), function(x) optimal.spacing(x))

#now add that spacing back into dfs, where it will become the y column
mid_atlantic.optim <- rep(0, nrow(mid_atlantic.df))
for (n in names(mid_atlantic.spacing)) {
	mid_atlantic.optim[which(mid_atlantic.df$freq.dif==as.numeric(n))] <- mid_atlantic.spacing[[n]]
}
mid_atlantic.df <- transform(mid_atlantic.df, Spacing=mid_atlantic.optim)

appalachia.optim <- rep(0, nrow(appalachia.df))
for (n in names(appalachia.spacing)) {
	appalachia.optim[which(appalachia.df$freq.dif==as.numeric(n))] <- appalachia.spacing[[n]]
}
appalachia.df <- transform(appalachia.df, Spacing=appalachia.optim)

equal.df$Spacing <- as.vector(equal.spacing)


#visualize!
mid_atlantic_vs_appalachia <-  ggplot(mid_atlantic.df, aes(x=freq.dif, y=Spacing))+geom_text(aes(size=mid_atlantic_words_viz.txt, label=row.names(mid_atlantic.df), colour=freq.dif))+
    geom_text(data=appalachia.df, aes(x=freq.dif, y=Spacing, label=row.names(appalachia.df), size=appalachia_words_viz.txt, color=freq.dif))+
    geom_text(data=equal.df, aes(x=freq.dif, y=Spacing, label=row.names(equal.df), size=mid_atlantic_words_viz.txt, color=freq.dif))+
    scale_size(range=c(3,11), name="Word Frequency")+scale_colour_gradient(low="darkred", high="darkblue", guide="none")+
    scale_x_continuous(breaks=c(min(appalachia.df$freq.dif),0,max(mid_atlantic.df$freq.dif)),labels=c("Said More in Appalachia","Said Equally","Said More in Mid Atlantic"))+
    scale_y_continuous(breaks=c(0),labels=c(""))+xlab("")+ylab("")+theme_bw(base_family= 'Helvetica')
ggsave(plot=mid_atlantic_vs_appalachia,filename="ma_app.png",width=13,height=7)



