#           Notes
# Ñ

Ñ = None
ñ = None

while True:
    if Ñ:
        for i in range(0,9999999999999):
            print('ñ :)')
    else:
        ñ = str(input('ñ: '))
        if ñ == 'ñ' or ñ in 'ñ':
            for i in range(0,9999999999999):
                print('ñ', end=' ')
        elif ñ == 'no' or ñ in 'no':
            for i in range(0,10):
                print("it's Ñ")
        else:
            ñ2 = str(input('Ñ >:('))
            if ñ2 == 'ñ' or ñ2 in 'ñ':
                Ñ = True
            else:
                for i in range(0,9999999999999):
                    print('say Ñ >:(')
