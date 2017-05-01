formatMhsmm <- function(data){

  nb.sequences = nrow(data)
  nb.observations = length(data)

  #transform list to data frame
  data_df <- data.frame(matrix(unlist(data), nrow = nb.sequences, byrow=F))


  #iterate over these in loops
  rows <- 1:nb.sequences
  observations <- 0:(nb.observations-1)

  #build vector with id values
  id = numeric(length = nb.sequences*nb.observations ) 

  for(i in rows)
  {
    for (j in observations)
    {
      id[i+j+(i-1)*(nb.observations-1)] = i
    }
  }

  #build vector with observation values
  sequences = numeric(length = nb.sequences*nb.observations) 

  for(i in rows)
  {
    for (j in observations)
    {
      sequences[i+j+(i-1)*(nb.observations-1)] = data_df[i,j+1]
    }
  }

  data.df = data.frame(id, sequences)

  #creation of hsmm.data object needed for training
  N <- as.numeric(table(data.df$id))
  train <- list(x = data.df$sequences, N = N)
  class(train) <- "hsmm.data"

  return(train)
}

#myArgs <- commandArgs(trailingOnly = TRUE)
#n<-strtoi(myArgs)

elength<-scan("C://Users//Dhruv_Passey_PC//Downloads//LogDiver//Final Log Analysis Tool//LogAnalysisTool//Temp_Output//HashedErrorTuplesLength.txt")
nonelength<-scan("C://Users//Dhruv_Passey_PC//Downloads//LogDiver//Final Log Analysis Tool//LogAnalysisTool//Temp_Output//HashedNonErrorTuplesLength.txt")

library(mhsmm)

con<-file('C://Users//Dhruv_Passey_PC//Downloads//LogDiver//Final Log Analysis Tool//LogAnalysisTool//Temp_Output//HashedErrorTupleDataFinal.csv')
open(con)

i<-1
sum<-0

# 3 states HSMM    
J=3

start.pois <- hsmmspec(init = rep(1/J, J),transition = matrix(c(0, .5, .5, .5, 0, .5, .5, .5, 0), nrow = J),parms.emis = list( mu=c(4, 12, 23), sigma = c(1, 1, 1)),
	sojourn = list(lambda = c(9, 25, 40), shift = c(5, 95, 45),type = "poisson"),dens.emis = dnorm.hsmm)
	
M <- 500

while (i<=length(elength))
{
	dataset<-read.table(con,skip=sum,nrow=elength[i])
	sum<-sum + elength[i]
	i<-i + 1
	train <- formatMhsmm(dataset)
	start.pois <- hsmmfit(train, start.pois, mstep = mstep.norm, M = M)
	
}

summary(start.pois)

close(con)

