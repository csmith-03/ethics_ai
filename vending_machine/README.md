# vending_machine.smv
* This file aims to create a vending machine using NUSMV. Below are some assumptions made when creating it:
  * Assumptions:
    1.	Vending machine only accepts 5, 10, and 25 cents
    2.	There are 3 products, each listed with a specific price
    3.	The vending machine dispenses change of 5 and 10 cents.
  * Addionally, here are some Computation Tree Logic (CTL) queries made from this model:
    1.	AG(!change_dispensed) -> AF(product_dispensed)
      * This query states that for all states in the model, if change is not dispensed, then a product will be dispensed. 
        
    2.	EF(product_dispensed) -> AG(product_dispensed -> EF(change_dispensed))
      * This query states that if a product is eventually dispensed, then for all products dispensed, correct change will dispense too. 
        
    3.	AG(selected_product = 1 -> AX(inserted_currency >= product_price[1]))
      * This query states that if product 1 is selected, the user will always insert currency that matches that of the price. 
        
    4.	AG(!change_dispensed -> AX(!product_dispensed))
      * Within this query, if change is not ready to be dispensed, then in the next state, no product should be dispensed either. 
        
    5.	AG(inserted currency = 5 | inserted_currency = 10 | inserted_currency = 25)
      * This query states that for all currency, the only accepted currencies to insert are 5, 10, and 25 cents. 

