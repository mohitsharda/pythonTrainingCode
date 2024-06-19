"""
I have HDFC BANK CREDIT CARD 
hdfc bank will charge 15% interest on oustanding amount 
minimum, you should be able to pay 10% of oustanding amount else your credit score will be compromised

april 2024 -> 50,000 ---->> input by user 
    april 2024 min -> 5000
            pending  -> 45000
                     + 15% of 45000 = 6750
i can only pay maxx of 8000 permonth ---> input by user

find in which month  whole amount will become 0
"""

def month(num, current):
    monthName = {
    1: "january", 2: "february", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December",
    }

    newMonth = (current + num - 1)% 12
    if newMonth == 0:
        newMonth = 12
    return monthName[newMonth]


Amount = int(input("HOW MUCH AMOUNT YOU WANT FROM BANK: "))
print("YOU CAN TAKE LOAN.. ")
print("-------------------------------------------------")
print("YOU HAVE TO PAY 10% OF UR OUTSTANDING (FIRST INSTALLMENT).. ")
firstInstallment = 0.10 * Amount
print("FIRST INSTALLMENT..", firstInstallment)
print("-------------------------------------------------")

print("BANK WILL CHARGE 15% ON OUTSTANDING EVERY MONTH..")
remainingAmount = (0.15 * (Amount - firstInstallment)) + (Amount - firstInstallment)
print("After first installment..", remainingAmount)
print("-------------------------------------------------")

remainingInstallments = int(input("ENTER AMOUNT YOU PAY AS REMAINING INSTALLMENTS.."))

monthNum = int(input("ENTER NUMBER OF MONTH IN WHICH U TAKE LOAN.. "))


i = 1
while remainingAmount != 0:
    if remainingAmount > remainingInstallments:
        remainingAmount -= remainingInstallments
        print("Amount after ", i, "month", "and", "remaining amount.", remainingAmount)

    else:
        remainingInstallments = remainingAmount
        remainingAmount -= remainingInstallments
        print("Amount after ", i, "month", "and", "remaining amount.", remainingAmount)

    i +=  1

i -= 1
result = month(i, monthNum)
print("So, After :", i, "months your loan will be cleared/closed: in the month...", result )