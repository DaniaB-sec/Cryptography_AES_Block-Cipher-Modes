import modulo_para_AES as AES
import os
from base64 import b64encode

'''
EXERCICIO: 

Faça as chamadas para criptografar e descriptografar com AES em cada um dos 4 modos: ECB, CBC, CTR e GCM 
O modo ECB foi fornecido como exemplo. Inclua o teste para os outros 3 modos CBC, CTR e GCM 
plaintext = 'TESTE DA EQUIPE X' ou 'TESTE DO ESTUDANTE XX' 

Repare que cada modo exige informações diferentes do receptor para poder decifrar:
- ECB: só a chave
- CBC e CTR: chave + iv
- GCM: chave + iv + tag

Você deve incluir apenas os parâmetros usados em cada chamada AES.decifra_AES.

PARA ENTREGAR A ATIVIDADE COPIE O RESULTADO DO PRINT NO FINAL DO ARQUIVO

'''

msg = 'GRUPO 7. DANIELLE B., GABRIEL B., MATEUS P.'
plaintext = msg.encode('UTF-8')

# Completa o bloco do AES se necessário (128 bits = 16 bytes)
if len(plaintext) % 16 != 0:
    plaintext = plaintext + bytearray(16 - len(plaintext) % 16)

chave = os.urandom(16)


# Copie e modifique esta seção para os 3 modos restantes
# Preencha decifra_AES só com o que o modo realmente precisa (iv, tag)
#-----------------------------------------------------
modo = 'ECB'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    # ECB não usa iv nem tag
    texto_decifrado = AES.decifra_AES(ciphertext, chave, modo)
    print('Plaintext:', texto_decifrado.decode())

    assert texto_decifrado == plaintext, 'ERRO: texto decifrado é diferente do original!'
    print('OK: texto decifrado confere com o original')

except Exception as e:
    print(e)

#-----------------------------------------------------

modo = 'CBC'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    # ECB não usa iv nem tag
    texto_decifrado = AES.decifra_AES(ciphertext, chave, modo, iv)
    print('Plaintext:', texto_decifrado.decode())

    assert texto_decifrado == plaintext, 'ERRO: texto decifrado é diferente do original!'
    print('OK: texto decifrado confere com o original')

except Exception as e:
    print(e)



modo = 'CTR'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    # ECB não usa iv nem tag
    texto_decifrado = AES.decifra_AES(ciphertext, chave, modo, iv)
    print('Plaintext:', texto_decifrado.decode())

    assert texto_decifrado == plaintext, 'ERRO: texto decifrado é diferente do original!'
    print('OK: texto decifrado confere com o original')

except Exception as e:
    print(e)


modo = 'GCM'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )

try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    # ECB não usa iv nem tag
    texto_decifrado = AES.decifra_AES(ciphertext, chave, modo, iv, tag)
    print('Plaintext:', texto_decifrado.decode())

    assert texto_decifrado == plaintext, 'ERRO: texto decifrado é diferente do original!'
    print('OK: texto decifrado confere com o original')

except Exception as e:
    print(e)


'''
TESTE DO MODO ECB
chave: [15, 8, 76, 220, 213, 230, 64, 116, 235, 254, 210, 96, 57, 80, 90, 91]
O modo ECB critografa cada bloco separadamente
Ciphertext (B64): b'y9DetTXWdrOMz+QmeYKUjxpO1mJYXQaI1LFBS0BpXf047ud4Kqr8nAKlZm97cCf3'
Plaintext: GRUPO 7. DANIELLE B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original

TESTE DO MODO CBC
chave: [15, 8, 76, 220, 213, 230, 64, 116, 235, 254, 210, 96, 57, 80, 90, 91]
O modo CBC faz um XOR de cada bloco com o anterior e cria um problema de paralelismo
iv: [224, 110, 229, 105, 231, 118, 70, 70, 127, 14, 236, 74, 149, 220, 3, 254]
Ciphertext (B64): b'DDTNI/30duk0uVeBOdmTY32jytsl/vI3s07JrcH8Xaoil8f7hzyotCAMhKoNVIjo'
Plaintext: GRUPO 7. DANIELLE B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original

TESTE DO MODO CTR
chave: [15, 8, 76, 220, 213, 230, 64, 116, 235, 254, 210, 96, 57, 80, 90, 91]
O modo CTR usa o AES para gerar um keystream para um XOR cipher
iv: [218, 49, 31, 12, 136, 234, 216, 248, 23, 206, 57, 118, 237, 186, 131, 157]
Ciphertext (B64): b'Ug1FHo7vGW7VFYd2sz2eNA8ZzJwXxMIdIpJLo59H1cUNoallKSoSFF2ggBmdl7mu'
Plaintext: GRUPO 7. DANIELLE B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original

TESTE DO MODO GCM
chave: [15, 8, 76, 220, 213, 230, 64, 116, 235, 254, 210, 96, 57, 80, 90, 91]
O modo GCM é similar ao CTC mais adiciona um tag de autenticacao
iv: [248, 100, 61, 174, 49, 68, 159, 164, 227, 252, 192, 152, 79, 183, 191, 51]
tag: [218, 76, 176, 222, 142, 46, 61, 17, 155, 102, 128, 65, 168, 223, 122, 134]
Ciphertext (B64): b'VyKUqXpLd1xLbFDFMjEqr5otbasfa1D1pTRCKFltB+Vy5iNvW4KWY7cQ65ovRT7x'
Plaintext: GRUPO 7. DANIELLE B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original
'''