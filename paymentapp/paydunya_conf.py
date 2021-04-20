import paydunya
import os
from paydunya import Store
PAYDUNYA_ACCESS_TOKENS = {
  'PAYDUNYA-MASTER-KEY':os.environ.get("PAYDUNYA_MASTER_KEY"),
  'PAYDUNYA-PRIVATE-KEY':os.environ.get("PAYDUNYA_PRIVATE_KEY"),
  'PAYDUNYA-TOKEN':os.environ.get("PAYDUNYA_TOKEN"),
}
print(os.environ.get("PAYDUNYA_MASTER_KEY"))
print(os.environ.get("PAYDUNYA_PRIVATE_KEY"))
print(os.environ.get("PAYDUNYA_TOKEN"))
# Activer le mode 'test'. Le debug est à False par défaut
paydunya.debug = True

# Configurer les clés d'API
paydunya.API_keys = PAYDUNYA_ACCESS_TOKENS

infos = {
  'name': "payment-paydunya", # Seul le nom est requis
  'tagline': "Application pour tester l'API paydunya",
  'postal_address': "Dakar Plateau - Etablissement kheweul",
  'phone_number': "779449628",
  'website_url': "https://paymentpaydunya.herokuapp.com/",
  'logo_url': "http://www.chez-sandra.sn/logo.png"
}

store = Store(**infos)
invoice = paydunya.Invoice(store)