index:7
banner_title:ANOVA and R Bootcamp (Biol 2003)
banner_description: Learn how to implement ANOVA in the R programming language
banner_img: anova.png
default_code: r

#ANOVA and the R Programming Language

##ANOVA

ANOVA, or Analysis of Variance, is a common tool used to test whether multiple samples are being taken from different distributions. For example imagine we give an IQ test to a random sample of students from different universities.  We want to determine if there is statistically significant different between the IQ of students at different universities. In other words we want to determine if one or more university samples are taken from different IQ distributions than the others. If we were testing just two universities, we would just use the t-test and be on our way. But having more than two samples can lead to problems. For instance if we were testing ten universities, we would match every university with every other one leading to 9+8+…+2+1 = (9*10)/2 = 45 different comparisons. If we use 0.95 as our confidence level for each test, then our confidence level for all 45 tests is (0.95)^45 which is about 0.01. This is very bad and leaves plenty of room to make mistakes. At this confidence level we could easily stumble on two universities which are taken from the same IQ distribution, but by natural variation we determined that they are significantly different. This is what is known as type I error where we reject the null hypothesis even though it is correct.

ANOVA is a statistical tool which avoids these errors. Instead of comparing each sample with every other sample, ANOVA’s trick is to try pooling all of the data as if it were from one sample. ANOVA then looks at the means and the “sum of square differences from the mean” for the whole pool. It then does the same for each of the individual samples. The idea is that if all of the samples were taken from the same distribution, then all of their individual means should be close to the pool’s mean. Additionally, the sum of square differences from the means for each of the samples added together should be close to the pool’s sum of square differences. For example take a look at these images from Wikipedia’s ANOVA page. (Don’t worry about the equations on the graph, just look at the shapes of the distributions.)

![ANOVA with samples from the same distribution](img/anova1.png)

The orange represents the distribution of the X1 through X4 being pooled together, where Xi represents the distribution of a particular sample. This could be the distribution of IQs at different universities for example. Notice how the means for X1 through X4 are all similar to the pool. Now consider every observation in a particular sample Xi. Take every element in Xi, subtract it from the mean of Xi, square it, and then add all the results together. This is what we mean by “sum of the squared differences from the mean”. Now do this for every Xi and add the results together. In this case the “sum of the squared differences from the mean” for each Xi added together are close to the “sum of the squared differences from the mean” for the entire pool. This makes us believe that all of these samples are taken from the same distribution.

Now consider this graph the same Wikipedia page:

![ANOVA with samples form different distributions](img/anova2.jpg)

The orange distribution still represents the pool, but notice how each of the blue Xi distributions are much pointier and have means in special areas. Since the means are very different from each other, and the sum of the squared differences from the mean for each Xi added together will be much smaller than the one for the entire pool, we can conclude that at least one of these samples is significantly different than another sample.

##R Programming

