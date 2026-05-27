import json
import os

from datetime import datetime


def guardar_log(
    usuario,
    accion
):

    archivo="logs.json"


    try:

        if os.path.exists(archivo):

            with open(
                archivo,
                "r",
                encoding="utf8"
            ) as f:


                contenido=f.read().strip()


                if contenido:

                    datos=json.loads(
                        contenido
                    )

                else:

                    datos=[]


        else:

            datos=[]


    except:

        datos=[]


    datos.append({

        "usuario":usuario,

        "accion":accion,

        "fecha":datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    })


    with open(
        archivo,
        "w",
        encoding="utf8"
    ) as f:


        json.dump(

            datos,

            f,

            indent=4,

            ensure_ascii=False

        )