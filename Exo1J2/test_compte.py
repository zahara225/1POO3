try:
        compte1.titulaire = ""
    except Exception as e:
        print(e)

    try:
        compte1.deposer(True)
    except Exception as e:
        print(e)