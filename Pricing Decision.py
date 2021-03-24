class Product:
    selling_price = 0
    profit = 0
    def __init__(self, name, supplier,price, sales, category):
        self.name = name
        self.supplier = supplier
        self.cost_price = price
        self.sales = sales #monthly sales
        self.category = category
        self.list_price = 2*price
        
    def cal_profit(self):
        return (self.selling_price-1.1*self.cost_price)/self.cost_price*100

        
category_age = {} #stores age of each product category in months
supplier_age = {} #stores age of supplier in months

def pricing_decision(product):
    if product.supplier not in supplier_age: #first time supplier
        supplier_age[product.supplier] = 0
        product.selling_price = 1.1 * product.cost_price
        product.profit = 0
    
    elif supplier_age[product.supplier] <= 2: #first 2 month for new supplier
        product.selling_price = 1.1 * product.cost_price
        product.profit = 0
    
    elif product.category not in category_age:   #new product category
        category_age[product.category] = 0
        product.selling_price = 1.1 * product.cost_price
        product.profit = 0
    
    elif category_age[product.category] <= 1:  #1 month benefit for new product
        product.selling_price = 1.1 * product.cost_price
        product.profit = 0
    
    else:
        if product.sales > 500:
            product.selling_price = product.list_price
            product.profit = product.cal_profit()
        elif product.sales >= 200:
            product.salling_price = 0.85 * product.list_price
            product.profit = product.cal_profit()
        else:
            product.selling_price = 0.65 * product.list_price
            product.sales = int(input())
            if(product.sales < 200):
                print("Drop Product")
                product.selling_price = 0
                product.profit = product.cal_profit()
            else:
                product.profit = product.cal_profit()
                
    
    return product.profit


        
