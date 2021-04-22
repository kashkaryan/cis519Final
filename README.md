# The Connotations of News Articles

For this project, we were interested in how media articles are written with the intent of subliminally influencing their readers. More specifiaclly, we wanted to test a machines ability to predict the connotations journalists try to embed onto their article from the get-go in their headers. Our goal was to cultivate a novel dataset that will help us predict the connotation of a news article.

### Making a Dataset

To make the project more interesting and manageable, our team decidede to cultivate a novel dataset centered around colleges, more specfically Penn. We used the centuries old Penn newspaper, [The Daily Pennsylvanian](https://www.thedp.com/) and their [archive](https://dparchives.library.upenn.edu/?a=cl&cl=CL2&e=-------en-20--1--txt-txIN-------) through the Penn library. One by one, we added emotionally charged and neutral headers into a large data set of 3000 headers, where we labeled each with a 1 if the connotation was neutral, a 2 if it was posiitve, and a 0 if it was negative. Since there is a level of subjectivity to the task, our team used crowdsourcing through Mechanical Turk (where poeple were asked to rate how a header made them feel) to aggregate workers' opinions into a more reliable data set. The quality control of the data set was done in Mechanical Turk by using a majority vote method, as well as us team members scanning through each header and the final label for each.

### Model

From here, using scikit we built 4 types of models that learned on our data set. The results are delineated in our report [here](https://docs.google.com/document/d/1yyBPh8OmRPIgCCPiCLrzVnYdvOMBwgYXWagA5v2iUiQ/edit?ts=607ccf82#).
