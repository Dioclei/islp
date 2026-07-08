8 July 2026
Answers are my own.
Some adjustments are made after checking against https://botlnec.github.io/islp/.

1. Performance of flexible statistical learning method vs inflexible statistical learning method
	1. $n$ is large, $p$ is small
		- flexible > inflexible - $n$ is large so the amount of noise is reduced. this allows the flexible model to fit well to the data
	2. $n$ is small, $p$ is large
		- flexible < inflexible - $n$ is small so there is a large amount of noise. with a large $p$, the flexible model will likely overfit, so its better to choose a less flexible model.
	3. relationship between predictors and response is highly non-linear
		- flexible > inflexible - more flexible model can fit non-linear relationships better, less flexible models are likely too biased no matter the sample size
	4. variance of error terms i.e. $\sigma^2 = Var(\epsilon)$ is extremely high
		- flexible < inflexible - more noise in data, so model should be less flexible so that it does not fit to the noise as easily, less overfitting
2. classification or regression, inference or prediction, $n$ and $p$
	1. $n = 500$, $p = 3$. Regression. Inference ("which factors affect …")
	2. $n=20$, $p=13$. Classification. Prediction ("success or failure")
	3. $n=52$, $p=3$. Regression ("% change …"). Prediction ("predicting …")
3. Sketch of squared bias, variance, training error, test error, and Bayes error against model flexibility
	1. Squared bias = squared deviation of predicted response vs actual response, should go down monotonically as model flexibility increases
	2. Variance = amount of variance should the model be trained on different training datasets. At 0 flexibility the model is independent of the data, so variance is 0. As model flexibility increases, it is more likely to have a larger variance of predictions when trained on different datasets (in other words the model fits to the noise), hence variance increases.
	3. training error = as flexibility increases, training error monotonically decreases because the model will eventually be able to learn all the relationships in the training data
	4. test error = U shaped because as flexibility increases, the model is able to better model the underlying $f$ and test error decreases. However, past a certain point, the model flexibility starts fitting to the noise of the training data more, and so test error will increase. This is overfitting. Test error = bias + variance + Bayes error, so it is lower bounded by the Bayes error.
	5. Bayes error = constant line because it represents irreducible error which is constant regardless of model flexibility.
4. Real life applications
	1. **Classification:**
		1. Predict whether it will be sunny, rainy, cloudy, etc. tomorrow
			1. Response: weather (sunny, rainy, cloudy)
			2. Predictors: surrounding area's weather, humidity, temperature, season
			3. I/P: prediction, because we want to predict tomorrow's weather
		2. Model mood for the day and the factors that go into it
			1. Response: Mood level (happy, sad, neutral)
			2. Predictors: Diet, stress/workload, amount of exercise, amount of sleep
			3. I/P: inference, because we want to better understand which factors affect mood (so that we can make good changes)
		3. Predict whether someone will have chronic diseases (diabetes, high blood pressure, high cholesterol, etc.)
			1. Response: Diabetes (yes/no), High blood pressure (yes/no), High cholesterol (yes/no)
			2. Predictors: sleep, diet, smoking, alcohol, work
			3. I/P: Prediction, but inference is good too to understand the factors that go into it and make lifestyle changes
	2. **Regression**
		1. Predict bus arrival time (# minutes from now)
			1. Response: # minutes from now till arrival
			2. Predictors: bus location, bus stop location, crowd levels, day of the week
			3. I/P: Prediction because we are only interested in the bus arrival time and not the factors
		2. Stock market returns
			1. Response: % increase in a stock
			2. Predictors: current price, volatility, liquidity
			3. I/P: Prediction because we are only interested in the returns and not how the factors affect it
		3. Find out what affects # people in a shopping mall
			1. Response: # people on a given day
			2. Predictors: weekday or weekend, time, discounts / events / promotions
			3. I/P: Inference because we want to find out the factors that affect it
	3. **Clustering**
		1. Cluster books, songs, movies, etc. based on their characteristics (e.g. genre, length, audience)
		2. Cluster customer preferences based on purchase history, purchased items, price of purchases
		3. Cluster people on linkedin to find similar/distinct groups of people
5. Advantages / Disadvantages of very flexible vs less flexible approach for regression or classification:
	1. Very flexible approaches are able to model nonlinear relationships
		1. i.e. Less bias, and given enough data, better performance
	2. Very flexible approaches are more prone to overfitting
	3. Very flexible approaches require a lot more data to capture complex nonlinear relationships
	4. Very flexible approaches are more computationally expensive, and are harder and longer to train.
	5. Very flexible approaches are less interpretable.
	6. Less flexible approaches are better when there is less data and less variables to model
	7. Additional notes from https://botlnec.github.io/islp/sols/chapter2/exercise5/:
		- More flexible?
			- large $n$ and small $p$
			- Non-linear relationship between predictors and response
		- Less flexible?
			- small $n$ and large $p$
			- High variance of error terms
6. Parametric means we simply need to estimate the parameters to a predefined function (that we assume the data follows). Non-parametric means we need to estimate the underlying function. Parametric methods are more interpretable but are usually less flexible than non-parametric methods.
7. K-Nearest Neighbours exercise
	1. Euclidean distance between each observation and test point:
		1. $3$
		2. $2$
		3. $\sqrt{10}$
		4. $\sqrt{5}$
		5. $\sqrt{2}$
		6. $\sqrt{3}$
	2. Prediction with $K=1$: Nearest neighbour is #5 with $\sqrt{2}$ distance, hence we take the class of #5 which is **Green**
	3. Prediction with $K=3$: Nearest 3 neighbours are #5, #6, #2, hence we take the mode which is **Red** (both #6 and #2 are Red)
	4. If Bayes decision boundary is highly non-linear, then,
		1. Visually, the boundary will look very wiggly and this can only come from a KNN with a small $K$. Hence we should choose a small $K$.
		2. If a large $K$ is used, the decision boundary will be smoother because of less emphasis on individual points. Non-linear boundaries will likely have a lot of small local differences that cannot be captured by taking the majority of a large number of neighbours. Hence we should choose $K$ to be small.
