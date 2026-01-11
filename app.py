import streamlit as st
import pandas as pd
import datetime
import random
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Gestión Taller 4.0",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
<style>
/* --- FUENTE CORPORATIVA --- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* --- CONTENEDOR PRINCIPAL --- */
.main .block-container {
    padding: 2rem 3rem;
    max-width: 1400px;
}

/* --- TÍTULOS --- */
h1 {
    font-size: 1.8rem;
    font-weight: 600;
    color: #1f2933;
}
h2 {
    font-size: 1.4rem;
    font-weight: 500;
    color: #374151;
}
h3 {
    font-size: 1.1rem;
    font-weight: 500;
    color: #4b5563;
}

/* --- TARJETAS KPI --- */
.metric-card {
    background-color: #ffffff;
    border-radius: 8px;
    padding: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
}

.metric-card h2 {
    color: #111827;   /* 👈 FIX NÚMEROS KPI */
}

.metric-card h3 {
    color: #6b7280;
}

/* --- BOTONES --- */
.stButton > button {
    background-color: #1f2933;
    color: white;
    border-radius: 6px;
    height: 42px;
    font-weight: 500;
    border: none;
}
.stButton > button:hover {
    background-color: #111827;
}

/* --- TABLAS --- */
[data-testid="stDataFrame"] {
    border: 1px solid #e5e7eb;
    border-radius: 6px;
}

/* --- SIDEBAR --- */
section[data-testid="stSidebar"] {
    background-color: #111827;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] p {
    color: #f9fafb;
}

/* --- FIX EXPANDER: ocultar SOLO texto de accesibilidad (keyboard shortcut) --- */
span.streamlit-expanderKeyboardShortcut {
    display: none;
}
</style>
""", unsafe_allow_html=True)





# --- GESTIÓN DE DATOS (SIMULACIÓN Y ESTADO) ---
if 'data_initialized' not in st.session_state:
    # Simular datos iniciales para que la app no arranque vacía
    
    # Técnicos
    tecnicos_data = {
        'ID': [101, 102, 103, 104, 105],
        'Nombre': ['Carlos Ruiz', 'Ana López', 'Miguel Ángel', 'Sofia Chen', 'Roberto Diaz'],
        'Especialidad': ['Mecánica General', 'Electricidad', 'Chapa y Pintura', 'Diagnóstico Avanzado', 'Mecánica Pesada'],
        'Nivel': ['Senior', 'Semi-Senior', 'Senior', 'Junior', 'Senior'],
        'Estado': ['Activo', 'Activo', 'Activo', 'Activo', 'Inactivo']
    }
    st.session_state.df_tecnicos = pd.DataFrame(tecnicos_data)
    # Tareas (Histórico simulado)
    tareas_data = {
        'ID_Tarea': [f'T-{i:04d}' for i in range(1, 21)],
        'Fecha': [datetime.date.today() - datetime.timedelta(days=random.randint(0, 30)) for _ in range(20)],
        'Tipo': random.choices(['Servicio 10k', 'Frenos', 'Embrague', 'Diagnóstico Eléctrico', 'Pintura Paragolpes'], k=20),
        'Tecnico_ID': random.choices(tecnicos_data['ID'], k=20),
        'Tiempo_Estandar_Min': [],
        'Tiempo_Real_Min': [],
        'Estado': random.choices(['Completada', 'Completada', 'Completada', 'En Proceso', 'Pendiente'], weights=[0.7, 0.1, 0.1, 0.05, 0.05], k=20),
        'Es_Retrabajo': []
    }
    
    # Lógica semi-realista para tiempos
    for tipo in tareas_data['Tipo']:
        if 'Servicio' in tipo: t, dev = 90, 10
        elif 'Frenos' in tipo: t, dev = 120, 20
        elif 'Embrague' in tipo: t, dev = 240, 40
        elif 'Diagnóstico' in tipo: t, dev = 45, 15
        else: t, dev = 180, 30
        
        std = t
        real = int(random.gauss(t, dev))
        tareas_data['Tiempo_Estandar_Min'].append(std)
        tareas_data['Tiempo_Real_Min'].append(max(real, 10)) # Mínimo 10 mins
        
        # Retrabajo aleatorio si el tiempo real fue muy bajo o muy alto (simulación de error)
        es_retrabajo = False
        if real > std * 1.5 or random.random() < 0.05:
            es_retrabajo = True
        tareas_data['Es_Retrabajo'].append(es_retrabajo)
        
    st.session_state.df_tareas = pd.DataFrame(tareas_data)
    # Kaizen (Mejoras)
    kaizen_data = {
        'ID_Kaizen': ['K-001', 'K-002', 'K-003'],
        'Fecha': [datetime.date.today() - datetime.timedelta(days=15), datetime.date.today() - datetime.timedelta(days=5), datetime.date.today()],
        'Problema': ['Demora en búsqueda de herramients especiales', 'Iluminación insuficiente en fosa 2', 'Exceso de formularios en papel'],
        'Area': ['Taller General', 'Mecánica', 'Administración'],
        'Propuesta': ['Implementar tablero de sombras (Shadow Board)', 'Instalar luces LED direccionales', 'Digitalizar OT en tablet'],
        'Estado': ['Implementada', 'En Curso', 'Pendiente'],
        'Responsable': ['Carlos Ruiz', 'Seguridad Higiene', 'Jefe Taller'],
        'Impacto': ['Tiempo', 'Seguridad', 'Calidad']
    }
    st.session_state.df_kaizen = pd.DataFrame(kaizen_data)
    
    st.session_state.data_initialized = True
# --- FUNCIONES AUXILIARES ---
def get_tecnico_name(id_tech):
    tech = st.session_state.df_tecnicos[st.session_state.df_tecnicos['ID'] == id_tech]
    if not tech.empty:
        return tech.iloc[0]['Nombre']
    return "Desconocido"
def kpi_card(title, value, delta=None, color="normal"):
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin:0; font-size: 1rem; color: #555;">{title}</h3>
        <h2 style="margin:0; font-size: 1.8rem;">{value}</h2>
        {f'<p style="margin:0; color: {"green" if color=="success" else "red"}; font-weight:bold;">{delta}</p>' if delta else ''}
    </div>
    """, unsafe_allow_html=True)
