# Currency Converter - By Youssef Khaled
print("=== EGP to USD Converter ===")
egp = float(input("Enter amount in EGP: "))
usd = egp / 48  # تقريبا سعر الدولار
print(egp, "EGP =", round(usd, 2), "USD")