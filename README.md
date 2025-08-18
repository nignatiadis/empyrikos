# Empyrikos Python Package

Python interface to [Empirikos.jl](https://github.com/nignatiadis/Empirikos.jl) for empirical Bayes methods.

## Installation

```bash
pip install git+https://github.com/nignatiadis/empyrikos.git
```

## Requirements

- Python 3.10+
- Julia 1.10+ (will be automatically installed via PyJulia if not present)

## Quick Start

```python
import empyrikos as eb
import numpy as np

# Example: Empirical partially Bayes t-test
# Generate test data consistent with model assumptions
np.random.seed(42)
n_tests = 100
df = np.full(n_tests, 10)  # degrees of freedom

# True effect sizes: mix of nulls and non-nulls  
true_beta = np.zeros(n_tests)
true_beta[50:] = np.random.normal(0, 1, 50)  # 50 nulls, 50 non-nulls
# True variances from inverse gamma (conjugate prior)
true_sigma_sq = 1.0 / np.random.gamma(2, 1/0.5, n_tests)

# Generate observed data according to model
beta_hat = np.random.normal(true_beta, np.sqrt(true_sigma_sq))
se_hat_squared = true_sigma_sq * np.random.chisquare(df) / df

# Run empirical partially Bayes t-test
result = eb.epb_ttest(
    beta_hat=beta_hat,
    se_hat_squared=se_hat_squared, 
    df=df,
    alpha=0.05
)

print(f"Number of rejections: {result.n_rejected}")
print(f"Adjusted p-values: {result.adj_pvalues[:5]}...")  # first 5
```

## Features

- **Empirical Partially Bayes t-test**: Advanced multiple testing with empirical Bayes shrinkage
- **Easy-to-use Python interface**: Pythonic API wrapping powerful Julia implementations
- **Automatic Julia integration**: Seamless Julia backend via PyJulia

## Documentation

For detailed documentation and examples, see [the documentation](docs/).

## License

MIT License - see LICENSE file for details.