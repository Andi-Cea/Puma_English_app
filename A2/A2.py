import streamlit as st

def app():
    st.title("Curso de Ingles - Nivel A2")
    st.markdown("---")
    
    # Inicializar estado de la sesion
    if 'progress_int' not in st.session_state:
        st.session_state.progress_int = {}
    if 'completed_lessons_int' not in st.session_state:
        st.session_state.completed_lessons_int = set()

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
    
    # Mostrar progreso general
    st.sidebar.markdown("---")
    st.sidebar.subheader("Progreso del Curso")
    
    total_lessons = 10
    completed = len(st.session_state.completed_lessons_int)
    progress_percentage = completed / total_lessons
    
    st.sidebar.progress(progress_percentage)
    st.sidebar.write(f"Lecciones completadas: {completed}/{total_lessons}")
    
    if st.sidebar.button("Reiniciar Progreso"):
        st.session_state.progress_int = {}
        st.session_state.completed_lessons_int = set()
        st.rerun()

    # ========== 1. PAST SIMPLE VS PAST CONTINUOUS ==========
    if tema == "1. Past Simple vs Past Continuous":
        st.header("1. Past Simple vs Past Continuous")
        
        st.subheader("Leccion Teorica")
        st.write("""
        En esta leccion aprenderas la diferencia entre el Past Simple y el Past Continuous.
        
        **Past Simple:**
        - Se usa para acciones completadas en el pasado
        - Indica que una accion comenzo y termino en el pasado
        - Ejemplo: I watched TV yesterday. (Ayer vi television, accion completada)
        
        **Past Continuous:**
        - Se usa para acciones que estaban en progreso en un momento especifico del pasado
        - Indica una accion que estaba ocurriendo cuando otra accion la interrumpio
        - Ejemplo: I was watching TV when the phone rang. (Estaba viendo TV cuando sonó el telefono)
        
        **Regla clave:**
        Cuando una accion interrumpe a otra:
        - Past Continuous para la accion larga (fondo)
        - Past Simple para la accion corta (interrupcion)
        
        **Estructura:**
        - Past Simple: sujeto + verbo en pasado
        - Past Continuous: sujeto + was/were + verbo+ing
        """)
        
        st.subheader("Ejemplos Practicos")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Past Simple:")
            st.write("- I ate breakfast at 7 AM.")
            st.write("- She arrived yesterday.")
            st.write("- They finished the project.")
        with col2:
            st.write("Past Continuous:")
            st.write("- I was eating breakfast at 7 AM.")
            st.write("- She was sleeping when I called.")
            st.write("- They were working all day.")
        
        st.subheader("Ejercicio de Practica")
        st.write("Completa las siguientes oraciones:")
        
        ejercicios = {
            "Yesterday at 8 PM, I ________ (watch) TV when the phone ________ (ring).": 
            "was watching, rang",
            "While I ________ (walk) to work, I ________ (see) an accident.": 
            "was walking, saw",
            "She ________ (read) a book when the lights ________ (go out).": 
            "was reading, went out"
        }
        
        respuestas_correctas = 0
        for i, (ejercicio, respuesta_correcta) in enumerate(ejercicios.items()):
            st.write(f"{i+1}. {ejercicio}")
            user_answer = st.text_input(f"Tu respuesta {i+1}:", key=f"past_{i}")
            if user_answer:
                if user_answer.lower().strip() == respuesta_correcta:
                    respuestas_correctas += 1
                    st.success("Correcto")
                else:
                    st.info(f"La respuesta correcta es: {respuesta_correcta}")
        
        if st.button("Completar Leccion 1"):
            if respuestas_correctas >= 2:
                st.session_state.completed_lessons_int.add("Past Simple vs Past Continuous")
                st.success("Felicitaciones. Has completado la leccion 1.")
            else:
                st.warning("Responde al menos 2 ejercicios correctamente para completar la leccion.")

    # ========== 2. PRESENT PERFECT ==========
    elif tema == "2. Present Perfect":
        st.header("2. Present Perfect")
        
        st.subheader("Leccion Teorica")
        st.write("""
        El Present Perfect conecta el pasado con el presente.
        
        **Estructura:**
        have/has + past participle (verbo en participio pasado)
        
        **Usos principales:**
        
        1. Experiencias pasadas sin tiempo especifico:
           - I have visited Paris. (He visitado Paris - no importa cuando)
           - She has eaten sushi. (Ella ha comido sushi)
        
        2. Acciones que comenzaron en el pasado y continuan en el presente:
           - I have lived here for 5 years. (Vivo aqui desde hace 5 años)
           - She has worked here since 2020. (Ella trabaja aqui desde 2020)
        
        3. Acciones pasadas con resultados en el presente:
           - I have lost my keys. (No puedo encontrar mis llaves ahora)
           - She has finished her homework. (Ahora puede descansar)
        
        **Palabras clave:**
        - For + periodo de tiempo (for 2 years, for a long time)
        - Since + punto de inicio (since Monday, since 2010)
        - Ever (alguna vez) - en preguntas
        - Never (nunca) - en negativas
        - Just (acabar de) - acciones recientes
        - Already (ya) - acciones completadas
        - Yet (todavia) - en preguntas y negativas
        """)
        
        st.subheader("Ejemplos Practicos")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Con for y since:")
            st.write("- I have studied English for 3 years.")
            st.write("- She has been a teacher since 2015.")
            st.write("- They have lived here for a decade.")
        with col2:
            st.write("Con ever y never:")
            st.write("- Have you ever been to London?")
            st.write("- I have never tried caviar.")
            st.write("- This is the best pizza I have ever eaten.")
        
        st.subheader("Ejercicio de Practica")
        st.write("Completa con 'for' o 'since':")
        
        ejercicios_fs = [
            ("I have lived in this city ________ 2015.", "since"),
            ("She has studied English ________ three years.", "for"),
            ("We have been friends ________ we were children.", "since"),
            ("He has worked here ________ five months.", "for")
        ]
        
        respuestas_fs = 0
        for i, (frase, correcta) in enumerate(ejercicios_fs):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(frase)
            with col2:
                user_answer = st.text_input("", key=f"fs_{i}", label_visibility="collapsed")
                if user_answer:
                    if user_answer.lower().strip() == correcta:
                        respuestas_fs += 1
                        st.success("Correcto")
                    else:
                        st.error(f"Incorrecto. Respuesta: {correcta}")
        
        if st.button("Completar Leccion 2"):
            if respuestas_fs >= 3:
                st.session_state.completed_lessons_int.add("Present Perfect")
                st.success("Felicitaciones. Has completado la leccion 2.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 3. FUTURE FORMS ==========
    elif tema == "3. Future Forms":
        st.header("3. Future Forms: Will vs Going to")
        
        st.subheader("Leccion Teorica")
        st.write("""
        En ingles hay dos formas principales de hablar del futuro: 'will' y 'going to'.
        
        **WILL (futuro simple):**
        - Estructura: sujeto + will + verbo infinitivo
        
        Usos de 'will':
        1. Decisiones espontaneas (en el momento de hablar):
           - The phone is ringing. I will answer it.
           - I'm tired. I will go to bed.
        
        2. Predicciones sin evidencia (opiniones personales):
           - I think it will rain tomorrow.
           - She will probably arrive late.
        
        3. Promesas y ofrecimientos:
           - I will help you with your homework.
           - I will never lie to you.
        
        **GOING TO:**
        - Estructura: sujeto + am/is/are + going to + verbo infinitivo
        
        Usos de 'going to':
        1. Planes y intenciones (decisiones ya tomadas):
           - I am going to study medicine next year.
           - She is going to travel to Japan.
        
        2. Predicciones con evidencia visible:
           - Look at those dark clouds. It is going to rain.
           - He is driving too fast. He is going to crash.
        
        **Diferencia clave:**
        - Will: decision en el momento, opinion
        - Going to: plan ya pensado, evidencia visible
        """)
        
        st.subheader("Ejemplos Practicos")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Will (decisiones espontaneas):")
            st.write("- I will have coffee, please.")
            st.write("- Don't worry. I will pay.")
            st.write("- We will see what happens.")
        with col2:
            st.write("Going to (planes):")
            st.write("- She is going to buy a car.")
            st.write("- They are going to get married.")
            st.write("- I am going to clean the house.")
        
        st.subheader("Ejercicio de Practica")
        st.write("Elige 'will' o 'going to' para cada situacion:")
        
        casos = [
            ("Las nubes estan muy oscuras. Creo que ________ (rain)", "is going to rain"),
            ("El telefono esta sonando. Yo ________ (answer) it", "will answer"),
            ("He estudiado mucho. ________ (pass) the exam", "am going to pass"),
            ("Prometo que ________ (be) honest contigo", "will be")
        ]
        
        respuestas_futuro = 0
        for i, (situacion, correcta) in enumerate(casos):
            st.write(situacion)
            user_answer = st.text_input(f"Tu respuesta {i+1}:", key=f"future_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_futuro += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 3"):
            if respuestas_futuro >= 3:
                st.session_state.completed_lessons_int.add("Future Forms")
                st.success("Felicitaciones. Has completado la leccion 3.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 4. MODAL VERBS ==========
    elif tema == "4. Modal Verbs":
        st.header("4. Modal Verbs")
        
        st.subheader("Leccion Teorica")
        st.write("""
        Los verbos modales son verbos auxiliares que expresan habilidad, permiso, obligacion, posibilidad, etc.
        
        **CAN:**
        - Habilidad: I can swim. (Se nadar)
        - Permiso informal: You can go now. (Puedes irte ahora)
        - Posibilidad: It can be dangerous. (Puede ser peligroso)
        
        **COULD:**
        - Habilidad pasada: I could run fast when I was young. (Podia correr rapido)
        - Permiso formal: Could I use your phone? (Podria usar su telefono)
        - Posibilidad: It could rain later. (Podria llover mas tarde)
        
        **SHOULD:**
        - Consejo y recomendacion: You should exercise more. (Deberias hacer mas ejercicio)
        - Obligacion moral: We should help others. (Deberiamos ayudar a otros)
        
        **MUST:**
        - Obligacion fuerte: You must wear a seatbelt. (Debes usar cinturon)
        - Prohibicion (must not): You must not smoke here. (No debes fumar aqui)
        - Conclusion logica: She must be tired. (Debe estar cansada)
        
        **Reglas importantes:**
        - Los modales no cambian con la persona (no se añade 's')
        - Van seguidos de un verbo en infinitivo sin 'to'
        - La negacion se forma con 'not'
        """)
        
        st.subheader("Tabla Resumen")
        st.markdown("""
        | Modal | Uso principal | Ejemplo |
        |-------|---------------|---------|
        | Can | Habilidad, permiso | I can speak English |
        | Could | Habilidad pasada, permiso formal | Could you help me? |
        | Should | Consejo | You should rest |
        | Must | Obligacion fuerte | You must study |
        """)
        
        st.subheader("Ejercicio de Practica")
        st.write("Completa con el modal correcto (can, could, should, must):")
        
        ejercicios_modal = [
            ("You ________ eat more vegetables. It's good for your health.", "should"),
            ("I ________ swim when I was five years old.", "could"),
            ("You ________ drive without a license. It's illegal.", "must not"),
            ("________ you help me with this box, please?", "could")
        ]
        
        respuestas_modal = 0
        for i, (frase, correcta) in enumerate(ejercicios_modal):
            st.write(frase)
            user_answer = st.text_input(f"Tu respuesta {i+1}:", key=f"modal_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_modal += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 4"):
            if respuestas_modal >= 3:
                st.session_state.completed_lessons_int.add("Modal Verbs")
                st.success("Felicitaciones. Has completado la leccion 4.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 5. COMPARATIVES AND SUPERLATIVES ==========
    elif tema == "5. Comparatives and Superlatives":
        st.header("5. Comparatives and Superlatives")
        
        st.subheader("Leccion Teorica")
        st.write("""
        Los comparativos y superlativos se usan para comparar personas, objetos o lugares.
        
        **COMPARATIVOS:**
        Se usan para comparar dos elementos.
        
        Reglas:
        1. Adjetivos cortos (1 silaba): se añade '-er'
           - tall -> taller
           - fast -> faster
           - small -> smaller
        
        2. Adjetivos de 2 silabas terminados en 'y': se cambia 'y' por 'ier'
           - happy -> happier
           - easy -> easier
        
        3. Adjetivos largos (2+ silabas): se usa 'more + adjetivo'
           - interesting -> more interesting
           - beautiful -> more beautiful
        
        4. Adjetivos irregulares:
           - good -> better
           - bad -> worse
           - far -> farther/further
        
        **SUPERLATIVOS:**
        Se usan para comparar un elemento con un grupo (el mas...).
        
        Reglas:
        1. Adjetivos cortos: se añade 'the + adjetivo + -est'
           - the tallest, the fastest, the smallest
        
        2. Adjetivos de 2 silabas terminados en 'y': the + adjetivo (y->iest)
           - the happiest, the easiest
        
        3. Adjetivos largos: the most + adjetivo
           - the most interesting, the most beautiful
        
        4. Irregulares:
           - good -> the best
           - bad -> the worst
        """)
        
        st.subheader("Tabla de Reglas")
        st.markdown("""
        | Tipo de adjetivo | Comparativo | Superlativo |
        |-----------------|-------------|--------------|
        | Corto: tall | taller | the tallest |
        | Corto: big | bigger (dobla consonante) | the biggest |
        | Termina en y: happy | happier | the happiest |
        | Largo: expensive | more expensive | the most expensive |
        | Irregular: good | better | the best |
        """)
        
        st.subheader("Ejercicio de Practica")
        st.write("Completa con la forma comparativa o superlativa correcta:")
        
        ejercicios_comp = [
            ("This book is ________ (interesting) than the movie.", "more interesting"),
            ("Mount Everest is ________ (high) mountain in the world.", "the highest"),
            ("My sister is ________ (young) than me.", "younger"),
            ("This is ________ (good) restaurant in the city.", "the best")
        ]
        
        respuestas_comp = 0
        for i, (frase, correcta) in enumerate(ejercicios_comp):
            st.write(frase)
            user_answer = st.text_input(f"Tu respuesta {i+1}:", key=f"comp_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_comp += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 5"):
            if respuestas_comp >= 3:
                st.session_state.completed_lessons_int.add("Comparatives and Superlatives")
                st.success("Felicitaciones. Has completado la leccion 5.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 6. CONDITIONALS TYPE 0 AND 1 ==========
    elif tema == "6. Conditionals Type 0 and 1":
        st.header("6. Conditionals Type 0 and 1")
        
        st.subheader("Leccion Teorica")
        st.write("""
        Los condicionales expresan situaciones que dependen de una condicion.
        
        **ZERO CONDITIONAL (Condicional Cero):**
        - Se usa para hechos generales y verdades universales
        - Estructura: If + present simple, present simple
        - Ejemplo: If you heat water to 100°C, it boils.
        - Tambien se puede usar 'when' en lugar de 'if'
        - Traduccion: Siempre que... entonces...
        
        **FIRST CONDITIONAL (Primer Condicional):**
        - Se usa para situaciones reales o posibles en el futuro
        - Estructura: If + present simple, will + infinitivo
        - Ejemplo: If it rains tomorrow, we will stay at home.
        - Tambien se puede usar: unless (a menos que), as soon as (tan pronto como)
        
        **Palabras clave para el First Conditional:**
        - If (si)
        - Unless (a menos que)
        - As soon as (tan pronto como)
        - When (cuando)
        """)
        
        st.subheader("Ejemplos Comparativos")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Zero Conditional:")
            st.write("- If you freeze water, it becomes ice.")
            st.write("- If you mix blue and yellow, you get green.")
            st.write("- When you exercise, you feel better.")
        with col2:
            st.write("First Conditional:")
            st.write("- If you study, you will pass.")
            st.write("- If she calls, I will tell her.")
            st.write("- We will go if we have time.")
        
        st.subheader("Ejercicio de Practica")
        st.write("Completa las oraciones condicionales:")
        
        ejercicios_cond = [
            ("If you ________ (heat) water to 100°C, it ________ (boil).", "heat, boils"),
            ("If it ________ (rain) tomorrow, we ________ (stay) at home.", "rains, will stay"),
            ("If you ________ (mix) red and white, you ________ (get) pink.", "mix, get"),
            ("If she ________ (study) hard, she ________ (pass) the exam.", "studies, will pass")
        ]
        
        respuestas_cond = 0
        for i, (frase, correcta) in enumerate(ejercicios_cond):
            st.write(frase)
            user_answer = st.text_input(f"Tu respuesta {i+1} (dos verbos separados por coma):", key=f"cond_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_cond += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 6"):
            if respuestas_cond >= 3:
                st.session_state.completed_lessons_int.add("Conditionals Type 0 and 1")
                st.success("Felicitaciones. Has completado la leccion 6.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 7. PASSIVE VOICE ==========
    elif tema == "7. Passive Voice (Present and Past)":
        st.header("7. Passive Voice (Present and Past)")
        
        st.subheader("Leccion Teorica")
        st.write("""
        La voz pasiva enfatiza la accion y no quien la realiza.
        
        **Estructura de la voz pasiva:**
        sujeto + verbo to be + past participle + (by + agente)
        
        **VOZ ACTIVA vs VOZ PASIVA:**
        
        Activa: Someone cleans the office every day.
        (Alguien limpia la oficina todos los dias - enfasis en quien limpia)
        
        Pasiva: The office is cleaned every day.
        (La oficina es limpiada todos los dias - enfasis en la accion)
        
        **Presente Pasivo:**
        am/is/are + past participle
        - English is spoken in many countries.
        - The letters are sent every morning.
        - I am invited to the party.
        
        **Pasado Pasivo:**
        was/were + past participle
        - The Mona Lisa was painted by Da Vinci.
        - The windows were broken yesterday.
        - The movie was made in 1999.
        
        **Cuando usar la voz pasiva:**
        1. Cuando no sabemos quien realiza la accion
        2. Cuando la accion es mas importante que quien la realiza
        3. En textos formales y cientificos
        """)
        
        st.subheader("Transformaciones Ejemplo")
        st.markdown("""
        Activa -> Pasiva
        
        1. Someone stole my car. -> My car was stolen.
        2. They build houses here. -> Houses are built here.
        3. Leonardo painted the Mona Lisa. -> The Mona Lisa was painted by Leonardo.
        """)
        
        st.subheader("Ejercicio de Practica")
        st.write("Transforma las siguientes oraciones a voz pasiva:")
        
        ejercicios_pass = [
            ("Someone cleans the office every day.", "the office is cleaned every day"),
            ("Leonardo da Vinci painted the Mona Lisa.", "the mona lisa was painted by leonardo da vinci"),
            ("People speak Spanish in many countries.", "spanish is spoken in many countries"),
            ("A dog bit my brother.", "my brother was bitten by a dog")
        ]
        
        respuestas_pass = 0
        for i, (activa, correcta) in enumerate(ejercicios_pass):
            st.write(f"Activa: {activa}")
            user_answer = st.text_input(f"Tu respuesta pasiva {i+1}:", key=f"pass_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_pass += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 7"):
            if respuestas_pass >= 3:
                st.session_state.completed_lessons_int.add("Passive Voice (Present and Past)")
                st.success("Felicitaciones. Has completado la leccion 7.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 8. REPORTED SPEECH BASIC ==========
    elif tema == "8. Reported Speech (Basic)":
        st.header("8. Reported Speech (Basic)")
        
        st.subheader("Leccion Teorica")
        st.write("""
        El Reported Speech (estilo indirecto) se usa para reportar lo que alguien dijo.
        
        **Cambios principales:**
        
        1. Cambio de tiempos verbales:
           - Present Simple -> Past Simple
           - Present Continuous -> Past Continuous
           - Present Perfect -> Past Perfect
           - will -> would
           - can -> could
           - am/is/are -> was/were
        
        2. Cambio de pronombres y posesivos:
           - I -> he/she
           - my -> his/her
           - we -> they
           - our -> their
        
        3. Cambio de expresiones de tiempo y lugar:
           - now -> then
           - today -> that day
           - here -> there
           - tomorrow -> the next day
           - yesterday -> the day before
           - this -> that
        
        **Verbos introductorios:**
        - say + that (decir que)
        - tell + persona + that (decir a alguien que)
        """)
        
        st.subheader("Tabla de Transformaciones")
        st.markdown("""
        | Direct Speech | Reported Speech |
        |---------------|------------------|
        | "I am happy" | She said (that) she was happy |
        | "I will call you" | He said he would call me |
        | "I live here" | She said she lived there |
        | "We are working" | They said they were working |
        """)
        
        st.subheader("Ejercicio de Practica")
        st.write("Transforma las siguientes oraciones a Reported Speech:")
        
        ejercicios_rep = [
            ("'I am tired,' she said.", "she said she was tired"),
            ("'I will help you,' he told me.", "he told me he would help me"),
            ("'We live in London,' they said.", "they said they lived in london")
        ]
        
        respuestas_rep = 0
        for i, (directa, correcta) in enumerate(ejercicios_rep):
            st.write(f"Directa: {directa}")
            user_answer = st.text_input(f"Tu respuesta indirecta {i+1}:", key=f"rep_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_rep += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 8"):
            if respuestas_rep >= 2:
                st.session_state.completed_lessons_int.add("Reported Speech (Basic)")
                st.success("Felicitaciones. Has completado la leccion 8.")
            else:
                st.warning("Responde correctamente al menos 2 ejercicios para completar la leccion.")

    # ========== 9. PHRASAL VERBS ==========
    elif tema == "9. Phrasal Verbs (Common)":
        st.header("9. Common Phrasal Verbs")
        
        st.subheader("Leccion Teorica")
        st.write("""
        Los phrasal verbs son verbos compuestos por un verbo + una preposicion o adverbio.
        Su significado suele ser diferente al verbo original.
        
        **LOS MAS COMUNES:**
        
        **LOOK + preposicion:**
        - look up: buscar informacion (en diccionario/internet)
        - look for: buscar algo perdido
        - look after: cuidar
        - look forward to: esperar con ilusion
        
        **TURN + preposicion:**
        - turn on: encender
        - turn off: apagar
        - turn up: subir volumen
        - turn down: bajar volumen / rechazar
        
        **GET + preposicion:**
        - get up: levantarse
        - get along with: llevarse bien con
        - get over: superar
        
        **GIVE + preposicion:**
        - give up: rendirse
        - give back: devolver
        
        **TAKE + preposicion:**
        - take off: despegar / quitarse ropa
        - take care of: cuidar de
        """)
        
        st.subheader("Lista de Phrasal Verbs para A2")
        st.markdown("""
        | Phrasal Verb | Significado | Ejemplo |
        |--------------|-------------|---------|
        | get up | levantarse | I get up at 7 AM |
        | turn on | encender | Turn on the light |
        | turn off | apagar | Turn off the TV |
        | look up | buscar | Look up the word |
        | give up | rendirse | Don't give up |
        | look for | buscar | I'm looking for my keys |
        | run out of | quedarse sin | We ran out of milk |
        | find out | descubrir | I found out the truth |
        """)
        
        st.subheader("Ejercicio de Practica")
        st.write("Completa las siguientes oraciones con el phrasal verb correcto:")
        
        ejercicios_pv = [
            ("Please ________ the TV. I want to watch the news.", "turn on"),
            ("I need to ________ this word in the dictionary.", "look up"),
            ("Don't ________. Keep trying.", "give up"),
            ("I usually ________ at 6 AM.", "get up")
        ]
        
        respuestas_pv = 0
        for i, (frase, correcta) in enumerate(ejercicios_pv):
            st.write(frase)
            user_answer = st.text_input(f"Tu respuesta {i+1}:", key=f"pv_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_pv += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        if st.button("Completar Leccion 9"):
            if respuestas_pv >= 3:
                st.session_state.completed_lessons_int.add("Phrasal Verbs (Common)")
                st.success("Felicitaciones. Has completado la leccion 9.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # ========== 10. CONNECTORS AND LINKING WORDS ==========
    elif tema == "10. Connectors and Linking Words":
        st.header("10. Connectors and Linking Words")
        
        st.subheader("Leccion Teorica")
        st.write("""
        Los conectores son palabras que unen ideas y mejoran la fluidez del texto.
        
        **TIPOS DE CONECTORES:**
        
        **1. SUMA (anadir informacion):**
        - and (y)
        - also (tambien)
        - in addition (ademas)
        - Example: She likes coffee and tea.
        
        **2. CONTRASTE (oponer ideas):**
        - but (pero)
        - however (sin embargo)
        - although (aunque)
        - Example: I like coffee, but I don't like tea.
        
        **3. CAUSA (explicar razon):**
        - because (porque)
        - since (ya que)
        - as (como/puesto que)
        - Example: I stayed home because it was raining.
        
        **4. CONSECUENCIA (mostrar resultado):**
        - so (asi que)
        - therefore (por lo tanto)
        - as a result (como resultado)
        - Example: It was raining, so I stayed home.
        
        **5. ORDEN Y SECUENCIA:**
        - first, second, third (primero, segundo, tercero)
        - then (entonces)
        - finally (finalmente)
        - Example: First, wake up. Then, have breakfast.
        """)
        
        st.subheader("Tabla de Conectores por Funcion")
        st.markdown("""
        | Funcion | Conectores | Ejemplo |
        |---------|------------|---------|
        | Suma | and, also | I like apples and oranges |
        | Contraste | but, although | Although it was cold, we went out |
        | Causa | because, since | I'm happy because I passed |
        | Consecuencia | so, therefore | I studied, so I passed |
        | Secuencia | first, then, finally | First, open the book |
        """)
        
        st.subheader("Ejercicio de Practica")
        st.write("Elige el conector correcto para cada oracion:")
        
        ejercicios_conn = [
            ("I wanted to go to the party, ________ I was too tired.", "but"),
            ("________ it was raining, we went to the beach.", "although"),
            ("She studied hard, ________ she passed the exam.", "so"),
            ("He didn't go to work ________ he was sick.", "because")
        ]
        
        respuestas_conn = 0
        for i, (frase, correcta) in enumerate(ejercicios_conn):
            st.write(frase)
            user_answer = st.text_input(f"Tu respuesta {i+1}:", key=f"conn_{i}")
            if user_answer:
                if user_answer.lower().strip() == correcta:
                    respuestas_conn += 1
                    st.success("Correcto")
                else:
                    st.info(f"Respuesta correcta: {correcta}")
        
        # Ejercicio adicional de escritura
        st.write("---")
        st.write("Ejercicio de escritura: Une estas dos oraciones usando un conector")
        st.write("Oracion 1: Ella estudio mucho")
        st.write("Oracion 2: Aprobo el examen")
        
        user_compose = st.text_input("Tu oracion compuesta:")
        if user_compose:
            correct_options = ["she studied so she passed", "she studied, so she passed", "she passed because she studied"]
            if any(opt in user_compose.lower() for opt in correct_options):
                st.success("Buen trabajo usando conectores")
                respuestas_conn += 1
            else:
                st.info("Ejemplos correctos: 'She studied, so she passed the exam' o 'She passed the exam because she studied'")
        
        if st.button("Completar Leccion 10"):
            if respuestas_conn >= 3:
                st.session_state.completed_lessons_int.add("Connectors and Linking Words")
                st.success("Felicitaciones. Has completado la leccion 10.")
            else:
                st.warning("Responde correctamente al menos 3 ejercicios para completar la leccion.")

    # Mostrar certificado al completar el curso
    if len(st.session_state.completed_lessons_int) == total_lessons:
        st.sidebar.markdown("---")
        st.sidebar.success("Curso completado")
        st.balloons()

# Ejecutar la aplicacion
if __name__ == "__main__":
    app()