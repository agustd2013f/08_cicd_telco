import csv
import textwrap
import matplotlib.pyplot as plt

# Datos estructurados del cuadro comparativo
data = {
    "Actividades Estratégicas": {
        "color": "#3498db",  # Azul
        "Definición": "Actividades prioritarias para la soberanía, la seguridad nacional y el desarrollo integral del país que están reservadas de forma exclusiva o prioritaria al control del Estado por mandato constitucional (Art. 28).",
        "Ejemplo en México": "Exploración, extracción y procesamiento de hidrocarburos, así como la transmisión y distribución de energía eléctrica.",
        "Institución / Empresa": "Petróleos Mexicanos (PEMEX) y Comisión Federal de Electricidad (CFE).",
        "Importancia Social": "Asegura la soberanía energética de la nación, garantiza el acceso continuo a recursos básicos para hogares e industrias, e ingresa recursos clave al presupuesto público."
    },
    "Actividades Exclusivas": {
        "color": "#e74c3c",  # Rojo
        "Definición": "Funciones de orden soberano, regulatorio y de autoridad propias del poder público que no pueden ser delegadas ni ejercidas bajo ninguna circunstancia por agentes económicos privados.",
        "Ejemplo en México": "Emisión de moneda nacional (billetes y monedas), acuñación y regulación de la política monetaria y financiera del país.",
        "Institución / Empresa": "Banco de México (Banxico).",
        "Importancia Social": "Preserva la estabilidad del poder adquisitivo de la población, controla la inflación y brinda confianza y certeza al sistema económico nacional."
    },
    "Actividades Competitivas": {
        "color": "#2ecc71",  # Verde
        "Definición": "Servicios económicos o sociales prestados por el Estado participando de manera simultánea en el mercado junto con empresas privadas para corregir fallas de mercado, evitar monopolios o garantizar precios accesibles.",
        "Ejemplo en México": "Prestación de servicios financieros, ahorro y distribución de apoyos de programas sociales en comunidades vulnerables.",
        "Institución / Empresa": "Banco del Bienestar, S.N.C. / Financiera para el Bienestar (FINABIEN).",
        "Importancia Social": "Promueve la inclusión financiera de la población en zonas rurales o marginadas donde la banca privada no tiene presencia por no ser rentable."
    },
    "Actividades de Mercado": {
        "color": "#9b59b6",  # Morado
        "Definición": "Producción y venta de bienes o servicios operados a través de empresas públicas que compiten en el mercado comercial abierto para atender necesidades operativas, logísticas o de desarrollo regional.",
        "Ejemplo en México": "Operación de transporte aéreo comercial de pasajeros y carga a nivel nacional e internacional.",
        "Institución / Empresa": "Mexicana de Aviación (Aerolínea del Estado Mexicano).",
        "Importancia Social": "Mejora la conectividad territorial uniendo ciudades con poca cobertura comercial privada, estimula el turismo regional y genera competencia para regular tarifas."
    }
}

def generar_csv():
    csv_filename = "cuadro_comparativo_miro.csv"
    categories = list(data.keys())
    fields = ["Definición", "Ejemplo en México", "Institución / Empresa", "Importancia Social"]
    
    with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(categories)
        for field in fields:
            row = [f"{field}:\n{data[cat][field]}" for cat in categories]
            writer.writerow(row)
    print(f"✅ Archivo CSV generado: '{csv_filename}'")

def generar_imagen():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    ax.axis('off')

    plt.title("CUADRO COMPARATIVO: ACTIVIDADES ECONÓMICAS DEL ESTADO MEXICANO", 
              fontsize=15, fontweight='bold', pad=20)

    categories = list(data.keys())
    fields_list = ["Definición", "Ejemplo en México", "Institución / Empresa", "Importancia Social"]

    col_width = 0.23
    row_height = 0.18
    left_margin = 0.04
    top_margin = 0.85

    for col_idx, cat in enumerate(categories):
        cat_data = data[cat]
        col_x = left_margin + col_idx * (col_width + 0.015)
        
        # Encabezado
        header_rect = plt.Rectangle((col_x, top_margin), col_width, 0.08, 
                                    facecolor=cat_data["color"], edgecolor='black', 
                                    linewidth=1.2, transform=ax.transAxes)
        ax.add_patch(header_rect)
        ax.text(col_x + col_width/2, top_margin + 0.04, cat, color='white', 
                weight='bold', fontsize=10, ha='center', va='center', transform=ax.transAxes)
        
        # Contenido
        for row_idx, field in enumerate(fields_list):
            y_pos = top_margin - (row_idx + 1) * (row_height + 0.01)
            
            box_rect = plt.Rectangle((col_x, y_pos), col_width, row_height, 
                                     facecolor='#FAFAFA', edgecolor=cat_data["color"], 
                                     linewidth=1, transform=ax.transAxes)
            ax.add_patch(box_rect)
            
            # Etiqueta
            ax.text(col_x + 0.01, y_pos + row_height - 0.025, f"• {field}:", 
                    weight='bold', fontsize=9, color='#2C3E50', transform=ax.transAxes)
            
            # Texto
            text_val = cat_data[field]
            wrapped_text = "\n".join(textwrap.wrap(text_val, width=32))
            ax.text(col_x + 0.01, y_pos + row_height - 0.045, wrapped_text, 
                    fontsize=8, color='#333333', va='top', transform=ax.transAxes)

    image_filename = "cuadro_comparativo.png"
    plt.tight_layout()
    plt.savefig(image_filename, bbox_inches='tight', dpi=300)
    print(f"✅ Imagen PNG generada: '{image_filename}'")

if __name__ == "__main__":
    generar_csv()
    generar_imagen()