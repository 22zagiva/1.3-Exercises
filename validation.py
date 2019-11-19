#!/usr/bin/env python3

def get_float():
    # initialize variables
    monthly_investment = 0
    yearly_interest_rate = 0

    # get input from the user
    while monthly_investment <= 0 or monthly_investment > 1000:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0 and monthly_investment <= 1000:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 1000") 
    
    while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 15")

    return monthly_investment, yearly_interest_rate

def get_int():
    # initialize variables    
    years = 0
    
    while years < 1 or years > 50:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 50")

    return years

def main():
    choice = "y"
    while choice.lower() == "y":
        

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()