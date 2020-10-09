#This code is used to calculate the new salary's for H1B level from old salary data

#import libraries
import numpy as np
from scipy import optimize 
from scipy.stats import norm
import scipy.special as sp
import matplotlib.pyplot as plt
from gaussianSalaryCalculator import salaryCalculator

# Function is used in the optimizer to predict mean
# and std deviation of data from old salary data
# The code is designed for only 4 data points as 
# H1B data is given for 4 levels
def get_distribution_data(inputVar,salaryCalculatorVar):
    mean = inputVar[0]
    std_dev = inputVar[1]
    percentileValues = salaryCalculatorVar.get_old_percentile_values()
    percentileValues = percentileValues/100 
    unit_vector = np.ones(percentileValues.size) 
    salary_list = unit_vector*mean + np.multiply(std_dev*unit_vector,sp.erf(2*percentileValues-1))
    errorVector = salary_list - salaryCalculatorVar.get_old_salary_values()
    print(errorVector)
    return np.sum(np.abs(errorVector))

# Function used for calculating final salarys from 
# percentile values from mean and std dev values
def get_distribution_data_final(salCalc,inputVar):
    mean = inputVar[0]
    std_dev = inputVar[1]
    percentileValues = salCalc.get_new_percentile_values()
    percentileValues = percentileValues/100 
    unit_vector = np.ones(percentileValues.size) 
    salary_list = unit_vector*mean + np.multiply(std_dev*unit_vector,sp.erf(2*percentileValues-1))
    return salary_list

# Minimizer function for predicting mean and std-dev
# from old salary data
def optimizeAndReturnSalaryLevels(salCalc,old_salary_levels_var ,old_salary_percentile_levels_var,new_salary_percentile_levels_var):
    initialGuess = [120000, 30000]
    salCalc.set_old_salary_values(old_salary_levels_var)
    salCalc.set_old_percentile_values(old_salary_percentile_levels_var)
    salCalc.set_new_percentile_values(new_salary_percentile_levels_var)
    return optimize.minimize(get_distribution_data,initialGuess,args=salCalc)

#Loading old salary and percentile data
old_salary_levels = [95430, 120578, 145725, 170872]
old_salary_percentile_levels = [17,34,50,67]

#Loading new percentile data
new_salary_percentile_levels = [45,62,78,95]

#Creating object for storing/handling salary info
s1 = salaryCalculator ()
s1.set_old_salary_values(old_salary_levels)
s1.set_old_percentile_values(old_salary_percentile_levels)
s1.set_new_percentile_values(new_salary_percentile_levels)

#Running minimizer
optimizedVal = optimizeAndReturnSalaryLevels(s1, old_salary_levels,old_salary_percentile_levels,new_salary_percentile_levels)

#Processing predicted mean and salar
optimizedVector = []
optimizedVector.append(optimizedVal.x[0])
optimizedVector.append(optimizedVal.x[1])

#Calculating final salary list
finalSalaryList = get_distribution_data_final(s1,optimizedVector)

#Printing results
print(np.round(finalSalaryList,2))

