from fastapi import FastAPI
from AES import AESCipher
app = FastAPI()
 
@app.get("/got_it/{key}/{mess}")
def read_course(key,mess):
  fuck=AESCipher(key)
  lol=fuck.encrypt(mess)
  
  return {"message for you": lol}

@app.get("/give_it/{key}/{mess}")
def rr(key,mess):
  a=mess.replace('%2B','+')
  b=a.replace('%2F',"/")
  me=b.replace('_',"/")
  
  #mess.replace('%40',"/")  
  #mess.replace('%3D','=')
  print(me)
  fuck=AESCipher(key)
  lol=fuck.decrypt(me)
  return {"message for you": lol}
