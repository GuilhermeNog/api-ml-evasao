import sklearn.compose._column_transformer as ct

print("Atributos em sklearn.compose._column_transformer:")
for attr in dir(ct):
    if not attr.startswith('__'):
        print(f"  - {attr}")

# Tenta ver se tem algo com "Remainder"
print("\n\nAtributos com 'remainder' ou 'Remainder':")
for attr in dir(ct):
    if 'remainder' in attr.lower():
        print(f"  - {attr}")
