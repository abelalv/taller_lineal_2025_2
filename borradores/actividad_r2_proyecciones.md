# Actividad guiada (R²): Rutas, Vientos y Proyecciones

**Contexto.** RoboDelivery opera robots de entrega en una ciudad idealizada en el plano $\mathbb{R}^2$.
Los centros A, B y C están definidos por sus **coordenadas** $(x,y)$ en kilómetros.
El sistema sufre dos **vientos** (Norte → empuja hacia el **Sur** y Este → empuja hacia el **Oeste**), modelados como **vectores**.
Hay **obstáculos lineales** (calles/avenidas) modelados como rectas.

**Regla de oro:** *Solo cambia las variables en la sección “Variables que puedes modificar” del script `actividad_r2_proyecciones.py`.*
El resto del código no necesita edición: realiza los cálculos y muestra resultados.

## Objetivos de aprendizaje (2º semestre de ingeniería)
1. Operar vectores en $\mathbb{R}^2$: suma, producto punto, norma, ángulos.
2. Aplicar **proyección de un vector** sobre otro y su interpretación física.
3. Modelar rutas como **vectores de desplazamiento** y obstáculos como **rectas**.
4. Conectar el signo de la proyección con **viento a favor/contra**.
5. Usar magnitudes vectoriales para una **estimación energética** simple.

---

## Preguntas (el script imprime resultados con base en tus variables)

**P1. Distancias de rutas.** Con tus coordenadas de A, B y C, ¿cuáles son las distancias (km) de A→B, B→C y A→C?
> Cambia solo las coordenadas de A, B, C y observa los resultados.

**P2. Ángulos y vientos.** ¿Cuál es el ángulo (°) entre cada ruta y cada viento?
> Cambia solo la intensidad de cada viento. ¿Qué ruta es más “alineada” (ángulo pequeño) con el viento Norte? ¿Y con el Este?

**P3. Proyecciones de viento sobre rutas.** Para la ruta A→B, ¿la proyección del viento resultante (Norte+Este) es positiva (viento **a favor**) o negativa (viento **en contra**)?
> Cambia *solo* las intensidades de los vientos y explica el signo de la proyección.

**P4. Cruce con obstáculos.** Con tu recta-obstáculo $y = y_0$ (o $x = x_0$), ¿la ruta B→C la cruza?
> Cambia *solo* el valor de `y_obstaculo` o `x_obstaculo` y verifica el booleano de cruce.

**P5. Energía estimada.** Suponiendo velocidad base constante y penalización por viento **en contra** proporcional a la proyección escalar (solo si es negativa), ¿qué energía (Wh) consumen las rutas?
> Cambia *solo* `vel_base_kmh`, `energia_por_km_Wh` y `penalizacion_Wh_por_mps_por_km` y compara rutas.

> **Sugerencia:** Si la proyección escalar del viento resultante sobre la ruta es $p$ (m/s), entonces usamos $p_-= \min(p,0)$ para penalizar solo viento en contra.

---

## Cómo trabajar
1. Abre `actividad_r2_proyecciones.py`.
2. Edita únicamente la sección **Variables que puedes modificar**.
3. Ejecuta el script y responde las 5 preguntas con base en la salida.
4. (Opcional) Guarda capturas de la salida para tu reporte.

¡Listo! No necesitas tocar funciones ni fórmulas.