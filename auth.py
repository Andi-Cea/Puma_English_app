import json

def login(usuario,password):

    with open("users.json","r",encoding="utf8") as f:
        datos=json.load(f)

    usuarios=datos["usuarios"]

    for u in usuarios:

        if(
            u["usuario"]==usuario and
            u["password"]==password
        ):

            return u

    return None