#Assignment 2, Kai Agoto. 
#calculates pension income

#collecting inputs for calculations
current_age = input("Enter Current age: ")
current_age = int(current_age) #must convert to str to int

current_yrs_serv = input("Enter Current years of service: ")
current_yrs_serv = int(current_yrs_serv) 

LE_salary_1 = input("Enter largest expected salary 1: ")
LE_salary_1 = int(LE_salary_1)

LE_salary_2 = input("Enter largest expected salary 2: ")
LE_salary_2 = int(LE_salary_2)

LE_salary_3 = input("Enter largest expected salary 3: ")
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

#print calculations, rounds results to dollar amt 

print("Pension at 55 years:$", f'{pension_at_55 : 0.2f}')
print("Pension at 60 years:$", f'{pension_at_60 : 0.2f}')
print("Pension at 65 years:$", f'{pension_at_65 : 0.2f}')
