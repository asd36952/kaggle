setwd("C:\\Users\\SeongWooLim\\Desktop\\kaggle")
train = read.csv("train.csv")
test = read.csv("test.csv")
test$Survived = NA
combined = rbind(train, test)
combined$Survived=as.factor(combined$Survived)
combined$Pclass=as.factor(combined$Pclass)
combined$Name=as.character(combined$Name)
combined$Ticket=as.character(combined$Ticket)
combined$Cabin=as.character(combined$Cabin)
combined[is.na(combined$Age),]$Age=mean(combined[!is.na(combined$Age),]$Age)
combined[is.na(combined$Fare),]$Fare=median(combined[!is.na(combined$Fare),]$Fare)
table.embarked=table(combined[combined$Embarked!="",]$Embarked)
combined[combined$Embarked=="",]$Embarked=names(table.embarked)[which.max(table.embarked)]
library(randomForest)
train=combined[combined$PassengerId %in% train$PassengerId,]
test=combined[combined$PassengerId%in% test$PassengerId,]
myformula = Survived ~ Pclass + Sex + Age + SibSp+ Parch + Fare + Embarked
mymodel = randomForest(myformula, data=train,maxnodes=8)
test$Survived = predict(mymodel, newdata=test)
write.csv(test[c("PassengerId", "Survived")], "submission.csv", row.names=FALSE)