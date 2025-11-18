from class_er import EsprReg



esp_reg = EsprReg()
esp_reg.set_pattern(r'^[a-zA-Z0-9]+$')  # Esempio: stringa alfanumerica
result = esp_reg.validate("Test123")
print(f'La stringa "Test123" è un: {result}')

result = esp_reg.validate("Test@123")
print(f'La stringa "Test@123" è un: {result}')
# Output atteso:
# La stringa "Test123" è un: match
# La stringa "Test@123" è un: mismatch