Now that we have better intuition for what kinds of questions we can ask with ANOVA, we can begin to translate that knowledge into an operation we can perform using the R programming language. You can download R for your system [here](https://cran.r-project.org/).  However, if you want to follow along in your browser, you are free to do so at the [R-fiddle site](http://www.r-fiddle.org/). If you are using r-fiddle, notice the gray box on the lower portion of the screen. We will just be using that, so feel free to expand that window.

We will be looking at this data about catching fish in various lakes in Minnesota. Our question is about whether or not there is a significant difference in the amount of caught fish between any of these lakes. We can use ANOVA for this quite easily. Here is our dataset.

<pre>
	| Rice Lake     | Long Lake     | Island Lake  |
	| :------------ |:--------------| :------------|
	| 68            | 150           | 160          |
	| 66            | 153           | 130          |
	| 110           | 102           | 142          |
	| 82            | 97            | 133          |
	| 90            | 95            | 130          |
	| 88            | 170           | 144          |
	| 140           | 80            | 170          |
	| 151           | 76            | 151          |
	| 123           | 102           | 135          |
	| 122           | 104           | 140          |
</pre>

Now if we were in Excel, there would be no problem. This data is fine and we can put it into Excel’s premade ANOVA function. We are in R though so things are a little bit different. The problem is in how we are structuring our data. This might be an okay tabulation for human readers, but it is actually a weak way to represent data. Look at any observation. Notice how a cell represents two pieces of information, the number of fish AND the name of the lake the fish were caught in. One of the principles of good data design is in spreading out your information so that one column just tells you one thing about that observation. You might think I’m crazy, but there is a lot of theory on this. Read this paper by Hadley Wickham on tidy data [here](http://vita.had.co.nz/papers/tidy-data.pdf). Within R we will need to convert into something like this:

<pre>
	| Count         | Lake          |
	| :------------ |:--------------|
	| 68            | Rice Lake     |
	| 66            | Rice Lake     |
	| ...           | ...           |
	| 150           | Long Lake     |
	| 153           | Long Lake     |
	| ...           | ...           |
	| 160           | Long Lake     |
	| 130           | Long Lake     |
	| ...           | ...           |
</pre>

This will turn our 10 by 3 table of data into a 30 by 2 size table. The idea is we want to test count sampling with particular lake variables, just as we might test IQ sampling with university variables. In this form we could also add any additional column property we want. Maybe we wanted to test fish count for time of day. (Morning, Afternoon, night. For example) Or perhaps weather would be a good property. If all of these properties were sampled randomly, then we would get to ask even more questions than if we were left with just the count/Lake name property that the original table offered. 

As an exercise, we will create the original table first and covert it over for our use.

Copy and paste this code into your R/R-fiddle console and press enter.

	fish <- data.frame( Rice_Lake = c(68,66,110,82,90,88,140,151,123,122), Long_Lake = c(150,153,102,97,95,170,80,76,102,104), Island_Lake = c(160,130,142,133,130,144,170,151,135,140) )

Don’t worry too much about the semantics of this piece of code. Intuitively this just makes the table we saw previously and gives it a label of ‘fish’. Too see this table in its formatted glory, just type ‘fish’ and press enter. Here is a screenshot from my computer for reference:

![Fish data in r-fiddle](img/r-fiddle.png)

Now we need to convert this table into its happier tidy counterpart. To do this I have used this expression: 

	tidy_fish <- data.frame(count = c(fish[['Rice_Lake']], fish[['Long_Lake']], fish[['Island_Lake']]), lake = c( rep('Rice_Lake', 10), rep('Long_Lake', 10), rep('Island_Lake', 10) ))


This is a mess of an expression, but it gets the job done. Really all you need to know is that this expression converted our non-tidy table into a tidy one, allowing us to use an ANOVA function that R provides for us. For more information on the syntax of an R command like this, refer to [this page]( http://adv-r.had.co.nz/Data-structures.html). For now, just copy the code over to R/R-fiddle and press enter. Then you can type ‘tidy-data’, press enter and see the formatted table.

Okay. Finally back to ANOVA. To perform ANOVA on this data set is as simple as this expression.

	anova_fish <- aov(count ~ lake, data=tidy_fish)

This expression uses the aov function. (Analysis of Variance) The ‘count ~ lake’ provides a relation of interest to the function, saying we want to analyze the relation between the number of fish in each of the lake samples. Using our IQ example, we might have written something like ‘IQ ~ university’, depending on the names we put in our data frame. We have to be sure to tell the aov function that data=tidy_fish so it knows what we mean when we refer to count and lake. 

Keep in mind that this syntax is very powerful. If we wanted to look at the relation between count and any other variable, we could represent that. For a hypothetical example,

	anova_fish_day <- aov(count ~ time_of_day, data=tidy_fish)

This assumes that we have a column for the time of day the fish were caught, which we don’t so don’t try it. We could do the same thing for day_of_the_week if that were an existing column. In that case we would probably not expect to see any significant difference. Remember though! Fish must be randomly chosen from given a sample whether that be lakes, day_of_week, time_of_day, or any other label you are looking at. If it is not then you will probably get inaccurate results. 

To see the results of our ANOVA we can write:

	summary(anova_fish)

For me this displayed:

![ANOVA fish summary](img/anova_fish_summary.png)

We can see that our p-value is 0.00662 which is less than our 0.05 cut off, so we conclude that at least one of these samples does not come from the same distribution as the rest. 

We do not yet know which of these lakes have significant differences of fish to each other. We discussed earlier how we could not just use a lot of t-tests to deal with each comparison because it easily lead us to false conclusions. Now that we have performed an ANOVA though, there is a function that will take all of that into account. It is called the Tukey Test. If you would like to learn more about Tukey’s test visit [this page](https://en.wikipedia.org/wiki/Tukey%27s_range_test). It can be performed easily in R with this command.

	TukeyHSD(anova_fish)

This returns all of the significances between each lake, as shown here:

![Tukey summary](img/tukey_summary.png)

Wasn’t that easy? Once we tidied up our dataset, finding results was remarkably straight forward. Here we see that only the Rice_Lake-Long_Lake combination are not significantly different.

##Conclusion

This was a very basic example, but we can extend this process to many other datasets very easily to ask interesting questions. R comes with a dataset called iris which observes different features of individual flowers. We can see the summary of this by typing:

	summary(iris)

![iris summary](img/iris_summary.png)

This dataset is similar to the lake dataset, only now we are looking at four features from samples instead of just one. We are sampling from the setosa, verisicolor, and virginica species of iris and want to see there is a significant difference between any particular features across these species. We can do just as we did before:

	sepal_length_anova <- aov(Sepal.Length ~ Species, data=iris)

![sepal ANOVA](img/sepal_anova.png)

Wow that p-value is really low. Looks significant to me. Let’s try a Tukey test on it:

![sepal Tukey](img/sepal_tukey.png)

And we find that each species pair is extremely significant. We can run the same test for any other feature. Try it yourself by running an ANOVA on Sepal.Width, Petal.Length, or Petal.Width and following it up with a Tukey test!

##Postlude

I would like to take a moment to try to explain two of the difficult looking expressions I wrote to create and manipulate the lake data that was entered prior to our ANOVA. The first like looked like this:

	fish <- data.frame( Rice_Lake = c(68,66,110,82,90,88,140,151,123,122), Long_Lake = c(150,153,102,97,95,170,80,76,102,104), Island_Lake = c(160,130,142,133,130,144,170,151,135,140) )

Let’s break this down a little bit. ‘data.frame’ is a function that takes in arguments. We provide it arguments by passing them into two parentheses following the function name. Informally this would be something like this. ‘data.frame(arguments go here)’ A data frame is an R ‘object’ which stores information about the data of interest. Think of this like a table you would make in Excel. What the data.frame function wants to know is the names of the columns and the list of data that goes in these columns. If we were just to type

	data.frame( Rice_Lake = c(68,66,110,82,90,88,140,151,123,122) )

this would create a data frame with just one column named ‘Rice_Lake’ with values 68, 66, and so on. The c function which wraps these numbers stands for ‘concatenate’ and merely tells R that this list of numbers goes together. By adding more column names and ‘c’ lists, we can populate all of the columns we care to have for our data frame along with their column names:

	data.frame( Rice_Lake = c(68,66,110,82,90,88,140,151,123,122), Long_Lake = c(150,153,102,97,95,170,80,76,102,104), Island_Lake = c(160,130,142,133,130,144,170,151,135,140) )

By placing ‘fish <- ‘ in front of this expression we are just telling R to take the data frame we created and label it as ‘fish’ so we can reference it later.

The second difficult expression we saw was:

	tidy_fish <- data.frame(count = c(fish[['Rice_Lake']], fish[['Long_Lake']], fish[['Island_Lake']]), lake = c( rep('Rice_Lake', 10), rep('Long_Lake', 10), rep('Island_Lake', 10) ))

Let’s break this down iteratively so we can see what is happening. The first thing I want is for our tidy data frame to just have two columns named ‘count’ and ‘lake’ so we can create our relation between ‘count’ and ‘lake’ within our ANOVA function. The setup would look something like this:

	data.frame( count = c(…), lake = c(…) )

We don’t yet know what goes within the c functions, but we can reason this out. For the count column we just want to stack the data for every lake on top of each other. We can do this by using bracket notation with the fish data frame we already created, turning our function into:

	data.frame( count = c( fish[[‘Rice_Lake’]], fish[[‘Long_Lake’]], fish[[‘Island_Lake’]] ), lake = c(…) )

The bracket notation is weird I know, but you probably have an intuitive sense for how it is grabbing the data we need to scrunch together. The double brackets are necessary because the take the data and, to be very hand wavy, puts it in a more scrunchable form. If we used single brackets it would not work because the numbers would come with a bunch of other data we do not want.

Finally we need to add the information to our ‘lake’ column. This is pretty intuitive. All we need to do is create a column of ten ‘Rice_Lake’ values followed by ten ‘Long_Lake’ values followed by ten ‘Island_Lake’ values. R comes with a handy rep function that allows us to do just that.

	data.frame( count = c( fish[[‘Rice_Lake’]], fish[[‘Long_Lake’]], fish[[‘Island_Lake’]] ), lake = c( rep(‘Rice_Lake’, 10), rep(‘Long_Lake’, 10), rep(‘Island_Lake’)  )

As you probably guessed, rep(‘Rice_Lake’, 10) repeats ‘Rice_Lake’ for us ten times.

If this is a lot to take in all in one sitting, you are right! Don’t worry though. Practice makes perfect and there are plenty of articles where people do things in R that are even more interesting than what we have done in this lesson. For this try [R-Bloggers](http://www.r-bloggers.com/). 