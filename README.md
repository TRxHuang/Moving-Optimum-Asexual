# Effective decoupling of mutations and the resulting loss of biodiversity caused by environmental change



## Introduction

This repository provides the code implementation for the research paper on the evolution of a large population of asexual organisms subject to selection and mutation on a quantitative trait. The model investigates two types of selection:
1. **Stabilising selection** - A unimodal selection where a single "optimal" trait value maximizes fitness.
2. **Bimodal selection** - A generalized stabilizing selection where there are two "optimal" trait values, resulting in a bimodal fitness function.

The study explores both static and dynamic environments, showing how the distribution of trait values changes over time under these selection pressures and mutation effects. Particularly, it addresses how rapid environmental changes can lead to a loss of diversity within the population.

**This repository also includes functionality for generating animations that visualize the evolutionary process over time.**



## Model
The evolution of the population distribution over generations is described as follows:

- The distribution of the population at each generation depends on integrating over all possible trait values, where the probability of a mutation is represented by a Gaussian (normal) distribution centered at zero with variance related to the mutation rate.
- The fitness function indicates how well each trait value supports survival and reproduction, with values ranging between 0 and 1. This fitness value varies based on the specific trait.



## Requirement
- **Python** version: >= 3.7



## Code Structure
- `Moving_Optimum_Asexual.py`: The main code for simulating the evolutionary dynamics of the asexual population under specified selection pressures and mutation rates.



## Usage
To run the model, ensure Python 3.7 or higher is installed. Then execute:

```bash
python Moving_Optimum_Asexual.py
```
