# ML Verbs

Generic interfaces for machine learning models.

This is a work-in-progress experimental project of [@nowanilfideme](https://nowan.dev)

## Motivation

Things I've disliked about various ML libraries:

- Specific data (dataframe) types for inputs and outputs.
- Operations that mutate in place.
- Assumptions on the interface, columns, etc. that are too specific.
- No way to consistently get parameters.
- Difficult to serialize long-term (`pickle` doesn't count!)
- Limited number of available operations.
- Difficult to use with static checks.

I've also gotten quite envious of Julia, where they have a wonderful generic data interface called
[`Tables.jl`](https://tables.juliadata.org/stable/) that their whole stats and ML community has embraced.
Many of the libraries still are quite "hacky", as seems to be the Julia ethos, but all the tools/params
being available to the user (because implementation and usage is in the same language) is great.
Sadly, I can't use or even test Julia at my day job (nobody knows Julia, so nobody to support).

## High-Level Design

This package is meant to define "verbs" that we use in Machine Learning. In this case, a "verb" is an
abstract `@runtime_checkable` `Protocol` interface.
