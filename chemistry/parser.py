from main import *

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

    def get_elements(self, reagents_no_plus, products_no_plus):

        reagents_quantities = []
        reagents_elements = []
        products_quantities = []
        products_elements = []
        for reagent in reagents_no_plus:
            for c in reagent:
                if c.isdigit():
                    reagents_quantities.append(c)
                elif c.isalpha():
                    reagents_elements.append(c)
            
            if reagent.isalpha():
                reagents_quantities.append("1")
        
        for product in products_no_plus:
            for c in product:
                if c.isdigit():
                    products_quantities.append(c)
                elif c.isalpha():
                    products_elements.append(c)
            
            if product.isalpha():
                products_quantities.append("1")

        for reagent_element, reagent_quantity in zip(reagents_elements, reagents_quantities):
            print(f"{reagent_element}: {reagent_quantity}")
        
        for product_element, product_quantity in zip(products_elements, products_quantities):
            print(f"{product_element}: {product_quantity}")