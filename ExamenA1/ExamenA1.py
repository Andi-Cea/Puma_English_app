import streamlit as st
import math

def check_answer_int(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_int += 10
            st.session_state.exercises_completed_int += 1
            st.success("Correcto! +10 puntos")
            return True
        else:
            st.error("Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("Formato invalido. Usa numeros.")
        return False

def app():
    st.title("Ejercicios Interactivos - Ingles Nivel A1")
    
    # Inicializar estado de la sesion
    if 'score_int' not in st.session_state:
        st.session_state.score_int = 0
    if 'exercises_completed_int' not in st.session_state:
        st.session_state.exercises_completed_int = 0

    # Menu de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "1. Verb To Be - Presente",
            "2. Pronombres Personales",
            "3. Numeros y Fechas",
            "4. Vocabulario Basico",
            "5. Presente Simple",
            "6. Adjetivos Basicos",
            "7. Preposiciones de Lugar",
            "8. There is / There are",
            "9. Preguntas con Do/Does",
            "10. Frases Cotidianas"
        ]
    )
    
    # Mostrar puntuacion
    st.sidebar.markdown("---")
    st.sidebar.metric("Puntuacion", st.session_state.score_int)
    st.sidebar.metric("Ejercicios Completados", st.session_state.exercises_completed_int)
    
    if st.sidebar.button("Reiniciar Puntuacion"):
        st.session_state.score_int = 0
        st.session_state.exercises_completed_int = 0
        st.rerun()

    # ========== 1. VERB TO BE - PRESENTE ==========
    if tema == "1. Verb To Be - Presente":
        st.header("1. Verb To Be - Presente (Ser o Estar)")
        st.info("Practica el verbo mas importante en ingles: am, is, are")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Completa con la forma correcta de To Be")
        st.write("I ________ a student.")
        
        opciones1 = ["am", "is", "are"]
        user_answer1 = st.radio("Selecciona:", opciones1, key="tobe1")
        
        if st.button("Verificar", key="check_tobe1"):
            if user_answer1 == "am":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'I am a student'")
            else:
                st.error("Incorrecto. 'I' siempre va con 'am'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Completa la oracion")
        st.write("She ________ happy today.")
        
        user_answer2 = st.radio("Selecciona:", opciones1, key="tobe2")
        
        if st.button("Verificar oracion", key="check_tobe2"):
            if user_answer2 == "is":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'She is happy today'")
            else:
                st.error("Incorrecto. 'He', 'She', 'It' usan 'is'")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Forma negativa")
        st.write("They ________ (not) at home.")
        
        user_answer3 = st.text_input("Escribe la oracion completa:", key="tobe3")
        
        if st.button("Verificar negativa", key="check_tobe3"):
            if user_answer3.lower().strip() == "are not" or user_answer3.lower().strip() == "aren't":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'They are not at home' o 'They aren't at home'")
            else:
                st.error("Incorrecto. La respuesta es 'are not' o 'aren't'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Verbo To Be - Presente:**
            - I am (Yo soy/estoy)
            - You are (Tu eres/estas)
            - He/She/It is (El/Ella/Ello es/esta)
            - We are (Nosotros somos/estamos)
            - They are (Ellos son/estan)
            
            **Negativo:** am not, is not (isn't), are not (aren't)
            """)

    # ========== 2. PRONOMBRES PERSONALES ==========
    elif tema == "2. Pronombres Personales":
        st.header("2. Pronombres Personales")
        st.info("Aprende los pronombres en ingles")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Traduce al ingles")
        st.write("Yo = ?")
        
        user_pron1 = st.text_input("Tu respuesta:", key="pron1")
        
        if st.button("Verificar", key="check_pron1"):
            if user_pron1.lower().strip() == "i":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Yo' = I")
            else:
                st.error("Incorrecto. 'Yo' en ingles es 'I' (siempre mayuscula)")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Elige el pronombre correcto")
        st.write("Maria es mi amiga. ________ es muy simpatica.")
        
        opciones_pron = ["I", "You", "He", "She", "It", "We", "They"]
        user_pron2 = st.radio("Selecciona:", opciones_pron, key="pron2")
        
        if st.button("Verificar pronombre", key="check_pron2"):
            if user_pron2 == "She":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'She' para mujeres")
            else:
                st.error("Incorrecto. Maria es mujer, entonces 'She'")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Completa la tabla")
        st.write("Español: Nosotros = Ingles: ________")
        
        user_pron3 = st.text_input("Tu respuesta:", key="pron3")
        
        if st.button("Verificar plural", key="check_pron3"):
            if user_pron3.lower().strip() == "we":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Nosotros' = We")
            else:
                st.error("Incorrecto. 'Nosotros' es 'We'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Pronombres Personales:**
            - I = Yo
            - You = Tu / Ustedes
            - He = El
            - She = Ella
            - It = Ello (cosas, animales)
            - We = Nosotros
            - They = Ellos
            """)

    # ========== 3. NUMEROS Y FECHAS ==========
    elif tema == "3. Numeros y Fechas":
        st.header("3. Numeros y Fechas")
        st.info("Practica los numeros del 1 al 20")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Escribe el numero en ingles")
        st.write("5 = ?")
        
        user_num1 = st.text_input("Tu respuesta:", key="num1")
        
        if st.button("Verificar", key="check_num1"):
            if user_num1.lower().strip() == "five":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 5 = five")
            else:
                st.error("Incorrecto. 5 = five")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Traduce el numero")
        st.write("Doce = ?")
        
        user_num2 = st.text_input("Tu respuesta:", key="num2")
        
        if st.button("Verificar numero", key="check_num2"):
            if user_num2.lower().strip() == "twelve":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Doce = twelve")
            else:
                st.error("Incorrecto. Doce = twelve")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Dia de la semana")
        st.write("El primer dia de la semana es...")
        
        opciones_dia = ["Sunday", "Monday", "Tuesday", "Wednesday"]
        user_dia = st.radio("Selecciona:", opciones_dia, key="dia")
        
        if st.button("Verificar dia", key="check_dia"):
            if user_dia == "Monday":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Monday = Lunes")
            else:
                st.error("Incorrecto. El primer dia laboral es Monday (Lunes)")
        
        with st.expander("Ver explicacion - Numeros 1-20"):
            st.write("""
            one=1, two=2, three=3, four=4, five=5
            six=6, seven=7, eight=8, nine=9, ten=10
            eleven=11, twelve=12, thirteen=13, fourteen=14, fifteen=15
            sixteen=16, seventeen=17, eighteen=18, nineteen=19, twenty=20
            """)

    # ========== 4. VOCABULARIO BASICO ==========
    elif tema == "4. Vocabulario Basico":
        st.header("4. Vocabulario Basico")
        st.info("Aprende palabras basicas en ingles")
        
        # Ejercicio 1 - Colores
        st.subheader("Ejercicio 1: Colores")
        st.write("¿Como se dice 'Rojo' en ingles?")
        
        user_color = st.text_input("Tu respuesta:", key="color")
        
        if st.button("Verificar color", key="check_color"):
            if user_color.lower().strip() == "red":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Rojo = Red")
            else:
                st.error("Incorrecto. Rojo = Red")
        
        # Ejercicio 2 - Animales
        st.subheader("Ejercicio 2: Animales")
        st.write("¿Como se dice 'Perro' en ingles?")
        
        user_animal = st.text_input("Tu respuesta:", key="animal")
        
        if st.button("Verificar animal", key="check_animal"):
            if user_animal.lower().strip() == "dog":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Perro = Dog")
            else:
                st.error("Incorrecto. Perro = Dog")
        
        # Ejercicio 3 - Objetos
        st.subheader("Ejercicio 3: Objetos de la casa")
        st.write("¿Como se dice 'Mesa' en ingles?")
        
        user_objeto = st.text_input("Tu respuesta:", key="objeto")
        
        if st.button("Verificar objeto", key="check_objeto"):
            if user_objeto.lower().strip() == "table":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Mesa = Table")
            else:
                st.error("Incorrecto. Mesa = Table")
        
        # Ejercicio 4 - Familia
        st.subheader("Ejercicio 4: Miembros de la familia")
        st.write("¿Como se dice 'Madre' en ingles?")
        
        user_familia = st.text_input("Tu respuesta:", key="familia")
        
        if st.button("Verificar familia", key="check_familia"):
            if user_familia.lower().strip() == "mother" or user_familia.lower().strip() == "mom":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Madre = Mother o Mom")
            else:
                st.error("Incorrecto. Madre = Mother o Mom")
        
        with st.expander("Ver vocabulario basico"):
            st.write("""
            **Colores:** red(rojo), blue(azul), yellow(amarillo), green(verde)
            **Animales:** dog(perro), cat(gato), bird(pajaro), fish(pez)
            **Familia:** mother(madre), father(padre), brother(hermano), sister(hermana)
            **Casa:** table(mesa), chair(silla), bed(cama), door(puerta)
            """)

    # ========== 5. PRESENTE SIMPLE ==========
    elif tema == "5. Presente Simple":
        st.header("5. Presente Simple")
        st.info("Habla de rutinas y acciones habituales")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Completa la oracion")
        st.write("I ________ (eat) breakfast at 7 AM.")
        
        user_pres1 = st.text_input("Verbo en presente:", key="pres1")
        
        if st.button("Verificar", key="check_pres1"):
            if user_pres1.lower().strip() == "eat":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'I eat breakfast'")
            else:
                st.error("Incorrecto. 'I eat' (sin 's' en tercera persona)")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Tercera persona - He/She/It")
        st.write("She ________ (work) in an office.")
        
        user_pres2 = st.text_input("Verbo en presente:", key="pres2")
        
        if st.button("Verificar tercera persona", key="check_pres2"):
            if user_pres2.lower().strip() == "works":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'She works' (se agrega 's')")
            else:
                st.error("Incorrecto. Con 'She' se agrega 's' -> works")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Negativo en presente")
        st.write("He ________ (not/like) coffee.")
        
        user_pres3 = st.text_input("Oracion negativa:", key="pres3")
        
        if st.button("Verificar negativo", key="check_pres3"):
            if user_pres3.lower().strip() == "doesn't like" or user_pres3.lower().strip() == "does not like":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'doesn't like' es la forma negativa")
            else:
                st.error("Incorrecto. La respuesta es 'doesn't like'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Presente Simple:**
            - I/You/We/They + verbo (I eat, you work, we play)
            - He/She/It + verbo + s (He eats, she works, it plays)
            
            **Negativo:**
            - I/You/We/They + don't + verbo
            - He/She/It + doesn't + verbo
            """)

    # ========== 6. ADJETIVOS BASICOS ==========
    elif tema == "6. Adjetivos Basicos":
        st.header("6. Adjetivos Basicos")
        st.info("Describe personas, lugares y objetos")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Adjetivos opuestos")
        st.write("Big = Grande. ¿Cual es lo opuesto? (pequeño)")
        
        user_adj1 = st.text_input("Tu respuesta:", key="adj1")
        
        if st.button("Verificar", key="check_adj1"):
            if user_adj1.lower().strip() == "small":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Big = Grande, Small = Pequeño")
            else:
                st.error("Incorrecto. Pequeño = Small")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Completa la oracion")
        st.write("The weather is ________ (caliente) today.")
        
        user_adj2 = st.text_input("Traduce 'caliente':", key="adj2")
        
        if st.button("Verificar adjetivo", key="check_adj2"):
            if user_adj2.lower().strip() == "hot":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Caliente = Hot")
            else:
                st.error("Incorrecto. Caliente = Hot")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Elige el adjetivo correcto")
        st.write("This movie is very ________ (bueno).")
        
        opciones_adj = ["bad", "good", "sad", "happy"]
        user_adj3 = st.radio("Selecciona:", opciones_adj, key="adj3")
        
        if st.button("Verificar", key="check_adj3"):
            if user_adj3 == "good":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Bueno = Good")
            else:
                st.error("Incorrecto. Bueno = Good")
        
        with st.expander("Ver adjetivos comunes"):
            st.write("""
            **Adjetivos basicos:**
            - good (bueno) / bad (malo)
            - big (grande) / small (pequeño)
            - happy (feliz) / sad (triste)
            - hot (caliente) / cold (frio)
            - new (nuevo) / old (viejo)
            - beautiful (bonito) / ugly (feo)
            """)

    # ========== 7. PREPOSICIONES DE LUGAR ==========
    elif tema == "7. Preposiciones de Lugar":
        st.header("7. Preposiciones de Lugar")
        st.info("Donde estan las cosas?")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Preposiciones")
        st.write("The cat is ________ the table. (sobre la mesa)")
        
        user_prep1 = st.text_input("Tu respuesta:", key="prep1")
        
        if st.button("Verificar", key="check_prep1"):
            if user_prep1.lower().strip() == "on":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Sobre = On")
            else:
                st.error("Incorrecto. Sobre la mesa = On the table")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Completa la oracion")
        st.write("The school is ________ the park. (al lado del parque)")
        
        user_prep2 = st.text_input("Tu respuesta:", key="prep2")
        
        if st.button("Verificar", key="check_prep2"):
            if user_prep2.lower().strip() == "next to":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Al lado de = Next to")
            else:
                st.error("Incorrecto. Al lado de = Next to")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Elige la preposicion correcta")
        st.write("The pencil is ________ the bag. (dentro de la mochila)")
        
        opciones_prep = ["on", "under", "in", "next to"]
        user_prep3 = st.radio("Selecciona:", opciones_prep, key="prep3")
        
        if st.button("Verificar preposicion", key="check_prep3"):
            if user_prep3 == "in":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Dentro = In")
            else:
                st.error("Incorrecto. Dentro de la mochila = In the bag")
        
        with st.expander("Ver preposiciones de lugar"):
            st.write("""
            **Preposiciones:**
            - in = dentro de
            - on = sobre
            - under = debajo de
            - next to = al lado de
            - behind = detras de
            - in front of = delante de
            - between = entre
            """)

    # ========== 8. THERE IS / THERE ARE ==========
    elif tema == "8. There is / There are":
        st.header("8. There is / There are")
        st.info("Expresar existencia (hay)")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Singular o plural")
        st.write("________ a book on the table.")
        
        opciones_there = ["There is", "There are"]
        user_there1 = st.radio("Selecciona:", opciones_there, key="there1")
        
        if st.button("Verificar", key="check_there1"):
            if user_there1 == "There is":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'There is' para singular (un libro)")
            else:
                st.error("Incorrecto. 'There is' para una cosa")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Plural")
        st.write("________ three cars in the street.")
        
        user_there2 = st.radio("Selecciona:", opciones_there, key="there2")
        
        if st.button("Verificar plural", key="check_there2"):
            if user_there2 == "There are":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'There are' para plural (tres carros)")
            else:
                st.error("Incorrecto. 'There are' para mas de una cosa")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Traduce")
        st.write("Hay un gato en el jardin.")
        
        user_there3 = st.text_input("Traduccion:", key="there3")
        
        if st.button("Verificar traduccion", key="check_there3"):
            if user_there3.lower().strip() == "there is a cat in the garden":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto!")
            else:
                st.error("Incorrecto. La respuesta es 'There is a cat in the garden'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **There is / There are:**
            - There is + singular (una cosa)
            - There are + plural (dos o mas cosas)
            
            Ejemplos:
            - There is a dog. (Hay un perro)
            - There are two dogs. (Hay dos perros)
            - There is water. (Hay agua - incontable)
            """)

    # ========== 9. PREGUNTAS CON DO/DOES ==========
    elif tema == "9. Preguntas con Do/Does":
        st.header("9. Preguntas con Do / Does")
        st.info("Aprende a hacer preguntas en ingles")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Pregunta con Do")
        st.write("________ you like pizza?")
        
        opciones_do = ["Do", "Does", "Is", "Are"]
        user_do1 = st.radio("Selecciona:", opciones_do, key="do1")
        
        if st.button("Verificar", key="check_do1"):
            if user_do1 == "Do":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Do you like pizza?'")
            else:
                st.error("Incorrecto. Con 'you' se usa 'Do'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Pregunta con Does")
        st.write("________ she speak Spanish?")
        
        user_do2 = st.radio("Selecciona:", opciones_do, key="do2")
        
        if st.button("Verificar con Does", key="check_do2"):
            if user_do2 == "Does":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Does she speak Spanish?'")
            else:
                st.error("Incorrecto. Con 'he/she/it' se usa 'Does'")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Crea una pregunta")
        st.write("Tu amigo tiene un perro. Preguntale:")
        
        user_do3 = st.text_input("Tu pregunta:", key="do3")
        
        if st.button("Verificar pregunta", key="check_do3"):
            if user_do3.lower().strip() == "do you have a dog":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Do you have a dog?'")
            else:
                st.error("Incorrecto. La pregunta es 'Do you have a dog?'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Preguntas con Do/Does:**
            - Do + I/you/we/they + verbo?
            - Does + he/she/it + verbo?
            
            Ejemplos:
            - Do you work? (Trabajas?)
            - Does she study? (Estudia ella?)
            """)

    # ========== 10. FRASES COTIDIANAS ==========
    elif tema == "10. Frases Cotidianas":
        st.header("10. Frases Cotidianas")
        st.info("Frases utiles para el dia a dia")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Saludos")
        st.write("¿Como se dice 'Buenos dias' en ingles?")
        
        user_frase1 = st.text_input("Tu respuesta:", key="frase1")
        
        if st.button("Verificar", key="check_frase1"):
            if user_frase1.lower().strip() == "good morning":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Good morning")
            else:
                st.error("Incorrecto. Buenos dias = Good morning")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Cortesia")
        st.write("¿Como se dice 'Gracias' en ingles?")
        
        user_frase2 = st.text_input("Tu respuesta:", key="frase2")
        
        if st.button("Verificar gracias", key="check_frase2"):
            if user_frase2.lower().strip() == "thank you" or user_frase2.lower().strip() == "thanks":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Thank you / Thanks")
            else:
                st.error("Incorrecto. Gracias = Thank you")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Despedidas")
        st.write("¿Como se dice 'Adios' en ingles?")
        
        user_frase3 = st.text_input("Tu respuesta:", key="frase3")
        
        if st.button("Verificar adios", key="check_frase3"):
            if user_frase3.lower().strip() == "goodbye" or user_frase3.lower().strip() == "bye":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Goodbye / Bye")
            else:
                st.error("Incorrecto. Adios = Goodbye")
        
        # Ejercicio 4
        st.subheader("Ejercicio 4: Presentacion")
        st.write("¿Como te presentas? 'Me llamo Juan' = ________")
        
        user_frase4 = st.text_input("Tu respuesta:", key="frase4")
        
        if st.button("Verificar presentacion", key="check_frase4"):
            if user_frase4.lower().strip() == "my name is juan":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'My name is Juan'")
            else:
                st.error("Incorrecto. 'My name is Juan'")
        
        with st.expander("Ver frases utiles"):
            st.write("""
            **Saludos y cortesia:**
            - Hello / Hi = Hola
            - Good morning = Buenos dias
            - Good afternoon = Buenas tardes
            - Good night = Buenas noches
            - Thank you = Gracias
            - Please = Por favor
            - Sorry = Lo siento
            - Goodbye / Bye = Adios
            
            **Presentacion:**
            - My name is... = Me llamo...
            - Nice to meet you = Mucho gusto
            - How are you? = Como estas?
            - I'm fine, thanks = Estoy bien, gracias
            """)

    # Barra de progreso
    st.sidebar.markdown("---")
    if st.session_state.exercises_completed_int > 0:
        progress = min(st.session_state.score_int / 100, 1.0)
        st.sidebar.progress(progress)
        st.sidebar.write(f"Progreso: {int(progress * 100)}%")

# Ejecutar la aplicacion
if __name__ == "__main__":
    app()