# --- SIDEBAR (NAVEGACIÓN) ---
with st.sidebar:
    st.image("https://st3.depositphotos.com/1002927/13268/v/450/depositphotos_132689652-stock-illustration-futuristic-gear-wheel-with-car.jpg", width=80)
    st.title("Workshop Operations Manager")
    st.caption("Operational & Continuous Improvement System")

    
    menu = st.radio(
        "Navegación",
        ["Dashboard General", "Gestión de Tareas", "Técnicos", "Calidad & Retrabajos", "Mejora Continua (Kaizen)"]
    )
    
    st.markdown("---")
    st.caption("© 2026 AutoSolutions Ind.")
# --- PÁGINAS ---
# 1. DASHBOARD GENERAL
if menu == "Dashboard General":
    st.title("Tablero de Control Operativo")
    
    # KPIs Superiores
    df_t = st.session_state.df_tareas
    df_k = st.session_state.df_kaizen
    
    total_tareas = len(df_t)
    tasa_retrabajo = (df_t['Es_Retrabajo'].sum() / total_tareas * 100) if total_tareas > 0 else 0
    kaizen_activas = len(df_k[df_k['Estado'] != 'Implementada'])
    
    # Calcular Eficiencia Global (Tiempo Estándar / Tiempo Real)
    # Cuidado con división por cero
    df_completadas = df_t[df_t['Estado'] == 'Completada']
    if not df_completadas.empty:
        eficiencia_avg = (df_completadas['Tiempo_Estandar_Min'].sum() / df_completadas['Tiempo_Real_Min'].sum()) * 100
    else:
        eficiencia_avg = 0
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        kpi_card("Total Tareas (Mes)", f"{total_tareas}", "Obj: >50")
    with col2:
        # Si la eficiencia > 100%, es bueno (verde), si no (rojo/amarillo)
        delta_ef = f"{eficiencia_avg:.1f}%"
        color_ef = "success" if eficiencia_avg >= 95 else "normal"
        kpi_card("Eficiencia Global", delta_ef, "Target: 95%", color_ef)
    with col3:
        # Retrabajo ideal < 3%
        delta_re = f"{tasa_retrabajo:.1f}%"
        color_re = "success" if tasa_retrabajo < 3 else "normal"
        kpi_card("Tasa de Retrabajos", delta_re, "Max: 3%", color_re) # Si es alto, no es success, simplificación visual
    with col4:
        kpi_card("Oportunidades Kaizen", f"{kaizen_activas} Activas")
    st.markdown("---")
    
    # Gráficos
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Distribución de Tareas por Tipo")
        if not df_t.empty:
            chart_data = df_t['Tipo'].value_counts()
            st.bar_chart(chart_data, color="#ff4b4b")
        else:
            st.info("Sin datos para mostrar.")
            
    with c2:
        st.subheader("Productividad por Técnico (Tareas Completadas)")
        if not df_t.empty:
            prod_tech = df_t[df_t['Estado']=='Completada']['Tecnico_ID'].value_counts()
            # Mapear IDs a Nombres
            prod_tech.index = [get_tecnico_name(tid) for tid in prod_tech.index]
            st.bar_chart(prod_tech)
        else:
            st.info("Sin datos.")
