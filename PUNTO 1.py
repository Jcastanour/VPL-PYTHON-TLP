#PUNTO 1

letras = ['P', 'Q', 'R', 'W', 'X', 'Y', 'Z']
digitos = ['9', '8', '7', '6', '5']
especiales = ['_', '#', '&', '%']

codigos_posibles = ["REF-{}{}{}{}{}{}".format(D1, D2, L1, L2, L3, E) for D1 in digitos
                                                            for D2 in digitos
                                                            for L1 in letras
                                                            for L2 in letras
                                                            for L3 in letras
                                                            for E in especiales]


tamaño_lista = len(codigos_posibles) #34300


#PUNTO 2
