from main import *
from collections import Counter
import re

class Equation_Parser:
    def divide_equation(self, equation):
        self.reagents, self.products = equation.replace(" ", "").split("->")
        print(self.reagents)
        print(self.products)


    def divide_reagents(self, reagents):

        self.reagents_no_plus = reagents.replace(" ", "").split("+")
        
        print(self.reagents_no_plus)

    
    def divide_products(self, products):

        self.products_no_plus = products.replace(" ", "").split("+")

        print(self.products_no_plus)

    def count_elements(self, reagents_no_plus, products_no_plus):
        
        # =============== REAGENTS ===============
        total_reagents = Counter()

        for item in self.reagents_no_plus:
            # Split the coef of the formula
            # Ex: 2H2O 
            #     >> num_molecule = "2"
            #     >> formula = "H2O"
            match = re.match(r"(\d*)(.*)", item)

            if match:
                num_molecule, formula = match.groups()
                
                if num_molecule:
                    coefficient = int(num_molecule) # convert "2" to 2
                else:
                    coefficient = 1                 # if there is no number, means it's 1

                # Identify all elements and indices
                # Ex: H2O
                #     >> [('H', '2'), ('O', '')]
                elements = re.findall(r"([A-Z][a-z]?)(\d*)", formula)

                for element, num_element in elements:
                    if num_element:
                        quantity = int(num_element)
                    else:
                        quantity = 1

                    # Ex: 4H2O
                    #     >> Coef: 4
                    #     >> quantity: 2
                    total_reagents[element] += coefficient * quantity

        # =============== PRODUCTS ===============
        total_products = Counter()

        for item in self.products_no_plus:
 
            match = re.match(r"(\d*)(.*)", item)

            if match:
                num_molecule, formula = match.groups()
                
                if num_molecule:
                    coefficient = int(num_molecule) 
                else:
                    coefficient = 1           

                elements = re.findall(r"([A-Z][a-z]?)(\d*)", formula)

                for element, num_element in elements:
                    if num_element:
                        quantity = int(num_element)
                    else:
                        quantity = 1

                    total_products[element] += coefficient * quantity

        for element, total in total_reagents.items():
            print(f"{element}: {total}")

        for element, total in total_products.items():
            print(f"{element}: {total}")