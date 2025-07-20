# Amazon_Vine_Analysis

## Overview

This project had two parts. First I extracted a dataset of Amazon book reviews from S3 storage, transformed it to match a schema, and loaded it into a PostgreSQL database. Second, I investigated the difference in five-star reviews between vine and non-vine reviews

## Results

The book review data were successfully extracted, transformed, and loaded into a relational database. The results of the vine vs. non-vine investigation are presented here:

Vine reviews: 
- total: 0
- five star: 0
- percentage five star: 0

Non-vine reviews: 
- total: 378638
- five star: 227734
- percentage five star: 60% 

## Summary
Apparently there were no Vine reviews in this dataset at all, so this analysis was not useful and we cannot say if there is any bias for reviews in the Vine program. 
