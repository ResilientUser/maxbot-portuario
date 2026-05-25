import streamlit as st
from dataclasses import dataclass
from typing import Dict, List


# =============================
# MAXBOT MVP
# Asistente de Desarrollo Profesional Portuario
# =============================

st.set_page_config(
    page_title="MAXBOT | MVP Portuario",
    page_icon="⚓",
    layout="wide",
)


@dataclass
class LearningRoute:
    name: str
    objective: str
    strengths: List[str]
    courses: List[str]
    institutional_gaps: List[str]
    recommendation_reason: str


AREA_OPTIONS = [
    "Operación portuaria",
    "Planeación y evaluación",
    "Administración y finanzas",
    "Dirección / mando",
]

INTEREST_OPTIONS = [
    "Indicadores y desempeño",
    "Toma de decisiones",
    "Normatividad y gestión",
    "Innovación / IA aplicada",
    "No estoy seguro, recomiéndame una ruta",
]

LEVEL_OPTIONS = ["Básico", "Intermedio", "Avanzado"]


COURSE_CATALOG = {
    "Indicadores y desempeño": "KPIs portuarios alineados a UNCTAD + World Bank (CPPI)",
    "Toma de decisiones": "Evaluación de proyectos portuarios y priorización estratégica",
    "Normatividad y gestión": "Marco regulatorio y gestión institucional portuaria",
    "Innovación / IA aplicada": "Aplicaciones prácticas de IA en operación y toma de decisiones portuarias",
    "Operación portuaria": "Indicadores operativos aplicados a muelles, dragado, tiempos y eficiencia",
    "Administración y finanzas": "Presupuesto basado en resultados aplicado a gestión portuaria",
}


def build_route(area: str, interest: str, level: str) -> LearningRoute:
    """Genera una ruta sugerida con lógica simple y explicable."""

    # Ruta por defecto según interés
    primary_course = COURSE_CATALOG.get(interest, COURSE_CATALOG["Indicadores y desempeño"])

    # Lógica por área
    if area == "Operación portuaria":
        strengths = [
            "Enfoque operativo directo",
            "Conocimiento del flujo real del puerto",
            "Capacidad para identificar cuellos de botella",
        ]
        institutional_gaps = [
            "Estandarización de indicadores operativos",
            "Uso consistente de datos para decisiones",
            "Vinculación entre desempeño y formación",
        ]
        secondary_courses = [
            COURSE_CATALOG["Operación portuaria"],
            COURSE_CATALOG["Indicadores y desempeño"],
            COURSE_CATALOG["Innovación / IA aplicada"],
        ]
        route_name = "Ruta Operativa con Enfoque en Desempeño"
        objective = "Fortalecer la capacidad para medir, comparar y mejorar la operación portuaria con base en estándares internacionales."
        recommendation_reason = (
            "Tu perfil operativo sugiere que la mayor oportunidad está en convertir experiencia práctica en decisiones más medibles y comparables."
        )

    elif area == "Planeación y evaluación":
        strengths = [
            "Visión estructurada de proyectos",
            "Capacidad de priorización",
            "Potencial para integrar información en decisiones estratégicas",
        ]
        institutional_gaps = [
            "Trazabilidad de decisiones",
            "Alineación entre proyectos e indicadores",
            "Integración de criterios estratégicos y operativos",
        ]
        secondary_courses = [
            COURSE_CATALOG["Toma de decisiones"],
            COURSE_CATALOG["Indicadores y desempeño"],
            COURSE_CATALOG["Innovación / IA aplicada"],
        ]
        route_name = "Ruta de Planeación Estratégica Portuaria"
        objective = "Mejorar la capacidad para evaluar, priorizar y dar seguimiento a proyectos y decisiones portuarias."
        recommendation_reason = (
            "Tu perfil sugiere alto potencial para traducir datos e indicadores en decisiones institucionales de mayor calidad."
        )

    elif area == "Administración y finanzas":
        strengths = [
            "Control presupuestal y administrativo",
            "Capacidad de estructurar procesos",
            "Visión sobre asignación de recursos",
        ]
        institutional_gaps = [
            "Conexión entre presupuesto y desempeño",
            "Uso de indicadores para seguimiento",
            "Identificación de brechas de capacidades por área",
        ]
        secondary_courses = [
            COURSE_CATALOG["Administración y finanzas"],
            COURSE_CATALOG["Indicadores y desempeño"],
            COURSE_CATALOG["Normatividad y gestión"],
        ]
        route_name = "Ruta de Gestión y Desempeño Institucional"
        objective = "Conectar presupuesto, capacidades e indicadores para fortalecer la gestión institucional del puerto."
        recommendation_reason = (
            "Tu perfil administrativo-financiero encaja con una ruta enfocada en vincular recursos con resultados medibles."
        )

    else:  # Dirección / mando
        strengths = [
            "Visión integral",
            "Capacidad de coordinar áreas",
            "Potencial para impulsar transformación institucional",
        ]
        institutional_gaps = [
            "Trazabilidad de capacidades del personal",
            "Alineación entre capacitación y desempeño",
            "Lectura estratégica de indicadores y riesgos",
        ]
        secondary_courses = [
            COURSE_CATALOG["Indicadores y desempeño"],
            COURSE_CATALOG["Toma de decisiones"],
            COURSE_CATALOG["Innovación / IA aplicada"],
        ]
        route_name = "Ruta Directiva de Decisión Estratégica"
        objective = "Fortalecer la capacidad directiva para tomar decisiones basadas en datos, indicadores y capacidades institucionales."
        recommendation_reason = (
            "Tu posición sugiere que el mayor valor está en usar la capacitación como herramienta de fortalecimiento institucional."
        )

    # Ajuste por interés explícito
    if interest != "No estoy seguro, recomiéndame una ruta":
        if primary_course not in secondary_courses:
            secondary_courses.insert(0, primary_course)
        else:
            # Lo mueve al inicio si ya existe
            secondary_courses = [primary_course] + [c for c in secondary_courses if c != primary_course]

    # Ajuste por nivel
    if level == "Básico":
        objective += " La ruta prioriza fundamentos, lenguaje común y comprensión aplicada."
    elif level == "Intermedio":
        objective += " La ruta prioriza integración de herramientas, indicadores y aplicaciones prácticas."
    else:
        objective += " La ruta prioriza diseño estratégico, comparación internacional y mejora institucional."

    # Mantener 3 cursos máximo
    courses = secondary_courses[:3]

    return LearningRoute(
        name=route_name,
        objective=objective,
        strengths=strengths,
        courses=courses,
        institutional_gaps=institutional_gaps,
        recommendation_reason=recommendation_reason,
    )


