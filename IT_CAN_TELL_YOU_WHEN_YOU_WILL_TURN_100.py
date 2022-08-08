print("\n\t\t <---LET's CHECK WHEN YOU WILL TURN 100--->")

try:
    a = input("\nENTER YOUR AGE or YEAR OF BIRTH : ")

    assert float(a)>0 ,""

    if float(a)<100:
        print("You will turn 100 after ", 100- float(a),"years from this year")

    elif float(a)>1990:
        print("you will turn 100 in ",100+float(a),"year")
    else:
        print("Invalid year")

except Exception:
    print("Invalid year")