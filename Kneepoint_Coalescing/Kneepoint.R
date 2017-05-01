y<-scan("C://Users//Dhruv_Passey_PC//Downloads//LogDiver//Final Log Analysis Tool//LogAnalysisTool//Temp_Output//TimeWindow.txt")
x<-scan("C://Users//Dhruv_Passey_PC//Downloads//LogDiver//Final Log Analysis Tool//LogAnalysisTool//Temp_Output//TimeStep.txt")

get.elbow.points.indices <- function(x, y, threshold) {
  d1 <- diff(y) / diff(x) # first derivative
  d2 <- diff(d1) / diff(x[-1]) # second derivative
  indices <- which(abs(d2) > threshold)  
  return(indices)
}

myArgs <- commandArgs(trailingOnly = TRUE)
n<-strtoi(myArgs)


# first approximate the function, since we have only a few points
ap <- approx(x, y, n=1000, yleft=min(y), yright=max(y))
x <- ap$x
y <- ap$y

indices <- get.elbow.points.indices(x, y, n) # threshold for huge jump = 1e4
x[indices]
#[1] 6.612851 # there is one such point
#plot(x, y, pch=19)
#points(x[indices], y[indices], pch=19, col='red')