# ---------- Sidebar ----------
with st.sidebar:
    st.title("⚓ MAXBOT")
    st.caption("MVP | Asistente Inteligente de Capacitación Portuaria")
    st.markdown("""
**Propósito del MVP**
- Recomendar rutas de aprendizaje
- Orientar por perfil y necesidad
- Simular inteligencia institucional para RRHH
- Demostrar valor de una Academia Portuaria Inteligente
""")

    st.divider()
    st.markdown("""
**Áreas iniciales**
- Operación portuaria
- Planeación y evaluación
- Administración y finanzas
- Dirección / mando
""")

    st.markdown("### Valor institucional")
    st.markdown(
    """
    - Profesionalización del personal portuario  
    - Estandarización de capacidades  
    - Alineación con indicadores internacionales (UNCTAD / World Bank)  
    - Trazabilidad de formación y desempeño  
    - Generación de inteligencia para RRHH  
    """
    )

# ---------- Header ----------
st.title("Plataforma de Formación Estratégica para ASIPONA Veracruz")
st.info(
    "Este demo muestra cómo ASIPONA Veracruz puede implementar un sistema inteligente de capacitación alineado a desempeño operativo, indicadores estratégicos y toma de decisiones institucional."
)
st.subheader("Sistema Inteligente de Capacitación Institucional para puertos")
st.write(
    "Este demo muestra cómo ASIPONA Veracruz puede implementar un sistema real de capacitación inteligente, con impacto directo en desempeño institucional y operación portuaria."
)

left, right = st.columns([1.1, 1])


with left:
    st.markdown("### 1) Perfil del usuario")

    with st.form("maxbot_form"):
        area = st.selectbox("¿Cuál es tu área principal dentro del puerto?", AREA_OPTIONS)
        interest = st.selectbox("¿Qué te interesa fortalecer?", INTEREST_OPTIONS)
        level = st.selectbox("¿Cuál consideras que es tu nivel actual?", LEVEL_OPTIONS)

        employee_type = st.radio(
            "Tipo de usuario",
            ["Personal operativo", "Mando medio", "Directivo"],
            horizontal=True,
        )

        st.markdown("#### Diagnóstico rápido de capacidades (simulación)")
        diagnostico = st.multiselect(
            "¿En qué áreas sientes mayor brecha actualmente?",
            [
                "Uso de indicadores",
                "Toma de decisiones",
                "Comprensión de operación portuaria",
                "Uso de datos",
                "Gestión institucional",
            ]
        )

        submitted = st.form_submit_button("Generar recomendación", use_container_width=True)

    if submitted:
        route = build_route(area, interest, level)

        if "Uso de indicadores" in diagnostico:
            route.courses.insert(0, COURSE_CATALOG["Indicadores y desempeño"])

        if "Toma de decisiones" in diagnostico:
            route.courses.insert(0, COURSE_CATALOG["Toma de decisiones"])

        route.courses = route.courses[:3]

        st.session_state["route"] = route
        st.session_state["area"] = area
        st.session_state["interest"] = interest
        st.session_state["level"] = level
        st.session_state["employee_type"] = employee_type

    st.markdown("### 2) Catálogo inicial de cursos")
    st.markdown(
        """
- **KPIs portuarios alineados a UNCTAD + World Bank (CPPI)**  
- **Metodología de Marco Lógico (MML)**  
- **Evaluación de proyectos portuarios y priorización estratégica**  
- **Indicadores operativos aplicados a muelles, dragado, tiempos y eficiencia**  
- **Marco regulatorio y gestión institucional portuaria**  
- **Aplicaciones prácticas de IA en operación y toma de decisiones portuarias**  
- **Presupuesto basado en resultados aplicado a gestión portuaria**
"""
    )

