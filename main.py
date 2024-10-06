#Assignment 2, Kai Agoto. 
#code calculates pension income

#collecting inputs for calculations
current_age = int(input("enter current age in years:"))

current_yrs_serv = int(input("enter current years of service:")) 

LE_salary_1 = int(input("enter largest expected annual income:"))
LE_salary_1 = int(LE_salary_1)

LE_salary_2 = input("enter second-largest expected annual income:")
LE_salary_2 = int(LE_salary_2)

LE_salary_3 = input("enter thrid-largest expected annual income:")
LE_salary_3 = int(LE_salary_3)

p_rate = 0.014

#calculations
avg_salary = (LE_salary_1 + LE_salary_2 + LE_salary_3)/3 #calculates avg salary

Ttl_yrs_at_55 = ((55 - current_age) + current_yrs_serv) 
Ttl_yrs_at_60 = ((60 - current_age) + current_yrs_serv)
Ttl_yrs_at_65 = ((65 - current_age) + current_yrs_serv)

pension_at_55 = (avg_salary * p_rate * Ttl_yrs_at_55) 
pension_at_60 = (avg_salary * p_rate * Ttl_yrs_at_60)
pension_at_65 = (avg_salary * p_rate * Ttl_yrs_at_65)

#print formating
result_55y = f'${pension_at_55:0.2f}'
result_60y = f'${pension_at_60:0.2f}'
result_65y = f'${pension_at_65:0.2f}'

print(f"\n{'retirement age':<21}{'retirement income':21}")
print(f"{'55':<21}{result_55y:21}")
print(f"{'60':<21}{result_60y:21}")
print(f"{'65':<21}{result_65y:21}")