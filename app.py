import streamlit as st
import pandas as pd
import json
import os

from auth import login
from logger import guardar_log

# ========================
# Archivos
# ========================

DATA_FILE="data.json"
TASK_FILE="tareas.json"


# ========================
# TAREAS
# ========================

def cargar_tareas():

    if not os.path.exists(TASK_FILE):

        return {"tareas":[]}

    with open(
        TASK_FILE,
        "r",
        encoding="utf8"
    ) as f:

        return json.load(f)


def guardar_tareas(data):

    with open(
        TASK_FILE,
        "w",
        encoding="utf8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def agregar_tarea(
    titulo,
    descripcion,
    grupo
):

    data=cargar_tareas()

    data["tareas"].append({

        "titulo":titulo,
        "descripcion":descripcion,
        "grupo":grupo

    })

    guardar_tareas(data)


# ========================
# DICCIONARIO
# ========================

def load_data():

    if not os.path.exists(DATA_FILE):

        return {"conceptos":[]}

    with open(
        DATA_FILE,
        "r",
        encoding="utf8"
    ) as f:

        return json.load(f)



def save_data(data):

    with open(
        DATA_FILE,
        "w",
        encoding="utf8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def get_definicions():

    data=load_data()

    return [

        (
            c["id"],
            c["termino"],
            c["definicion"]
        )

        for c in data["conceptos"]

    ]


def insert_definicion(
    termino,
    definicion
):

    data=load_data()

    conceptos=data["conceptos"]

    new_id=max(
        [c["id"] for c in conceptos],
        default=0
    )+1


    conceptos.append({

        "id":new_id,

        "termino":termino,

        "definicion":definicion

    })

    save_data(data)



def update_definicion_by_id(
    registro_id,
    termino,
    definicion
):

    data=load_data()

    for c in data["conceptos"]:

        if c["id"]==registro_id:

            c["termino"]=termino
            c["definicion"]=definicion

    save_data(data)



def delete_definicion(
    termino
):

    data=load_data()

    data["conceptos"]=[

        c

        for c in data["conceptos"]

        if c["termino"]!=termino

    ]

    save_data(data)



# ========================
# Importaciones vistas
# ========================

from A1 import A1
from A2 import A2
from Examen2 import ExamenA2
from ExamenA1 import ExamenA1


# ========================
# Config
# ========================

st.set_page_config(

    page_title="Puma English",
    layout="centered"

)


# ========================
# Sesiones
# ========================

if "usuario" not in st.session_state:

    st.session_state.usuario=None


if "rol" not in st.session_state:

    st.session_state.rol=None


# ========================
# LOGIN
# ========================

if st.session_state.usuario is None:


    st.title(
        "Puma English"
    )


    usuario=st.text_input(
        "Usuario"
    )


    password=st.text_input(
        "Contraseña",
        type="password"
    )


    if st.button(
        "Entrar"
    ):


        user=login(
            usuario,
            password
        )


        if user:


            st.session_state.usuario=usuario

            st.session_state.rol=user["rol"]


            guardar_log(

                usuario,

                "Inicio sesión"

            )

            st.rerun()


        else:

            st.error(
                "Datos incorrectos"
            )


    st.stop()


# ========================
# Sidebar
# ========================

st.sidebar.success(

    f"Bienvenido {st.session_state.usuario}"

)


st.sidebar.write(

    "Rol:",
    st.session_state.rol

)


# ========================
# Menús roles
# ========================

if st.session_state.rol=="alumno":

    opciones=[

        "Diccionary",
        "Tareas",
        "A1",
        "A2",
        "Examen A1",
        "Examen A2"

    ]


elif st.session_state.rol=="maestra":

    opciones=[

        "Diccionary",
        "A1",
        "A2",
        "Examen A1",
        "Examen A2",
        "Panel Maestra"

    ]


elif st.session_state.rol=="administrador":

    opciones=[

        "Diccionary",
        "A1",
        "A2",
        "Examen A1",
        "Examen A2",
        "Logs"

    ]


menu=st.sidebar.radio(

    "Selecciona:",
    opciones

)


# ========================
# Cerrar sesión
# ========================

if st.sidebar.button(
    "Cerrar sesión"
):

    guardar_log(

        st.session_state.usuario,

        "Cerró sesión"

    )

    st.session_state.usuario=None

    st.session_state.rol=None

    st.rerun()



# ====================================
# TAREAS ALUMNOS
# ====================================

if menu=="Tareas":

    st.title(
        "Mis actividades"
    )

    tareas=cargar_tareas()


    if len(tareas["tareas"])==0:

        st.info(
            "No hay actividades"
        )


    for t in tareas["tareas"]:

        with st.expander(
            t["titulo"]
        ):

            st.write(
                t["descripcion"]
            )

            st.caption(
                "Grupo: "+t["grupo"]
            )


# ====================================
# DICCIONARIO
# ====================================

elif menu=="Diccionary":

    st.title(
        "Puma English"
    )


    col1,col2=st.columns([3,1])


    with col1:

        query=st.text_input(
            "Buscar"
        )


        if query:

            guardar_log(

                st.session_state.usuario,

                f"Buscó: {query}"

            )


    with col2:

        exact=st.checkbox(
            "Exacta"
        )


    rows=get_definicions()


    data={

        r[1]:r[2]

        for r in rows

    }


    id_map={

        r[1]:r[0]

        for r in rows

    }


    def search(
        q,
        exact_match
    ):

        q=q.lower()

        if not q:

            return sorted(
                data.items()
            )


        if exact_match:

            return [

                (k,v)

                for k,v in data.items()

                if k.lower()==q

            ]


        return [

            (k,v)

            for k,v in data.items()

            if q in k.lower()
            or q in v.lower()

        ]


    results=search(
        query,
        exact
    )


    for palabra,defin in results:

        with st.expander(
            palabra
        ):

            st.write(
                defin
            )


# ====================================
# A1
# ====================================

elif menu=="A1":

    guardar_log(
        st.session_state.usuario,
        "Entró A1"
    )

    A1.app()


elif menu=="A2":

    guardar_log(
        st.session_state.usuario,
        "Entró A2"
    )

    A2.app()


elif menu=="Examen A1":

    guardar_log(
        st.session_state.usuario,
        "Entró Examen A1"
    )

    ExamenA1.app()


elif menu=="Examen A2":

    guardar_log(
        st.session_state.usuario,
        "Entró Examen A2"
    )

    ExamenA2.app()



# ====================================
# PANEL MAESTRA
# ====================================

elif menu=="Panel Maestra":

    st.title(
        "Panel Maestra"
    )


    tab1,tab2=st.tabs(

        [
            "Actividad",
            "Asignaciones"
        ]

    )


    with tab1:


        st.subheader(
            "Actividad alumnos"
        )


        try:


            with open(
                "logs.json",
                "r",
                encoding="utf8"
            ) as f:


                logs=json.load(f)


            df=pd.DataFrame(
                logs
            )


            st.dataframe(
                df,
                use_container_width=True
            )


        except:

            st.warning(
                "Sin registros"
            )


    with tab2:


        titulo=st.text_input(
            "Título"
        )


        descripcion=st.text_area(
            "Descripción"
        )


        grupo=st.selectbox(

            "Asignar a",

            [

                "Todos",
                "A1",
                "A2"

            ]

        )


        if st.button(
            "Crear actividad"
        ):


            agregar_tarea(

                titulo,
                descripcion,
                grupo

            )


            guardar_log(

                st.session_state.usuario,

                f"Creó tarea {titulo}"

            )


            st.success(
                "Actividad creada"
            )


# ====================================
# ADMIN
# ====================================

elif menu=="Logs":

    st.title(
        "Logs"
    )


    try:

        with open(
            "logs.json",
            "r",
            encoding="utf8"
        ) as f:

            data=json.load(f)


        df=pd.DataFrame(
            data
        )


        st.dataframe(
            df,
            use_container_width=True
        )


    except:

        st.warning(
            "Sin registros"
        )