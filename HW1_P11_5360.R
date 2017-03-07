#HW1_P11_5360 R version

data=read.table("ES.asc",header=T,as.is=TRUE,sep=",")

data0<-head(data,1000000)
data1 <-as.data.frame(matrix(0, ncol = 1000, nrow = 1000000))
names(data1) <- paste0('Return', 1:1000)
for (i in 1:1000){
  data1[,i]<-c(rep(NA,i),diff(data0$Close,lag=i)/data0$Close[1:(1000000-i)])
}

sigma_tau <- apply(data1,2,sd,na.rm=TRUE)
tau<- c(1:1000)
plot(tau,sigma_tau,main="lin-lin")
plot(log(tau),log(sigma_tau),main="log-log")

lin<-lm(sigma_tau~tau)
summary(lin)
1/(1+exp(-1.635e-05))

log<-lm(log10(sigma_tau)~log10(tau))
summary(log)