# 2. GESTIÓN DE TAREAS
elif menu == "Gestión de Tareas":
    st.title("🛠️ Gestión Operativa")
    
    tab1, tab2 = st.tabs(["📋 Nueva Tarea", "🗃️ Historial de Tareas"])
    
    with tab1:
        st.write("### Asignar Nueva Orden de Trabajo")
        with st.form("form_tarea"):
            c_f1, c_f2 = st.columns(2)
            
            with c_f1:
                tipo_tarea = st.selectbox("Tipo de Servicio", ["Servicio 10k", "Frenos", "Embrague", "Diagnóstico Eléctrico", "Chapa/Pintura", "Otro"])
                tiempo_std = st.number_input("Tiempo Estándar (min)", min_value=10, value=60, step=10)
                tecnico_asignado = st.selectbox(
                    "Técnico Asignado", 
                    options=st.session_state.df_tecnicos[st.session_state.df_tecnicos['Estado']=='Activo']['ID'],
                    format_func=lambda x: f"{x} - {get_tecnico_name(x)}"
                )
            
            with c_f2:
                fecha_tarea = st.date_input("Fecha Programada", datetime.date.today())
                observaciones = st.text_area("Observaciones / Detalles del vehículo")
                
            submitted = st.form_submit_button("Crear Tarea")
            
            if submitted:
                # Crear ID Tarea
                new_id = f"T-{len(st.session_state.df_tareas) + 100:04d}"
                new_row = {
                    'ID_Tarea': new_id,
                    'Fecha': fecha_tarea,
                    'Tipo': tipo_tarea,
                    'Tecnico_ID': tecnico_asignado,
                    'Tiempo_Estandar_Min': tiempo_std,
                    'Tiempo_Real_Min': 0, # Inicia en 0
                    'Estado': 'Pendiente',
                    'Es_Retrabajo': False
                }
                st.session_state.df_tareas = pd.concat([st.session_state.df_tareas, pd.DataFrame([new_row])], ignore_index=True)
                st.success(f"Tarea {new_id} creada exitosamente.")
    
    with tab2:
        st.write("### Registro de Operaciones")
        
        # Filtros
        filtro_estado = st.multiselect("Filtrar por Estado", st.session_state.df_tareas['Estado'].unique(), default=st.session_state.df_tareas['Estado'].unique())
        
        df_view = st.session_state.df_tareas[st.session_state.df_tareas['Estado'].isin(filtro_estado)].copy()
        
        # Mapear nombre técnico para visualización
        df_view['Nombre_Tecnico'] = df_view['Tecnico_ID'].apply(get_tecnico_name)
        
        st.dataframe(
            df_view[['ID_Tarea', 'Fecha', 'Tipo', 'Nombre_Tecnico', 'Estado', 'Tiempo_Estandar_Min', 'Tiempo_Real_Min']],
            use_container_width=True,
            hide_index=True
        )
        
        st.subheader("Actualizar Tarea")
        col_up1, col_up2, col_up3 = st.columns(3)
        with col_up1:
            tarea_sel = st.selectbox("Seleccionar ID Tarea", st.session_state.df_tareas['ID_Tarea'].tolist())
        with col_up2:
            nuevo_estado = st.selectbox("Nuevo Estado", ["Pendiente", "En Proceso", "Completada", "Cancelada"])
        with col_up3:
            tiempo_real = st.number_input("Tiempo Real Invertido (min)", min_value=0, step=5)
            
        if st.button("Actualizar Estado"):
            idx = st.session_state.df_tareas[st.session_state.df_tareas['ID_Tarea'] == tarea_sel].index[0]
            st.session_state.df_tareas.at[idx, 'Estado'] = nuevo_estado
            if tiempo_real > 0:
                st.session_state.df_tareas.at[idx, 'Tiempo_Real_Min'] = tiempo_real
            st.success("Tarea actualizada.")
