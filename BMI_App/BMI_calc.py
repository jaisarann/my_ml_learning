from pywebio.input import *
from pywebio.output import *


def bmi_calc():
    height = input('Entter Height : ', type=FLOAT)
    weight = input('Enter Weight : ', type=FLOAT)
    
    actual_bmi = weight / (height / 100) ** 2
    
    bmi_output = {16 : 'Severely Underweight', 
                  18.5 : 'Underweight', 
                  25 : 'Normal', 
                  30 : 'Over weight',
                  35 : 'Moderately Obese',
                  float('inf') : 'Severely Obese'}  
    
    for bmi_std, bmi_type in bmi_output.items():
        # print('weight : ' , weight)
        if actual_bmi < bmi_std:
            put_text(f'Your height {height}, weidht {weight} and your BMI is : {bmi_type}')
            break
        
if __name__ == '__main__':
    bmi_calc()
    
      