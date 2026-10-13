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

        # self.reagents_quantities = []
        # self.reagents_elements = []
        # self.products_quantities = []
        # self.products_elements = []
        # for reagent in reagents_no_plus:
        #     for c in reagent:
        #         if c.isdigit():
        #             c = int(c)
        #             self.reagents_quantities.append(c)
        #         elif c.isalpha():
        #             self.reagents_elements.append(c)
            
        #     if reagent.isalpha():
        #         self.reagents_quantities.append(1)
        
        # for product in products_no_plus:
        #     for c in product:
        #         if c.isdigit():
        #             c = int(c)
        #             self.products_quantities.append(c)
        #         elif c.isalpha():
        #             self.products_elements.append(c)
            
        #     if product.isalpha():
        #         self.products_quantities.append(1)

        # for reagent_element, reagent_quantity in zip(self.reagents_elements, self.reagents_quantities):
        #     print(f"{reagent_element}: {reagent_quantity}")
        
        # for product_element, product_quantity in zip(self.products_elements, self.products_quantities):
        #     print(f"{product_element}: {product_quantity}")
        total_reagents = Counter()

        for item in self.reagents_no_plus:
            match = re.match(r"(\d*)([A-Za-z]+)", item)

            if match:
                num_element, element = match.groups()

                if num_element:
                    quantity = int(num_element)
                else:
                    quantity = 1

                total_reagents[element] += quantity

        for element, total in total_reagents.items():
            print(f"{element}: {total}")

        
        total_products = Counter()

        for item in self.products_no_plus:
            match = re.match(r"(\d*)([A-Za-z]+)", item)

            if match:
                num_element, element = match.groups()

                if num_element:
                    quantity = int(num_element)
                else:
                    quantity = 1

                total_products[element] += quantity

        for element, total in total_products.items():
            print(f"{element}: {total}")