# 3. GESTIÓN DE TÉCNICOS
elif menu == "Técnicos":
    st.title("👥 Equipo de Trabajo")
    
    with st.expander("➕ Alta de Nuevo Técnico"):
        with st.form("new_tech"):
            c1, c2 = st.columns(2)
            nombre = c1.text_input("Nombre Completo")
            especialidad = c2.selectbox("Especialidad", ["Mecánica General", "Electricidad", "Chapa y Pintura", "Diagnóstico"])
            nivel = c1.selectbox("Nivel (Seniority)", ["Junior", "Semi-Senior", "Senior"])
            estado_tech = c2.selectbox("Estado Inicial", ["Activo", "Inactivo"])
            
            if st.form_submit_button("Guardar"):
                new_id = st.session_state.df_tecnicos['ID'].max() + 1
                new_tech = {'ID': new_id, 'Nombre': nombre, 'Especialidad': especialidad, 'Nivel': nivel, 'Estado': estado_tech}
                st.session_state.df_tecnicos = pd.concat([st.session_state.df_tecnicos, pd.DataFrame([new_tech])], ignore_index=True)
                st.success("Técnico registrado.")
    
    st.dataframe(st.session_state.df_tecnicos, use_container_width=True, hide_index=True)
    
    # Métrica rápida de equipo
    activs = len(st.session_state.df_tecnicos[st.session_state.df_tecnicos['Estado'] == 'Activo'])
    st.metric("Técnicos Activos", activs)
# 4. CALIDAD Y RETRABAJOS
elif menu == "Calidad & Retrabajos":
    st.title("🛡️ Control de Calidad")
    
    st.info("El sistema detecta automáticamente desvíos significativos de tiempo como potenciales alertas de calidad.")
    
    df = st.session_state.df_tareas
    
    # Análisis de desvíos (>20% del tiempo estandár)
    df['Desvio'] = df['Tiempo_Real_Min'] - df['Tiempo_Estandar_Min']
    df['Porc_Desvio'] = (df['Desvio'] / df['Tiempo_Estandar_Min']) * 100
    
    desvios_criticos = df[(df['Porc_Desvio'] > 20) & (df['Estado'] == 'Completada')]
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("⚠️ Alertas de Tiempo")
        st.write("Tareas completadas que excedieron el tiempo estándar en +20%")
        if not desvios_criticos.empty:
            st.dataframe(desvios_criticos[['ID_Tarea', 'Tipo', 'Tecnico_ID', 'Tiempo_Estandar_Min', 'Tiempo_Real_Min', 'Porc_Desvio']])
        else:
            st.success("No hay desvíos críticos recientes.")
            
    with c2:
        st.subheader("📉 Reporte de Retrabajos")
        retrabajos = df[df['Es_Retrabajo'] == True]
        st.write(f"Total Retrabajos Históricos: {len(retrabajos)}")
        if not retrabajos.empty:
             st.dataframe(retrabajos[['ID_Tarea', 'Tipo', 'Fecha', 'Tecnico_ID']])
        else:
            st.write("Sin retrabajos registrados.")
    st.markdown("---")
    st.write("### Registrar Retrabajo Manual")
    id_ref = st.selectbox("Tarea Original (ID)", df['ID_Tarea'].unique())
    motivo = st.text_input("Motivo del fallo / Causa Raíz")
    if st.button("Marcar como Retrabajo"):
        idx = df[df['ID_Tarea'] == id_ref].index[0]
        st.session_state.df_tareas.at[idx, 'Es_Retrabajo'] = True
        st.warning(f"La tarea {id_ref} ha sido marcada como retrabajo.")
