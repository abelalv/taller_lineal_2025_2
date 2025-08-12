import numpy as np

# ================================================================
# === Variables que puedes modificar (¡solo esta sección!) =======
# ================================================================

# Coordenadas (km) de los centros A, B, C en el plano (x, y)
A = np.array([1.0, 8.0])
B = np.array([6.0, 7.0])
C = np.array([8.0, 2.0])

# Intensidades de vientos (m/s). Norte empuja hacia "abajo" (sur), Este empuja hacia la izquierda (oeste).
intensidad_viento_norte = 1.0   # m/s (vector [0, -intensidad])
intensidad_viento_este  = 1.0   # m/s (vector [-intensidad, 0])

# Obstáculos como líneas principales (puedes usar una u otra)
usar_obstaculo_horizontal = True
y_obstaculo = 5.0   # recta y = y_obstaculo
x_obstaculo = 4.5   # recta x = x_obstaculo

# Parámetros de energía/velocidad
vel_base_kmh = 10.0                 # velocidad base (km/h) para todas las rutas
energia_por_km_Wh = 20.0            # energía base por km (Wh/km)
penalizacion_Wh_por_mps_por_km = 3.0 # penalización adicional por (m/s) de viento en contra por km

# ================================================================
# === No edites debajo: funciones y cálculos =====================
# ================================================================

def norma(v):
    return float(np.linalg.norm(v))

def distancia(P, Q):
    return norma(Q - P)

def angulo_grados(u, v):
    nu, nv = norma(u), norma(v)
    if nu == 0 or nv == 0:
        return np.nan
    cosang = np.clip(np.dot(u, v) / (nu * nv), -1.0, 1.0)
    return float(np.degrees(np.arccos(cosang)))

def proyeccion_escalar(u, v):
    """ Proyección escalar de u sobre v: (u·v_hat) """
    nv = norma(v)
    if nv == 0:
        return np.nan
    v_hat = v / nv
    return float(np.dot(u, v_hat))

def proyeccion_vector(u, v):
    """ Proyección vectorial de u sobre v: [(u·v_hat) v_hat] """
    nv = norma(v)
    if nv == 0:
        return np.array([np.nan, np.nan])
    v_hat = v / nv
    return float(np.dot(u, v_hat)) * v_hat

def cruza_linea_horizontal(P, Q, y0):
    """ ¿El segmento PQ cruza la línea y = y0? """
    y1, y2 = P[1], Q[1]
    return (min(y1, y2) <= y0) and (y0 <= max(y1, y2)) and (y1 != y2)

def cruza_linea_vertical(P, Q, x0):
    """ ¿El segmento PQ cruza la línea x = x0? """
    x1, x2 = P[0], Q[0]
    return (min(x1, x2) <= x0) and (x0 <= max(x1, x2)) and (x1 != x2)

# Vectores de viento
viento_norte = np.array([0.0, -intensidad_viento_norte])
viento_este  = np.array([-intensidad_viento_este, 0.0])
viento_total = viento_norte + viento_este

# Rutas
rAB = B - A
rBC = C - B
rAC = C - A

# --- P1: Distancias ---
dAB = distancia(A, B)
dBC = distancia(B, C)
dAC = distancia(A, C)

# --- P2: Ángulos ruta-viento ---
ang_AB_N = angulo_grados(rAB, viento_norte)
ang_AB_E = angulo_grados(rAB, viento_este)
ang_BC_N = angulo_grados(rBC, viento_norte)
ang_BC_E = angulo_grados(rBC, viento_este)
ang_AC_N = angulo_grados(rAC, viento_norte)
ang_AC_E = angulo_grados(rAC, viento_este)

# --- P3: Proyección del viento total sobre rAB ---
proj_vtotal_sobre_AB = proyeccion_escalar(viento_total, rAB)   # m/s
# Signo > 0: viento a favor de la dirección de la ruta; < 0: en contra

# --- P4: Cruce con obstáculo ---
if usar_obstaculo_horizontal:
    cruza_BC = cruza_linea_horizontal(B, C, y_obstaculo)
else:
    cruza_BC = cruza_linea_vertical(B, C, x_obstaculo)

# --- P5: Energía estimada en Wh (penaliza solo viento en contra) ---
def energia_ruta(dist_km, ruta_vec):
    p = proyeccion_escalar(viento_total, ruta_vec)  # m/s
    p_contra = min(p, 0.0)  # solo si es <= 0 hay penalización
    penalizacion_por_km = -p_contra * penalizacion_Wh_por_mps_por_km
    return dist_km * (energia_por_km_Wh + penalizacion_por_km)

E_AB = energia_ruta(dAB, rAB)
E_BC = energia_ruta(dBC, rBC)
E_AC = energia_ruta(dAC, rAC)

# ---------------- Salida legible ----------------
print("=== ACTIVIDAD: R^2, PROYECCIONES Y RUTAS ===\n")
print("Centros (km):")
print(f" A = {A},  B = {B},  C = {C}\n")

print("Vientos (m/s):")
print(f" Viento Norte = {viento_norte},  Viento Este = {viento_este},  Total = {viento_total}\n")

print("P1) Distancias de ruta (km):")
print(f" d(A→B) = {dAB:.3f},  d(B→C) = {dBC:.3f},  d(A→C) = {dAC:.3f}\n")

print("P2) Ángulos (°) entre rutas y vientos:")
print(f" Ruta A→B vs Norte = {ang_AB_N:.1f}, vs Este = {ang_AB_E:.1f}")
print(f" Ruta B→C vs Norte = {ang_BC_N:.1f}, vs Este = {ang_BC_E:.1f}")
print(f" Ruta A→C vs Norte = {ang_AC_N:.1f}, vs Este = {ang_AC_E:.1f}\n")

print("P3) Proyección escalar del viento total sobre la ruta A→B (m/s):")
print(f" Proyección = {proj_vtotal_sobre_AB:.3f}  -> {'A FAVOR' if proj_vtotal_sobre_AB>0 else ('EN CONTRA' if proj_vtotal_sobre_AB<0 else 'NEUTRA')} \n")

print("P4) Cruce de ruta B→C con obstáculo:")
if usar_obstaculo_horizontal:
    print(f" ¿Cruza la recta y = {y_obstaculo}? -> {cruza_BC}")
else:
    print(f" ¿Cruza la recta x = {x_obstaculo}? -> {cruza_BC}")
print()

print("P5) Energía estimada por ruta (Wh):")
print(f" E(A→B) = {E_AB:.2f} Wh,  E(B→C) = {E_BC:.2f} Wh,  E(A→C) = {E_AC:.2f} Wh")
print("\nNota: la penalización aplica solo si la proyección del viento total sobre la ruta es negativa (viento en contra).")
