# Pointwise mutual information

It is a measure of how often two events $x$ and $y$ occur, compared with what we would expect if they were independent:

$$
I(x, y) = \log_2\frac{P(x, y)}{P(x)P(y)}
$$

The pointwise mutual information between a target word $w$ and a context word $c$ is then defined as:

$$
\text{PMI}(w, c) = \log_2\frac{P(w, c)}{P(w)P(c)}
$$
The numerator tells us how often we observed the two words together (assuming we compute probability by using the MLE). The denominator tells us how often we would **expect** the two words to co-occur assuming they each occurred independently. Thus, the ratio gives us an estimate of how much more the two words co-occur than we expect by chance.

It's more useful to consider the positive values only since we would require an enormous corpus to determine whether two words co-occur *less* frequently than random. So we can modify the above definition to *positive point mutual information* where we truncate at zero.

$$
\text{PPMI}(w, c) = \max(\log_2\frac{P(w,c)}{P(w)P(c)}, 0)
$$
More formally, let's assume we have a co-occurrence matrix $F$ with $W$ rows (words) and $C$ columns (contexts), where $f_{ij}$ gives the number of times word $w_i$ occurs in context $c_j$. This can be turned into a PPMI matrix where $ppmi_{ij}$ gives the PPMI value of word $w_i$ with context $c_j$ as follows:

$$
p_{ij} = \frac{f_{ij}}{\sum_{i=1}^W\sum_{j=1}^Cf_{ij}}p_{i*} = \frac{\sum_{j=1}^C f_{ij}}{\sum_{i=1}^W\sum_{j=1}^C f_{ij}}p_{*j} = \frac{\sum_{i=1}^W f_ij}{\sum_{i=1}^W\sum_{j=1}^Cf_{ij}}
$$

$$
\text{PPMI}_{ij} = \max(\log_2\frac{p_{ij}}{p_{i*}p_{j*}}, 0)
$$

PMI has the problem of being biased toward infrequent events; very rare words tend to have very high PMI values. One way to reduce this bias toward low frequency events is to slightly change the computation for $P(c)$, using a different function $P_\alpha(c)$ that raises the probability of the context word to the power of $\alpha$:

$$
\text{PPMI}_\alpha(w, c) = \max(\log_2\frac{P(w, c)}{P(w)P_\alpha(c)}, 0),
$$
Where
$$
P_\alpha = \frac{\text{count}(c)^\alpha}{\sum_c\text{count}(c)^\alpha}
$$
Setting of $\alpha = 0.75$ improved performance of embeddings on a wide range of tasks. This works because raising the count to $\alpha=0.75$ increases the probability assigned to rare contexts.

Another possible solution is Laplace smoothing: Before computing PMI, a small constant $k$ (values of 0.1-3 are common) is added to each of the counts, shrinking (discounting) all the non-zero values. The larger the $k$, the more the non-zero counts are discounted.