# 5. KAIZEN (MEJORA CONTINUA)
elif menu == "Mejora Continua (Kaizen)":
    st.title("Módulo de Mejora Continua (Kaizen)")
    st.markdown("Gestión de oportunidades de mejora y resolución de problemas de raíz.")
    
    col_k1, col_k2 = st.columns([1, 2])
    
    with col_k1:
        st.subheader("Nueva Propuesta")
        with st.form("kaizen_form"):
            problema = st.text_area("Problema Detectado")
            area = st.selectbox("Área", ["Mecánica", "Recepción", "Repuestos", "Limpieza", "Administración"])
            impacto = st.selectbox("Categoría de Impacto", ["Calidad", "Costo", "Entrega (Tiempo)", "Seguridad", "Moral"])
            propuesta = st.text_area("Propuesta de Solución")
            responsable = st.text_input("Responsable Sugerido")
            
            if st.form_submit_button("Registrar Kaizen"):
                new_k_id = f"K-{len(st.session_state.df_kaizen) + 1:03d}"
                new_kaizen = {
                    'ID_Kaizen': new_k_id,
                    'Fecha': datetime.date.today(),
                    'Problema': problema,
                    'Area': area,
                    'Propuesta': propuesta,
                    'Estado': 'Pendiente',
                    'Responsable': responsable, 
                    'Impacto': impacto
                }
                st.session_state.df_kaizen = pd.concat([st.session_state.df_kaizen, pd.DataFrame([new_kaizen])], ignore_index=True)
                st.success(f"Ticket {new_k_id} generado.")
    
    with col_k2:
        st.subheader("Tablero de Mejoras")
        if not st.session_state.df_kaizen.empty:
            # Vista tipo Kanban simplificada con pestañas
            t_pend, t_proc, t_done = st.tabs(["🔴 Pendientes", "🟡 En Curso", "🟢 Implementadas"])
            
            def show_kaizen_list(status_flt):
                subset = st.session_state.df_kaizen[st.session_state.df_kaizen['Estado'] == status_flt]
                if subset.empty:
                    st.write("--- Vacío ---")
                else:
                    for i, row in subset.iterrows():
                        with st.container():
                            st.markdown(f"**{row['ID_Kaizen']} - {row['Area']}**")
                            st.caption(f"Impacto: {row['Impacto']} | Resp: {row['Responsable']}")
                            st.text(f"🛑 {row['Problema']}")
                            st.info(f"💡 {row['Propuesta']}")
                            if status_flt != "Implementada":
                                c_act1, c_act2 = st.columns(2)
                                if c_act1.button("Avanzar etapa", key=f"adv_{row['ID_Kaizen']}"):
                                    next_st = "En Curso" if status_flt == "Pendiente" else "Implementada"
                                    st.session_state.df_kaizen.at[i, 'Estado'] = next_st
                                    st.experimental_rerun()
                                    
                            st.divider()
            with t_pend: show_kaizen_list("Pendiente")
            with t_proc: show_kaizen_list("En Curso")
            with t_done: show_kaizen_list("Implementada")
        else:
            st.info("Aún no hay registros Kaizen.")
# Footer simple
st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.info("Modo Simulación Activo")