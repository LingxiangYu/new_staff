set.seed(5)  # For reproducibility
dat = data.frame(x=rnorm(10))

dat$ratio = dat$x/lag(dat$x,-1)

require(zoo)
set.seed(123)
x <- zoo(sample(c(1:9), 10, replace = T))
y <- lag(x, -4, na.pad = TRUE)
cbind(x, y)
x1 <- data.frame(x=rnorm(10))
y1 <- lag(x1, -1, na.pad=TRUE)
cbind(x1,y1)