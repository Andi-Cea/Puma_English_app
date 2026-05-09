import streamlit as st

def app():
    # Configuración de la página
    st.set_page_config(
        page_title="Curso de Inglés Nivel A1", 
        page_icon="🇬🇧",
        layout="wide"
    )
    
    # Título principal
    st.title("Curso de Inglés Nivel A1")
    st.markdown("### Para estudiantes de habla hispana - Nivel Elemental")
    st.markdown("---")

    # ======================== SECCION 1: PAST SIMPLE ========================
    st.markdown("## 1. Past Simple - Verbos Regulares e Irregulares")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Verbos Regulares (terminacion -ed)")
        st.markdown("""
        | Regla | Ejemplo |
        |-------|---------|
        | +ed | work → worked |
        | +d (termina en e) | live → lived |
        | y → ied (consonante+y) | study → studied |
        | Doble consonante + ed | stop → stopped |
        """)
    
    with col2:
        st.markdown("### Verbos Irregulares Comunes")
        st.markdown("""
        | Presente | Pasado | Español |
        |----------|--------|---------|
        | go | went | ir |
        | eat | ate | comer |
        | see | saw | ver |
        | buy | bought | comprar |
        | drink | drank | beber |
        | write | wrote | escribir |
        """)
    
    st.markdown("### Estructura del Past Simple")
    st.markdown("""
    **Afirmativo:** Sujeto + verbo en pasado
    - I **visited** my grandmother yesterday.
    - She **went** to the cinema last night.
    
    **Negativo:** Sujeto + **didn't** + verbo base
    - I **didn't visit** my grandmother.
    - She **didn't go** to the cinema.
    
    **Pregunta:** **Did** + sujeto + verbo base?
    - **Did you visit** your grandmother?
    - **Did she go** to the cinema?
    """)
    
    st.markdown("### Expresiones de tiempo en pasado")
    st.info("""
    yesterday (ayer) | last night (anoche) | last week (la semana pasada)
    last month (el mes pasado) | last year (el año pasado) | in 2010 (en 2010)
    two days ago (hace dos dias) | when I was a child (cuando era niño)
    """)
    
    st.markdown("---")

    # ======================== SECCION 2: PAST CONTINUOUS ========================
    st.markdown("## 2. Past Continuous (Pasado Continuo)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Estructura")
        st.markdown("""
        **Afirmativo:** Sujeto + **was/were** + verbo-ing
        - I **was watching** TV at 8pm.
        - They **were playing** football.
        
        **Negativo:** Sujeto + **wasn't/weren't** + verbo-ing
        - I **wasn't sleeping**.
        - They **weren't working**.
        """)
    
    with col2:
        st.markdown("### Usos principales")
        st.markdown("""
        1. **Acciones en progreso** en un momento especifico del pasado:
           - At 7am, I **was having** breakfast.
        
        2. **Dos acciones simultaneas**:
           - While I **was studying**, my brother **was playing**.
        
        3. **Accion interrumpida** (con Past Simple):
           - I **was walking** when I **saw** an accident.
        """)
    
    st.markdown("### Past Simple vs Past Continuous")
    st.markdown("""
    | Past Simple | Past Continuous |
    |-------------|-----------------|
    | Accion completada | Accion en progreso |
    | She **arrived** at 8pm. | She **was arriving** when I called. |
    | He **finished** his work. | He **was finishing** his work. |
    """)
    
    st.markdown("---")

    # ======================== SECCION 3: PRESENT PERFECT ========================
    st.markdown("## 3. Present Perfect")
    
    st.markdown("### Estructura: Sujeto + have/has + past participle")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Usos principales")
        st.markdown("""
        1. **Experiencias pasadas** (sin tiempo especifico):
           - I **have visited** Paris.
           - She **has never eaten** sushi.
        
        2. **Acciones que empezaron en el pasado y continuan**:
           - I **have lived** here for 5 years.
           - She **has worked** here since 2020.
        
        3. **Acciones recientes** (con just/already/yet):
           - I **have just finished** my homework.
        """)
    
    with col2:
        st.markdown("### Palabras clave")
        st.markdown("""
        - **Ever** (alguna vez) - preguntas
        - **Never** (nunca) - negativas
        - **Just** (acabar de)
        - **Already** (ya)
        - **Yet** (aun/todavia) - negativas y preguntas
        - **For** + periodo de tiempo
        - **Since** + punto de inicio
        """)
    
    st.markdown("### For vs Since")
    st.markdown("""
    | For (duracion) | Since (punto de inicio) |
    |----------------|-------------------------|
    | for three years | since 2020 |
    | for two hours | since Monday |
    | for a long time | since I was a child |
    """)
    
    st.markdown("---")

    # ======================== SECCION 4: FUTURE FORMS ========================
    st.markdown("## 4. Future Forms (Will vs Going to)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Will (decisiones espontaneas)")
        st.markdown("""
        **Estructura:** Sujeto + will + verbo base
        
        - **Decisiones del momento:**
          \"The phone is ringing.\" \"I **will answer** it.\"
        
        - **Predicciones sin evidencia:**
          I think it **will rain** tomorrow.
        
        - **Promesas y ofrecimientos:**
          I **will help** you with your homework.
        """)
    
    with col2:
        st.markdown("### Going to (planes y predicciones con evidencia)")
        st.markdown("""
        **Estructura:** Sujeto + am/is/are + going to + verbo base
        
        - **Planes futuros:**
          I **am going to travel** to London next month.
        
        - **Predicciones con evidencia:**
          Look at those clouds! It **is going to rain**.
        
        - **Intenciones:**
          She **is going to study** medicine.
        """)
    
    st.markdown("### Present Continuous para futuro (arrangements)")
    st.markdown("""
    Para planes fijos y acuerdos:
    - I **am meeting** my friends tomorrow at 7pm.
    - She **is flying** to New York next week.
    """)
    
    st.markdown("---")

    # ======================== SECCION 5: MODAL VERBS ========================
    st.markdown("## 5. Modal Verbs (Can, Could, Should, Must, Have to)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Can / Could")
        st.markdown("""
        **Can** (habilidad/permiso):
        - I **can** swim. (habilidad)
        - You **can** leave early. (permiso)
        
        **Could** (pasado de can / peticion formal):
        - I **could** run fast when I was young.
        - **Could** you help me, please?
        """)
        
        st.markdown("### Should (consejo)")
        st.markdown("""
        - You **should** eat more vegetables.
        - You **shouldn't** smoke.
        - **Should** I call the doctor?
        """)
    
    with col2:
        st.markdown("### Must / Have to (obligacion)")
        st.markdown("""
        **Must** (obligacion interna/reglas):
        - I **must** study for the exam.
        - You **mustn't** smoke here.
        
        **Have to** (obligacion externa):
        - I **have to** work on Sunday.
        - She **has to** wear a uniform.
        
        **Diferencia:** Must = del hablante | Have to = por circunstancias
        """)
    
    st.markdown("---")

    # ======================== SECCION 6: COMPARATIVES AND SUPERLATIVES ========================
    st.markdown("## 6. Comparatives and Superlatives")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Comparativos")
        st.markdown("""
        **Adjetivos cortos (1-2 silabas) + er + than:**
        - tall → taller than
        - big → bigger than (doble consonante)
        - happy → happier than (y → ier)
        
        **Adjetivos largos: more + adjetivo + than:**
        - expensive → more expensive than
        - beautiful → more beautiful than
        
        **Irregulares:**
        - good → better than
        - bad → worse than
        - far → farther than
        """)
    
    with col2:
        st.markdown("### Superlativos")
        st.markdown("""
        **Adjetivos cortos: the + adjetivo + est:**
        - tall → the tallest
        - big → the biggest
        - happy → the happiest
        
        **Adjetivos largos: the most + adjetivo:**
        - expensive → the most expensive
        - beautiful → the most beautiful
        
        **Irregulares:**
        - good → the best
        - bad → the worst
        - far → the farthest
        """)
    
    st.markdown("### Ejemplos")
    st.markdown("""
    - This book is **better than** that one. (comparativo)
    - She is **the best** student in class. (superlativo)
    - My car is **more expensive than** yours.
    - This is **the most delicious** cake I've ever eaten.
    """)
    
    st.markdown("---")

    # ======================== SECCION 7: CONDITIONALS TYPE 0 AND 1 ========================
    st.markdown("## 7. Conditionals Type 0 and 1")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Zero Conditional (hechos generales)")
        st.markdown("""
        **Estructura:** If + present simple, present simple
        
        **Uso:** Verdades universales y hechos cientificos
        
        **Ejemplos:**
        - If you **heat** water to 100°C, it **boils**.
        - If it **rains**, the grass **gets** wet.
        - If you **mix** red and blue, you **get** purple.
        """)
    
    with col2:
        st.markdown("### First Conditional (posibilidades reales)")
        st.markdown("""
        **Estructura:** If + present simple, will + infinitivo
        
        **Uso:** Situaciones reales y probables en el futuro
        
        **Ejemplos:**
        - If it **rains** tomorrow, I **will stay** home.
        - If you **study** hard, you **will pass** the exam.
        - If she **doesn't hurry**, she **will miss** the bus.
        """)
    
    st.markdown("### Nota importante")
    st.warning("""
    En el First Conditional, la palabra 'unless' significa 'if not':
    - Unless you study = If you don't study
    - I won't pass unless I study hard.
    """)
    
    st.markdown("---")

    # ======================== SECCION 8: PASSIVE VOICE ========================
    st.markdown("## 8. Passive Voice (Presente y Pasado)")
    
    st.markdown("### Estructura: Sujeto + to be + past participle")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Presente Pasivo (am/is/are + past participle)")
        st.markdown("""
        **Activo:** Someone cleans the office.
        **Pasivo:** The office **is cleaned**.
        
        **Activo:** They make cars here.
        **Pasivo:** Cars **are made** here.
        
        **Activo:** She writes the report.
        **Pasivo:** The report **is written** by her.
        """)
    
    with col2:
        st.markdown("### Pasado Pasivo (was/were + past participle)")
        st.markdown("""
        **Activo:** Someone painted the house.
        **Pasivo:** The house **was painted**.
        
        **Activo:** They built this bridge in 1990.
        **Pasivo:** This bridge **was built** in 1990.
        
        **Activo:** Leonardo painted the Mona Lisa.
        **Pasivo:** The Mona Lisa **was painted** by Leonardo.
        """)
    
    st.markdown("### ¿Cuando usar la voz pasiva?")
    st.markdown("""
    - Cuando la accion es mas importante que quien la realiza
    - Cuando no sabemos quien realizo la accion
    - En contextos formales y academicos
    """)
    
    st.markdown("---")

    # ======================== SECCION 9: REPORTED SPEECH ========================
    st.markdown("## 9. Reported Speech (Estilo Indirecto)")
    
    st.markdown("### Cambios importantes al reportar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Tiempos verbales")
        st.markdown("""
        | Directo | Indirecto |
        |---------|------------|
        | Present Simple | Past Simple |
        | \"I **am** tired\" | He said he **was** tired |
        | Present Continuous | Past Continuous |
        | \"I **am watching** TV\" | He said he **was watching** TV |
        | will | would |
        | \"I **will** call\" | He said he **would** call |
        """)
    
    with col2:
        st.markdown("### Palabras que cambian")
        st.markdown("""
        | Directo | Indirecto |
        |---------|------------|
        | today | that day |
        | tomorrow | the next day |
        | yesterday | the day before |
        | now | then |
        | here | there |
        | this | that |
        """)
    
    st.markdown("### Ejemplos")
    st.markdown("""
    **Directo:** \"I **am hungry**,\" she said.
    **Indirecto:** She said (that) she **was hungry**.
    
    **Directo:** \"I **will call you tomorrow**,\" he told me.
    **Indirecto:** He told me (that) he **would call me the next day**.
    
    **Directo:** \"I **don't like** coffee,\" he said.
    **Indirecto:** He said (that) he **didn't like** coffee.
    """)
    
    st.markdown("---")

    # ======================== SECCION 10: PHRASAL VERBS ========================
    st.markdown("## 10. Common Phrasal Verbs")
    
    st.markdown("### Phrasal Verbs mas usados en nivel A2")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **get up** - levantarse
        - I **get up** at 7am.
        
        **wake up** - despertarse
        - She **wakes up** early.
        
        **turn on** - encender
        - **Turn on** the TV, please.
        
        **turn off** - apagar
        - **Turn off** the lights.
        
        **look for** - buscar
        - I'm **looking for** my keys.
        
        **look at** - mirar
        - **Look at** this picture!
        """)
    
    with col2:
        st.markdown("""
        **give up** - rendirse
        - Never **give up**!
        
        **run out of** - quedarse sin
        - We **ran out of** milk.
        
        **find out** - descubrir
        - I need to **find out** the truth.
        
        **put on** - ponerse (ropa)
        - **Put on** your coat.
        
        **take off** - quitarse (ropa)
        - **Take off** your shoes.
        
        **sit down** - sentarse
        - Please **sit down**.
        """)
    
    st.markdown("### Importante sobre Phrasal Verbs")
    st.warning("""
    - Algunos phrasal verbs son **separables** (turn the TV on = turn on the TV)
    - Otros son **inseparables** (look for my keys = no se puede decir look my keys for)
    - Con pronombres, SIEMPRE se separan: turn **it** on, not turn on it
    """)
    
    st.markdown("---")

    # ======================== SECCION 11: CONNECTORS ========================
    st.markdown("## 11. Connectors and Linking Words")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Conectores de adicion")
        st.markdown("""
        - **and** - y
        - **also** - tambien
        - **too** - tambien (final de oracion)
        
        **Ejemplos:**
        - I like coffee **and** tea.
        - She speaks English **also** French.
        - I love pizza, **too**.
        """)
        
        st.markdown("### Conectores de contraste")
        st.markdown("""
        - **but** - pero
        - **however** - sin embargo
        - **although** - aunque
        
        **Ejemplos:**
        - I like coffee **but** I don't drink it.
        - It was expensive **however** I bought it.
        - **Although** it rained, we went out.
        """)
    
    with col2:
        st.markdown("### Conectores de causa y consecuencia")
        st.markdown("""
        - **because** - porque
        - **so** - asi que
        - **therefore** - por lo tanto
        
        **Ejemplos:**
        - I'm tired **because** I worked hard.
        - It was late, **so** I went home.
        - She studied a lot **therefore** she passed.
        """)
        
        st.markdown("### Conectores de tiempo")
        st.markdown("""
        - **then** - entonces/luego
        - **after that** - despues de eso
        - **finally** - finalmente
        
        **Ejemplos:**
        - I woke up, **then** I had breakfast.
        - I finished work **after that** I went home.
        - **Finally**, we arrived.
        """)
    
    st.markdown("---")

    # ======================== SECCION 12: EJERCICIO PRACTICO ========================
    st.markdown("## Ejercicio de Practica - Nivel A2")
    st.markdown("Completa las siguientes oraciones:")
    
    with st.form(key="quiz_form_a2"):
        st.markdown("**1. Completa con el verbo en pasado simple:** She ________ (go) to the supermarket yesterday.")
        q1 = st.text_input("Respuesta 1:", key="a2_q1")
        
        st.markdown("**2. Past Continuous:** While I ________ (study), the phone rang.")
        q2 = st.text_input("Respuesta 2:", key="a2_q2")
        
        st.markdown("**3. Present Perfect:** I ________ (never/eat) sushi.")
        q3 = st.text_input("Respuesta 3:", key="a2_q3")
        
        st.markdown("**4. Will o Going to?** Look at those clouds! It ________ (rain).")
        q4 = st.text_input("Respuesta 4:", key="a2_q4")
        
        st.markdown("**5. Modal verb:** You ________ (consejo) exercise more.")
        q5 = st.text_input("Respuesta 5:", key="a2_q5")
        
        st.markdown("**6. Comparative:** This book is ________ (interesting) than the movie.")
        q6 = st.text_input("Respuesta 6:", key="a2_q6")
        
        st.markdown("**7. First Conditional:** If she ________ (study), she will pass.")
        q7 = st.text_input("Respuesta 7:", key="a2_q7")
        
        st.markdown("**8. Passive Voice:** The Mona Lisa ________ (paint) by Da Vinci.")
        q8 = st.text_input("Respuesta 8:", key="a2_q8")
        
        st.markdown("**9. Reported Speech:** 'I am happy,' she said. → She said that she ________ happy.")
        q9 = st.text_input("Respuesta 9:", key="a2_q9")
        
        st.markdown("**10. Phrasal Verb:** Please ________ the TV (encender).")
        q10 = st.text_input("Respuesta 10:", key="a2_q10")
        
        submit = st.form_submit_button("Verificar respuestas")
        
        if submit:
            score = 0
            total = 10
            st.markdown("---")
            st.markdown("### Resultados:")
            
            # Respuestas correctas
            if q1.lower().strip() == "went":
                score += 1
                st.success("1. Correcto - 'went'")
            else:
                st.error("1. Incorrecto - La respuesta es 'went'")
            
            if q2.lower().strip() == "was studying":
                score += 1
                st.success("2. Correcto - 'was studying'")
            else:
                st.error("2. Incorrecto - La respuesta es 'was studying'")
            
            if q3.lower().strip() == "have never eaten":
                score += 1
                st.success("3. Correcto - 'have never eaten'")
            else:
                st.error("3. Incorrecto - La respuesta es 'have never eaten'")
            
            if q4.lower().strip() == "is going to rain":
                score += 1
                st.success("4. Correcto - 'is going to rain'")
            else:
                st.error("4. Incorrecto - La respuesta es 'is going to rain'")
            
            if q5.lower().strip() == "should":
                score += 1
                st.success("5. Correcto - 'should'")
            else:
                st.error("5. Incorrecto - La respuesta es 'should'")
            
            if q6.lower().strip() == "more interesting":
                score += 1
                st.success("6. Correcto - 'more interesting'")
            else:
                st.error("6. Incorrecto - La respuesta es 'more interesting'")
            
            if q7.lower().strip() == "studies":
                score += 1
                st.success("7. Correcto - 'studies'")
            else:
                st.error("7. Incorrecto - La respuesta es 'studies'")
            
            if q8.lower().strip() == "was painted":
                score += 1
                st.success("8. Correcto - 'was painted'")
            else:
                st.error("8. Incorrecto - La respuesta es 'was painted'")
            
            if q9.lower().strip() == "was":
                score += 1
                st.success("9. Correcto - 'was'")
            else:
                st.error("9. Incorrecto - La respuesta es 'was'")
            
            if q10.lower().strip() == "turn on":
                score += 1
                st.success("10. Correcto - 'turn on'")
            else:
                st.error("10. Incorrecto - La respuesta es 'turn on'")
            
            st.markdown(f"### Tu puntuacion: {score}/{total}")
            if score == 10:
                st.balloons()
                st.success("Excelente! Dominas el nivel A2!")
            elif score >= 7:
                st.info("Buen trabajo! Estas en camino a dominar el nivel A2!")
            elif score >= 5:
                st.warning("Bien! Revisa los temas donde tuviste errores.")
            else:
                st.error("Sigue practicando! Revisa la teoria nuevamente.")
    
    st.markdown("---")
    
    # ======================== SECCION 13: RECURSOS ========================
    st.markdown("## Recursos para seguir mejorando")
    st.markdown("""
    ### Diferencias clave A1 vs A2:
    - A1: Frases simples y vocabulario basico
    - A2: Descripciones mas largas y tiempos pasados
    
    ### Temas a practicar para nivel A2:
    - Past Simple vs Past Continuous
    - Present Perfect con for/since
    - Will vs Going to
    - Verbos modales
    - Frases condicionales basicas
    
    ### Canales recomendados para A2:
    - English with Lucy (intermedio)
    - BBC Learning English
    - Learn English with TV Series
    
    ### Tips de estudio:
    - Escribe un diario en ingles usando past tense
    - Mira series con subtitulos en ingles
    - Practica speaking describiendo tus rutinas diarias
    """)
    
    st.markdown("---")
    st.markdown("### Ya has completado el nivel A1? Continúa con A2!")
    st.markdown("*La practica constante te llevará al siguiente nivel. Sigue asi!*")

if __name__ == "__main__":
    app()