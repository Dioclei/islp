Answers were cross-checked with https://botlnec.github.io/islp/sols/chapter3/exercise1/

1. Null hypotheses to p-values, and conclusions in terms of `sales`, `TV`, `radio`, and `newspaper`
	- Because there are 4 coefficients, there are 4 null hypotheses.
	1. $H_0$ for `TV`: In the **presence** of `radio` and `newspaper` (and the intercept), there is no relationship between `tv` and `sales`
	2. $H_0$ for `radio`: In the **presence** of `TV` and `newspaper` (and the intercept), there is no relationship between `radio` and `sales`
	3. $H_0$ for `newspaper`: In the **presence** of `TV` and `radio` (and the intercept), there is no relationship between `newspaper` and `sales`
	4. $H_0$ for the intercept: In the **absence** of `TV`, `radio`, and `newspaper`, `sales` are zero.
	- Based on the p-values, we can reject the null hypothesis for `TV`, `radio`, and the intercept, but not for `newspaper`.
	- We conclude that there is a relationship between `TV` and `sales`, between `radio` and `sales`, and in the absence of `TV`, `radio`, `newspaper`, `sales` are non-zero.
	- We also conclude that there is no relationship between `newspaper` and `sales` in the presence of `TV` and `radio`.
	- Note: at 5% p-value, there is 19% chance of having one appear as significant out of 3 variables, even if there was no relationship for all of them.
2. Difference between KNN classifier and KNN regressor
	1. The methodology is similar but the conclusion is different.
	2. For the KNN classifier, for some test observation, we find the K nearest observations and assign the mode class of these observations to the test observation.
	3. For the KNN regressor, for some test observation, we find the K nearest observations, average their individual corresponding response values, and assign that average to the test observation.
3. Analysis on dataset:
	- $\hat{\beta}_0=50$
	- $X_1=GPA, \hat{\beta}_1=20$
	- $X_2=IQ, \hat{\beta}_2=0.07$
	- $X_3=Level, \hat{\beta}_3=35$
	- $X_4=Interaction~between~GPA~and~IQ, \hat{\beta}_4=0.01$
	- $X_5=Interaction~between~GPA~and~Level, \hat{\beta}_5=-10$
	- Response: starting salary after graduation (in thousands of dollars)
	1. (a)(i) / (a)(ii) / (a)(iii) / (a)(iv): False / False / True / False. For fixed values of GPA and IQ, the difference is given by $Y_{college} - Y_{hs} = \hat{\beta}_3 + \hat{\beta}_5 * GPA = 35 - 10 * GPA$. If GPA > 3.5, High school grads have on average a higher expected salary than College grads so answer is (a)(iii).
	2. (b) Salary of a college graduate with IQ of 110 and GPA of 4.0 is $50 + 20 * 4.0 + 0.07 * 110 + 1 * 35 + 0.01 * (110 * 4.0) + -10 * (4.0 * 1) = 137.1$
	3. (c) False, the value of the coefficient is not enough to justify that there is no interaction, we need to look at the p-value of the t-statistic of the interaction variable for the null hypothesis that there is no relationship ($H_0: \beta_4=0$). While the coefficient for interaction between GPA and IQ is small, it is reasonable because IQ is a large number (whereas something like GPA is a small number, so the coefficient looks larger).
4. Cubic regression vs Linear regression
	1. Underlying relationship is linear
		1. (a) Training RSS for the cubic regression should be **smaller** than for the linear regression, because the cubic regression will fit better to the noise of the dataset.
		2. (b) Test RSS for the linear regression should be **smaller** than for the cubic regression, because the linear regression model will ~~be closer to the underlying linear relationship~~ have **less bias** (due to the underlying relationship being linear) and be able to predict on new observations more accurately.
	2. Underlying relationship is non-linear, but the deviation from linearity is unknown
		1. (c) Training RSS for cubic regression is **smaller**, simply because it can fit better to the dataset.
		2. (d) ~~Test RSS for cubic regression is also **smaller**, because it is better able to model the underlying relationship than a linear model. This allows it to make a better prediction on new observations.~~
		   Not enough information. We don't know how far from linear the true relationship is, so we don't know how much bias the two models will have. If the true relationship is only a little non-linear, then the linear model may have a lower bias.
5. Consider a linear regression without the intercept, such that $\hat{y}_i=x_i\hat{\beta}$, where $\hat{\beta} = \left( \sum^n_{i=1}x_iy_i \right) / \left( \sum^n_{i=1}x_i^2 \right)$
	- I didn't know how to do this at first. But I was on the right track of substituting the equations in. I think I just didn't manage to see the similarity of the expressions and cleanly separate the summations.
$$
\begin{aligned}
\hat{y}_i &= x_i\hat{\beta} \\
&= x_i * \left( \sum^n_{i'=1}x_{i'}y_{i'} \right) / \left( \sum^n_{j=1}x_j^2 \right) \\
&= \sum^n_{i'=1} \left( \frac{x_ix_{i'}y_{i'}}{\sum^n_{j=1}x_j^2} \right) \\
&= \sum^n_{i'=1} \left( \frac{x_ix_{i'}}{\sum^n_{j=1}x_j^2} \right) y_{i'} \\
&= \sum^n_{i'=1} a_{i'} y_{i'} \\
a_{i'} &= \frac{x_ix_{i'}}{\sum^n_{j=1}x_j^2}
\end{aligned}
$$

6. Using the equations for $\hat{\beta}_0$ and $\hat{\beta}_1$, Argue that in the case of simple linear regression, the least squares line always passes through the point $(\bar{x}, \bar{y})$
$$
\begin{gathered}
\hat{\beta}_1 = \frac{\sum^n_{i=1}(x_i-\bar{x})(y_i-\bar{y})}{\sum^n_{i=1}(x_i-\bar{x})^2} \\
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}
\end{gathered}
$$
	- Substitute the definition of $\hat{\beta}_0$ and $x=\bar{x}$ into $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1x$, we get:
$$
\hat{y} = \bar{y} - \hat{\beta}_1\bar{x} + \hat{\beta}_1\bar{x}=\bar{y}
$$
	- Hence, when $x=\bar{x}$, $y = \bar{y}$.