with right:
    st.markdown("### 3) Recomendación de MAXBOT")
    st.info("Ruta sugerida con enfoque en desempeño operativo y alineación a indicadores portuarios")

    if "route" not in st.session_state:
        st.info(
            "Completa el perfil para que MAXBOT sugiera una ruta de formación, "
            "brechas institucionales y cursos recomendados."
        )
    else:
        route: LearningRoute = st.session_state["route"]
        st.success(f"**Ruta sugerida:** {route.name}")

        st.markdown("#### Objetivo de la ruta")
        st.write(route.objective)

        st.markdown("#### ¿Por qué esta recomendación?")
        st.write(route.recommendation_reason)

        st.markdown("#### Cursos recomendados")
        for i, course in enumerate(route.courses, start=1):
            st.markdown(f"**{i}.** {course}")

        st.markdown("#### Certificación asociada")
        certification_name = f"Certificación en {route.courses[0]}"
        st.success(f"🎓 {certification_name}")

        st.markdown(
            """
**Beneficios de la certificación**
- Compartible en LinkedIn
- Integrable al historial profesional del participante
- Alineada al programa institucional de capacitación
"""
        )

        st.markdown("#### Fortalezas del perfil")
        for item in route.strengths:
            st.markdown(f"- {item}")

        st.markdown("#### Brechas institucionales detectadas (simulación RRHH)")
        for gap in route.institutional_gaps:
            st.markdown(f"- {gap}")

        st.markdown("#### Valor institucional esperado")
        st.markdown(
            """
- Mayor **estandarización** de capacidades  
- Mejor **alineación entre formación y desempeño**  
- Más **trazabilidad de perfiles** y rutas de carrera  
- Mejores insumos para **decisión y planeación institucional**
"""
        )




st.divider()

st.markdown("""
### Sistema Inteligente de Capacitación Institucional para Veracruz

Este enfoque permite:

- Alinear la capacitación con indicadores operativos reales del puerto  
- Reducir curva de aprendizaje en temas clave (KPIs, operación, evaluación)  
- Estandarizar criterios de toma de decisiones entre áreas  
- Generar trazabilidad entre capacitación, desempeño y resultados  

No es capacitación teórica: es una herramienta de gestión institucional.
""")


col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 4) Simulación de inteligencia institucional para RRHH")
    st.write(
        "Este bloque no busca marketing, sino mostrar cómo la plataforma podría entregar "
        "información útil para gestión de capacidades institucionales."
    )

    simulated_data = {
        "Perfiles con mayor demanda": [
            "Mando medio en operación portuaria",
            "Planeación y evaluación",
            "Administración y finanzas",
        ],
        "Temas con mayor interés": [
            "KPIs portuarios",
            "Evaluación de proyectos",
            "IA aplicada a decisiones",
        ],
        "Brechas recurrentes": [
            "Estandarización de indicadores",
            "Trazabilidad de capacidades",
            "Vinculación entre desempeño y formación",
        ],
    }

    for section, items in simulated_data.items():
        st.markdown(f"**{section}**")
        for item in items:
            st.markdown(f"- {item}")

with col_b:
    st.markdown("### 5) Lógica del sistema (MVP)")
    st.code(
        """
Entrada:
- Área del usuario
- Interés principal
- Nivel actual

Proceso:
- MAXBOT clasifica perfil
- Asocia ruta sugerida
- Recomienda 3 cursos
- Identifica brechas institucionales
- Emisión de certificados digitales compartibles

Salida:
- Ruta de aprendizaje
- Cursos recomendados
- Insight para RRHH
        """.strip(),
        language="text",
    )

    st.markdown("### 6) Próximo nivel")
    st.markdown(
        """
- Login institucional  
- Histórico por empleado  
- Dashboard para RRHH  
- Progreso de carrera  
- Asistente conversacional con documentos internos  

"""
    )


st.divider()
st.caption(
    "MAXBOT MVP | Demo conceptual para una Academia Portuaria Inteligente. "
    "Este prototipo está diseñado para demostrar valor institucional antes del desarrollo completo de la plataforma."
)
