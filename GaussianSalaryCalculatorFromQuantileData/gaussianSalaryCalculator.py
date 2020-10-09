import numpy as np
class salaryCalculator(object):
   
    """This class takes care of all the functions for calculating H1B salary
        The class assumes that the salary is normally distributed"""
    def __init__(self):
        self.old_salary_data = np.zeros(4)
        self.old_salary_percentile = np.zeros(4)
        self.new_salary_percentile = np.zeros(4)

    def set_old_salary_values(self,old_salary_var):
        self.old_salary_data = np.array(old_salary_var)
    def get_old_salary_values(self):
        return self.old_salary_data

    def set_old_percentile_values(self,old_percentile_var):
        self.old_salary_percentile = np.array(old_percentile_var)
    def get_old_percentile_values(self):
        return self.old_salary_percentile

    def set_new_percentile_values(self,new_percentile_var):
        self.new_salary_percentile = np.array(new_percentile_var)
    def get_new_percentile_values(self):
        return self.new_salary_percentile
