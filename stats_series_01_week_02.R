# Snippet 1
# Discrete data
pets <- sample(0:4, 10, replace = TRUE)

# Continuous data
weights <- rnorm(10, mean=70, sd=10)

# Snippet 2
# Ordinal data
sizes <- factor(c("Small", "Medium", "Large", "Large", "Small", "Medium"),
                levels = c("Small", "Medium", "Large"), ordered = TRUE)

# Nominal data
colors <- factor(c("Red", "Blue", "Green", "Blue", "Red", "Green"))

# Snippet 3
# Binary data
success <- sample(c(0, 1), size = 100, replace = TRUE, prob = c(0.5, 0.5))

# Snippet 4
# Time series data
library(xts)
dates <- seq(as.Date("2020/1/1"), by = "day", length.out = 100)
values <- rnorm(100)
time_series <- xts(values, order.by = dates)
