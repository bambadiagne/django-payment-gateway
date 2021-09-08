import paydunya
import os
from paydunya import Store
PAYDUNYA_ACCESS_TOKENS = {
  'PAYDUNYA-MASTER-KEY':os.environ.get("PAYDUNYA_MASTER_KEY"),
  'PAYDUNYA-PRIVATE-KEY':os.environ.get("PAYDUNYA_PRIVATE_KEY"),
  'PAYDUNYA-PUBLIC-KEY':os.environ.get("PAYDUNYA_PUBLIC_KEY"),
  'PAYDUNYA-TOKEN':os.environ.get("PAYDUNYA_TOKEN"),
}
paydunya.API_keys = PAYDUNYA_ACCESS_TOKENS

paydunya.debug = True


infos = {
  'name': "paymentpaydunya", # Seul le nom est requis
  
}
store = Store(**infos)
invoice = paydunya.Invoice(store)