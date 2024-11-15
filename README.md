
# 🛍️ **Simulador de Ventas** 🚗

## 📝 **Descripción** 

Esta aplicación está diseñada para ayudar a los usuarios a aprender y practicar el análisis de datos generando datos de ventas simulados. El propósito es proporcionar un conjunto de datos realista que se pueda utilizar para probar técnicas de análisis y visualización de datos, como el análisis de ventas 📊, el análisis de tendencias 📈, y la creación de informes con herramientas como **Streamlit** y **Faker**. 

La aplicación genera datos de ventas simuladas, incluyendo detalles como el vendedor 👨‍💼, el cliente 👩‍💼, el producto (vehículo 🚙), la cantidad, el total de la venta 💸, la fecha de venta 📅 y la URL de la imagen del producto 📷. Estos datos se pueden descargar en formato JSON para ser utilizados en análisis posteriores.

---

## 📦 **Requisitos** 

- 🐍 **Python 3.x**
- 📦 Librerías necesarias:
  - `Faker`
  - `streamlit`

---

## 🛠️ **Instalación** 

1. Clona este repositorio o descarga los archivos del proyecto.

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```bash
   streamlit run app.py
   ```

   Esto abrirá la aplicación en tu navegador 🌐, donde podrás interactuar con los formularios y generar ventas simuladas.

---

## 🖥️ **Uso de la Aplicación**

1. **Generación de Ventas** 💰: En el panel lateral, puedes configurar varios filtros, como el número de clientes, vendedores 👩‍💻, vehículos 🚗, y la cantidad de facturas. Al presionar el botón "Generar" 🟢, la aplicación generará ventas simuladas basadas en estos parámetros.

2. **Visualización de Datos** 📊: Una vez que las ventas son generadas, se mostrarán en la página principal con detalles como:

   - Vendedor 👨‍💼
   - Cliente 👩‍💼
   - Producto (Vehículo) 🚙
   - Cantidad 🔢
   - Precio Unitario 💵
   - Total de la Venta 💸
   - Fecha de Venta 📅
   - URL de la Imagen del Vehículo 🖼️
   - Ciudad de Venta 🌆 (Ubicación aleatoria asignada a cada venta)

3. **Descargar los Datos** ⬇️: Puedes descargar los datos generados en formato JSON utilizando el botón de descarga disponible en la interfaz.

---

## 🗂️ **Ejemplo de Salida**

Cuando se generan ventas, los datos tendrán la siguiente estructura:

```json
[
  {
    "id_venta": "a3c9b2a1-1234-5678-9101-112233445566",
    "vendedor": "Juan Pérez 👨‍💼",
    "cliente": "Ana López 👩‍💼",
    "producto": "Toyota Corolla 🚙",
    "cantidad": 2,
    "total_venta": 40000,
    "fecha_venta": "2023-10-15",
    "vehiculo_url": "https://example.com/images/toyota_corolla.jpg",
    "ciudad": "Santiago 🌆"
  },
  ...
]
```

---

## 🎯 **Objetivo de la Aplicación**

El objetivo de esta aplicación es proporcionar un entorno práctico para que los usuarios puedan generar datos simulados y utilizarlos en proyectos de análisis de datos. Al generar ventas simuladas con diferentes parámetros y ciudades, los usuarios pueden:

- Practicar la limpieza y manipulación de datos 📊.
- Analizar tendencias y patrones de ventas 📈.
- Crear visualizaciones y reportes utilizando herramientas de análisis de datos como Pandas, Matplotlib, Seaborn, etc.

---

## 🤝 **Contribuciones**

Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio y enviar un pull request con tus mejoras o sugerencias 💡.

---

## 📜 **Licencia**

Este proyecto está bajo la Licencia MIT 📝.

---

¡Disfruta del análisis de datos con esta herramienta y empieza a aprender de manera divertida y práctica! 🎉
