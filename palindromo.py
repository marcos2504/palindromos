

def palindromo(palabra):
    
    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", ""):
        return True
    else:
        return False
   


