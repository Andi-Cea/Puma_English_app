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
    st.title("Ejercicios Interactivos - Ingles Nivel A2")
    
    # Inicializar estado de la sesion
    if 'score_int' not in st.session_state:
        st.session_state.score_int = 0
    if 'exercises_completed_int' not in st.session_state:
        st.session_state.exercises_completed_int = 0

    # Menu de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "1. Past Simple vs Past Continuous",
            "2. Present Perfect",
            "3. Future Forms",
            "4. Modal Verbs",
            "5. Comparatives and Superlatives",
            "6. Conditionals Type 0 and 1",
            "7. Passive Voice (Present and Past)",
            "8. Reported Speech (Basic)",
            "9. Phrasal Verbs (Common)",
            "10. Connectors and Linking Words"
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

    # ========== 1. PAST SIMPLE VS PAST CONTINUOUS ==========
    if tema == "1. Past Simple vs Past Continuous":
        st.header("1. Past Simple vs Past Continuous")
        st.info("Practica la diferencia entre acciones completadas y acciones en progreso en el pasado")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Completa la oracion")
        st.write("Yesterday at 8 PM, I ________ (watch) TV when the phone ________ (ring).")
        
        col1, col2 = st.columns(2)
        with col1:
            user_verb1 = st.text_input("Primer verbo (past continuous):", key="past1")
        with col2:
            user_verb2 = st.text_input("Segundo verbo (past simple):", key="past2")
        
        if st.button("Verificar", key="check_past1"):
            if user_verb1.lower().strip() == "was watching" and user_verb2.lower().strip() == "rang":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'was watching' y 'rang'")
            else:
                st.error("Incorrecto. La respuesta es 'was watching' y 'rang'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Elige la opcion correcta")
        st.write("While I ________ to work, I ________ an accident.")
        
        opciones = [
            "walked / saw",
            "was walking / was seeing",
            "was walking / saw",
            "walked / was seeing"
        ]
        
        user_choice = st.radio("Selecciona:", opciones, key="past_choice")
        
        if st.button("Verificar opcion", key="check_past2"):
            if user_choice == "was walking / saw":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Accion larga (was walking) interrumpida por accion corta (saw)")
            else:
                st.error("Incorrecto. La respuesta correcta es 'was walking / saw'")
        
        # Explicacion
        with st.expander("Ver explicacion"):
            st.write("""
            **Past Simple:** Acciones completadas en el pasado.
            **Past Continuous:** Acciones en progreso en un momento especifico del pasado.
            
            Cuando una accion interrumpe a otra:
            - Past Continuous para la accion larga (fondo)
            - Past Simple para la accion corta (interrupcion)
            """)

    # ========== 2. PRESENT PERFECT ==========
    elif tema == "2. Present Perfect":
        st.header("2. Present Perfect")
        st.info("Practica experiencias pasadas sin tiempo especifico")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Completa con 'for' o 'since'")
        st.write("1. I have lived in this city ________ 2015.")
        st.write("2. She has studied English ________ three years.")
        
        user_for_since1 = st.text_input("Respuesta 1:", key="fs1")
        user_for_since2 = st.text_input("Respuesta 2:", key="fs2")
        
        if st.button("Verificar for/since", key="check_fs"):
            if user_for_since1.lower().strip() == "since" and user_for_since2.lower().strip() == "for":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! since + punto de inicio, for + periodo de tiempo")
            else:
                st.error("Incorrecto. since + año (2015), for + duracion (three years)")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Preguntas en Present Perfect")
        st.write("Crea una pregunta usando 'ever' para la siguiente situacion:")
        st.write("Quieres saber si tu amigo ha visitado Paris.")
        
        user_question = st.text_input("Tu pregunta:", key="question")
        
        if st.button("Verificar pregunta", key="check_question"):
            correct_answers = [
                "have you ever visited paris",
                "have you ever been to paris"
            ]
            if user_question.lower().strip() in correct_answers:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Have you ever visited Paris?'")
            else:
                st.error("La respuesta correcta es: 'Have you ever visited Paris?'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Present Perfect:** have/has + past participle
            - Experiencias: I have visited London.
            - Sin tiempo especifico
            - 'Ever' en preguntas, 'never' en negativas
            - 'For' + duracion, 'Since' + punto de inicio
            """)

    # ========== 3. FUTURE FORMS ==========
    elif tema == "3. Future Forms":
        st.header("3. Future Forms: Will vs Going to")
        st.info("Practica la diferencia entre decisiones espontaneas y planes")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Decide que forma usar")
        st.write("Las nubes estan muy oscuras. Creo que ________ (rain).")
        
        user_future1 = st.text_input("Tu respuesta:", key="future1")
        
        if st.button("Verificar", key="check_future1"):
            if user_future1.lower().strip() == "is going to rain":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Going to - prediccion con evidencia")
            else:
                st.error("Incorrecto. La respuesta es 'is going to rain'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Decision espontanea")
        st.write("El telefono esta sonando. Yo ________ (answer) it.")
        
        user_future2 = st.text_input("Tu respuesta:", key="future2")
        
        if st.button("Verificar decision", key="check_future2"):
            if user_future2.lower().strip() == "will answer":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Will - decision espontanea en el momento")
            else:
                st.error("Incorrecto. La respuesta es 'will answer'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Will:** Decisiones espontaneas, predicciones sin evidencia, promesas
            **Going to:** Planes, predicciones con evidencia visible
            
            Ejemplos:
            - It's cold. I will close the window. (decision espontanea)
            - Look at those clouds! It's going to rain. (evidencia)
            """)

    # ========== 4. MODAL VERBS ==========
    elif tema == "4. Modal Verbs":
        st.header("4. Modal Verbs: Can, Could, Should, Must")
        st.info("Practica verbos modales para habilidad, permiso, consejo y obligacion")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Elige el modal correcto")
        st.write("You ________ eat more vegetables. It's good for your health.")
        
        opciones_modal = ["can", "could", "should", "must"]
        user_modal = st.radio("Selecciona:", opciones_modal, key="modal1")
        
        if st.button("Verificar modal", key="check_modal1"):
            if user_modal == "should":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Should - consejo")
            else:
                st.error("Incorrecto. 'Should' se usa para dar consejos")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Traduce")
        st.write("No puedo encontrar mis llaves.")
        
        user_translation = st.text_input("Traduccion al ingles:", key="translation")
        
        if st.button("Verificar traduccion", key="check_trans"):
            if user_translation.lower().strip() == "i can't find my keys":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto!")
            else:
                st.error("Incorrecto. La respuesta es 'I can't find my keys'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Can:** habilidad, permiso informal
            **Could:** habilidad pasada, permiso formal
            **Should:** consejo, recomendacion
            **Must:** obligacion fuerte, prohibicion (mustn't)
            """)

    # ========== 5. COMPARATIVES AND SUPERLATIVES ==========
    elif tema == "5. Comparatives and Superlatives":
        st.header("5. Comparatives and Superlatives")
        st.info("Practica comparaciones entre personas, objetos y lugares")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Completa el comparativo")
        st.write("This book is ________ (interesting) than the movie.")
        
        user_comp = st.text_input("Tu respuesta:", key="comp")
        
        if st.button("Verificar comparativo", key="check_comp"):
            if user_comp.lower().strip() == "more interesting":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! adjetivos largos: more + adjective")
            else:
                st.error("Incorrecto. La respuesta es 'more interesting'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Superlativo")
        st.write("Mount Everest is ________ (high) mountain in the world.")
        
        user_sup = st.text_input("Tu respuesta:", key="sup")
        
        if st.button("Verificar superlativo", key="check_sup"):
            if user_sup.lower().strip() == "the highest":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! adjetivos cortos: the + adj+est")
            else:
                st.error("Incorrecto. La respuesta es 'the highest'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Comparativos:**
            - Adjetivos cortos (+er): taller, faster
            - Adjetivos largos (more + adj): more expensive
            - Irregulares: good -> better, bad -> worse
            
            **Superlativos:**
            - Adjetivos cortos (the + adj+est): the tallest
            - Adjetivos largos (the most + adj): the most beautiful
            """)

    # ========== 6. CONDITIONALS TYPE 0 AND 1 ==========
    elif tema == "6. Conditionals Type 0 and 1":
        st.header("6. Conditionals Type 0 and 1")
        st.info("Practica situaciones reales y probables")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Zero Conditional")
        st.write("Completa: If you ________ (heat) water to 100°C, it ________ (boil).")
        
        col1, col2 = st.columns(2)
        with col1:
            user_zero1 = st.text_input("Primer verbo:", key="zero1")
        with col2:
            user_zero2 = st.text_input("Segundo verbo:", key="zero2")
        
        if st.button("Verificar zero conditional", key="check_zero"):
            if user_zero1.lower().strip() == "heat" and user_zero2.lower().strip() == "boils":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Zero conditional - hechos generales")
            else:
                st.error("Incorrecto. La respuesta es 'heat' y 'boils'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: First Conditional")
        st.write("Completa: If it ________ (rain) tomorrow, we ________ (stay) at home.")
        
        col1, col2 = st.columns(2)
        with col1:
            user_first1 = st.text_input("Primer verbo:", key="first1")
        with col2:
            user_first2 = st.text_input("Segundo verbo:", key="first2")
        
        if st.button("Verificar first conditional", key="check_first"):
            if user_first1.lower().strip() == "rains" and user_first2.lower().strip() == "will stay":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! First conditional - posibilidad real")
            else:
                st.error("Incorrecto. La respuesta es 'rains' y 'will stay'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Zero Conditional (hechos generales):**
            If + present simple, present simple
            
            **First Conditional (posibilidades reales):**
            If + present simple, will + infinitivo
            """)

    # ========== 7. PASSIVE VOICE ==========
    elif tema == "7. Passive Voice (Present and Past)":
        st.header("7. Passive Voice - Present and Past")
        st.info("Practica como enfatizar la accion y no quien la realiza")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Present Passive")
        st.write("Transforma a voz pasiva: 'Someone cleans the office every day'")
        
        user_passive1 = st.text_input("Oracion pasiva:", key="passive1")
        
        if st.button("Verificar passive", key="check_pass1"):
            if user_passive1.lower().strip() == "the office is cleaned every day":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! is + past participle")
            else:
                st.error("Incorrecto. La respuesta es 'The office is cleaned every day'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Past Passive")
        st.write("Transforma a voz pasiva: 'Leonardo da Vinci painted the Mona Lisa'")
        
        user_passive2 = st.text_input("Oracion pasiva:", key="passive2")
        
        if st.button("Verificar past passive", key="check_pass2"):
            if user_passive2.lower().strip() == "the mona lisa was painted by leonardo da vinci":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! was + past participle")
            else:
                st.error("Incorrecto. La respuesta es 'The Mona Lisa was painted by Leonardo da Vinci'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Voz Pasiva:** sujeto + verbo to be + past participle
            
            Presente: am/is/are + past participle
            Pasado: was/were + past participle
            
            Se usa cuando la accion es mas importante que quien la realiza.
            """)

    # ========== 8. REPORTED SPEECH BASIC ==========
    elif tema == "8. Reported Speech (Basic)":
        st.header("8. Reported Speech - Basic")
        st.info("Practica como reportar lo que alguien dijo")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Cambia a reported speech")
        st.write("Direct speech: 'I am happy,' she said.")
        
        user_reported1 = st.text_input("Reported speech:", key="rep1")
        
        if st.button("Verificar reported", key="check_rep1"):
            correct_answers = ["she said she was happy", "she said that she was happy"]
            if user_reported1.lower().strip() in correct_answers:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! am -> was, said + that")
            else:
                st.error("Incorrecto. La respuesta es 'She said she was happy'")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Cambia a reported speech")
        st.write("Direct speech: 'I will call you tomorrow,' he told me.")
        
        user_reported2 = st.text_input("Reported speech:", key="rep2")
        
        if st.button("Verificar reported 2", key="check_rep2"):
            correct_answers = [
                "he told me he would call me the next day",
                "he told me that he would call me the next day"
            ]
            if user_reported2.lower().strip() in correct_answers:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! will -> would, tomorrow -> the next day")
            else:
                st.error("Incorrecto. La respuesta es 'He told me he would call me the next day'")
        
        with st.expander("Ver explicacion"):
            st.write("""
            **Cambios en Reported Speech:**
            - Present Simple -> Past Simple
            - will -> would
            - am/is/are -> was/were
            - today -> that day
            - tomorrow -> the next day
            - here -> there
            """)

    # ========== 9. PHRASAL VERBS ==========
    elif tema == "9. Phrasal Verbs (Common)":
        st.header("9. Common Phrasal Verbs")
        st.info("Practica los phrasal verbs mas usados en ingles")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Empareja el significado")
        st.write("Look up = ?")
        
        meanings = {
            "buscar informacion": "look up",
            "levantarse": "get up",
            "apagar": "turn off",
            "encender": "turn on",
            "rendirse": "give up"
        }
        
        user_meaning = st.radio("Selecciona el significado:", list(meanings.keys()), key="pv1")
        
        if st.button("Verificar phrasal 1", key="check_pv1"):
            if user_meaning == "buscar informacion":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Look up = buscar informacion (en diccionario/internet)")
            else:
                st.error("Incorrecto. Look up = buscar informacion")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Completa la oracion")
        st.write("Please ________ the TV. I want to watch the news.")
        
        user_pv = st.text_input("Phrasal verb (turn ___):", key="pv2")
        
        if st.button("Verificar phrasal 2", key="check_pv2"):
            if user_pv.lower().strip() == "turn on":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Turn on = encender")
            else:
                st.error("Incorrecto. La respuesta es 'turn on'")
        
        with st.expander("Ver explicacion - Phrasal Verbs comunes"):
            st.write("""
            **Phrasal Verbs mas usados:**
            - look up = buscar informacion
            - get up = levantarse
            - turn on = encender
            - turn off = apagar
            - give up = rendirse
            - look for = buscar
            - run out of = quedarse sin
            - find out = descubrir
            """)

    # ========== 10. CONNECTORS AND LINKING WORDS ==========
    elif tema == "10. Connectors and Linking Words":
        st.header("10. Connectors and Linking Words")
        st.info("Practica como conectar ideas en ingles")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Elige el conector correcto")
        st.write("I wanted to go to the party, ________ I was too tired.")
        
        connectors = ["and", "but", "so", "because"]
        user_conn1 = st.radio("Selecciona:", connectors, key="conn1")
        
        if st.button("Verificar conector 1", key="check_conn1"):
            if user_conn1 == "but":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'But' expresa contraste")
            else:
                st.error("Incorrecto. 'But' se usa para contraste")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Completa con 'so', 'because', o 'although'")
        st.write("________ it was raining, we went to the beach.")
        
        user_conn2 = st.text_input("Tu respuesta:", key="conn2")
        
        if st.button("Verificar conector 2", key="check_conn2"):
            if user_conn2.lower().strip() == "although":
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! 'Although' = a pesar de que (concesion)")
            else:
                st.error("Incorrecto. La respuesta es 'Although'")
        
        # Ejercicio 3
        st.subheader("Ejercicio 3: Une las oraciones")
        st.write("Ella estudio mucho. Aprobo el examen.")
        st.write("Usa 'so' o 'because':")
        
        user_conn3 = st.text_input("Oracion completa:", key="conn3")
        
        if st.button("Verificar conectores", key="check_conn3"):
            correct_answers = [
                "she studied so she passed the exam",
                "she studied, so she passed the exam",
                "she passed the exam because she studied"
            ]
            if user_conn3.lower().strip() in correct_answers:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("Correcto! Excelente uso de conectores")
            else:
                st.error("Ejemplos correctos: 'She studied, so she passed the exam' o 'She passed the exam because she studied'")
        
        with st.expander("Ver explicacion - Conectores"):
            st.write("""
            **Conectores mas comunes:**
            - **and** = y (suma ideas)
            - **but** = pero (contraste)
            - **so** = asi que (consecuencia)
            - **because** = porque (causa)
            - **although** = aunque (concesion)
            - **however** = sin embargo
            - **therefore** = por lo tanto
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