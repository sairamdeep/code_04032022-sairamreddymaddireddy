# packaging-python-code
An overview for building custom python libraries.
## BMI Calculator  
This code takes in the input config file which contains weight,height of a person and health risk categories for given BMI range.
Outputs the count of persons in the specified health risk category
## Documentation
* Steps to install the package (in Linux)
  * Create virtual environment using venv (https://docs.python.org/3/library/venv.html)
    * ``` python3 -m venv venv ```
    * ``` source venv/bin/activate ```  
  * Install wheel package using pip
    * ``` pip install wheel ```
  * Install package from git using pip 
    * ```python -m pip install git+https://github.com/sairamdeep/packaging-python-code.git ```  
* Steps to run the package
  * Prepare the cfg.yaml
    * <img src="https://user-images.githubusercontent.com/22652457/156877123-d514fba4-bbe5-447c-83a7-2e58cef06360.png"  width="400" height="300"> 
    * data path should be w.r.t cfg file path
  * In the terminal activate the venv in which you installed bmipackage
  * After activation, run python cmd. It will python shell
    * ```(venv) user@system :python``` 
  * In the python shell, import BMICalculator
    * ``` >>> from bmicalculator.BMICalculator import BMICalculator ```  
  * Initiate BMI class by passing cfg file with path
    * ``` >>> bm=BMICalculator('cfg1.yaml')```
  * Now, use the initiated class object and get the counts of BMI categories
    * ``` >>> bm.getOverWeightCount ```
    * ```Total Overweighted people records:  0 ```
