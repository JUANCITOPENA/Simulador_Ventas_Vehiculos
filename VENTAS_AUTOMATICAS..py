
import random
import json
from faker import Faker
from datetime import datetime, timedelta
import streamlit as st

fake = Faker()

# Definición de ciudades
ciudades = {
    "Santo Domingo": {"codigo": "SDQ", "lat": 18.4861, "lon": -69.9312},
    "Santiago": {"codigo": "STI", "lat": 19.4500, "lon": -70.7000},
    "La Romana": {"codigo": "LRQ", "lat": 18.4333, "lon": -68.9667},
    "San Francisco de Macorís": {"codigo": "SFM", "lat": 19.3000, "lon": -70.2500},
    "Puerto Plata": {"codigo": "POP", "lat": 19.7953, "lon": -70.6944},
    "Moca": {"codigo": "MCQ", "lat": 19.3833, "lon": -70.5167},
    "Boca Chica": {"codigo": "BCQ", "lat": 18.4475, "lon": -69.6067},
    "Higüey": {"codigo": "HQG", "lat": 18.6153, "lon": -68.7072},
    "Nagua": {"codigo": "NGQ", "lat": 19.3833, "lon": -69.8500},
    "San Pedro de Macorís": {"codigo": "SPM", "lat": 18.4500, "lon": -69.3000},
    "Barahona": {"codigo": "BRH", "lat": 18.2194, "lon": -71.1194},
    "La Vega": {"codigo": "LVE", "lat": 19.2328, "lon": -70.5344},
    "San Cristóbal": {"codigo": "SCA", "lat": 18.3667, "lon": -70.0167},
    "Villa Altagracia": {"codigo": "VAL", "lat": 18.9603, "lon": -70.2433},
    "San Juan de la Maguana": {"codigo": "SJM", "lat": 18.8200, "lon": -71.1394},
    "Dajabón": {"codigo": "DAJ", "lat": 19.5553, "lon": -71.6844},
    "Azua": {"codigo": "AZU", "lat": 18.4344, "lon": -70.7356},
    "Constanza": {"codigo": "CON", "lat": 18.9214, "lon": -70.8956},
    "Sabaneta": {"codigo": "SAB", "lat": 18.5897, "lon": -71.2797},
    "Punta Cana": {"codigo": "PUC", "lat": 18.5810, "lon": -68.3749},
    "Pedernales": {"codigo": "PED", "lat": 18.1375, "lon": -71.7628},
    "Bani": {"codigo": "BAN", "lat": 18.2711, "lon": -70.3206},
    "Montecristi": {"codigo": "MTC", "lat": 19.8028, "lon": -71.6642},
    "Cotuí": {"codigo": "CTU", "lat": 19.0297, "lon": -70.2322},
    "San José de Ocoa": {"codigo": "SJO", "lat": 18.4731, "lon": -70.8839},
    "Jarabacoa": {"codigo": "JAR", "lat": 19.0853, "lon": -70.6792},
    "Hato Mayor": {"codigo": "HTM", "lat": 18.6439, "lon": -69.2767},
    "La Altagracia": {"codigo": "LAG", "lat": 18.5644, "lon": -68.3767},
    "Santiago Rodríguez": {"codigo": "SRO", "lat": 19.2217, "lon": -71.1647}
}


# Datos de vehículos

vehiculos = [
    {
      "codigo": 1001,
      "tipo": "Sedán 🚗",
      "modelo": "Toyota Corolla",
      "caracteristicas": "5 asientos, motor de 2.0L",
      "imagen": "https://di-uploads-pod7.dealerinspire.com/toyotaofnorthmiami/uploads/2022/10/2023-GR-Corolla-1.png",
      "numeroPuertas": 4,
      "motor": "2.0L",
      "combustible": "Gasolina",
      "categoria": "Económico",
      "precio": 23500
    },
    {
      "codigo": 1002,
      "tipo": "SUV 🚙",
      "modelo": "Honda CR-V",
      "caracteristicas": "7 asientos, tracción en las 4 ruedas",
      "imagen": "https://vehicle-images.dealerinspire.com/stock-images/chrome/7b86c6e9e60a2b8f14fd207fe964e40e.png",
      "numeroPuertas": 4,
      "motor": "2.4L",
      "combustible": "Gasolina",
      "categoria": "Intermedio",
      "precio": 32000
    },
    {
      "codigo": 1003,
      "tipo": "Deportivo 🏎️",
      "modelo": "Ford Mustang",
      "caracteristicas": "Potente motor V8, diseño aerodinámico",
      "imagen": "https://platform.cstatic-images.com/in/v2/stock_photos/6fc391c8-2e8b-4854-b84c-3c94c431fb19/ca5e1b68-4c6b-403b-b95a-a77a6f529da5.png",
      "numeroPuertas": 2,
      "motor": "V8",
      "combustible": "Gasolina",
      "categoria": "Deportivo Premium",
      "precio": 45000
    },
    {
      "codigo": 1004,
      "tipo": "Compacto 🚗",
      "modelo": "Volkswagen Golf",
      "caracteristicas": "4 asientos, económico y versátil",
      "imagen": "https://di-uploads-pod20.dealerinspire.com/hendrickvwfrisco/uploads/2023/02/mlp-img-top-2023-golf-r-temp.png",
      "numeroPuertas": 4,
      "motor": "1.8L",
      "combustible": "Gasolina",
      "categoria": "Económico",
      "precio": 25000
    },
    {
      "codigo": 1005,
      "tipo": "Camioneta 🚚",
      "modelo": "Ford Explorer",
      "caracteristicas": "Capacidad para 7 pasajeros, tracción en las 4 ruedas",
      "imagen": "https://islarentacar.net/wp-content/uploads/2021/03/explorer-2012-.0.png",
      "numeroPuertas": 4,
      "motor": "3.5L",
      "combustible": "Gasolina",
      "categoria": "SUV Premium",
      "precio": 45000
    },
    {
      "codigo": 1006,
      "tipo": "Deportivo 🏎️",
      "modelo": "Chevrolet Camaro",
      "caracteristicas": "Potente motor V8, diseño deportivo",
      "imagen": "https://chevrolet.com.ph/wp-content/uploads/2022/06/camaro-Exterior-Crush-min.png",
      "numeroPuertas": 2,
      "motor": "V8",
      "combustible": "Gasolina",
      "categoria": "Deportivo Premium",
      "precio": 42000
    },
    {
      "codigo": 1007,
      "tipo": "Sedán 🚗",
      "modelo": "Honda Civic",
      "caracteristicas": "Espacioso y eficiente en combustible",
      "imagen": "https://vehicle-images.dealerinspire.com/stock-images/chrome/7b86c6e9e60a2b8f14fd207fe964e40e.png",
      "numeroPuertas": 4,
      "motor": "1.5L",
      "combustible": "Gasolina",
      "categoria": "Económico",
      "precio": 24000
    },
    {
      "codigo": 1008,
      "tipo": "SUV 🚙",
      "modelo": "Toyota RAV4",
      "caracteristicas": "Estilo deportivo, ideal para la aventura",
      "imagen": "https://deltacomercial.com.do/cdn/modelos/rav4/43670b4254bab43b747ec25fbfdf3713.png",
      "numeroPuertas": 4,
      "motor": "2.5L",
      "combustible": "Gasolina",
      "categoria": "Intermedio",
      "precio": 33000
    },
    {
      "codigo": 1009,
      "tipo": "Hatchback 🚗",
      "modelo": "Mazda 3",
      "caracteristicas": "Diseño elegante y deportivo, excelente manejo",
      "imagen": "https://di-uploads-pod2.dealerinspire.com/headquartermazdaspanishtoggle/uploads/2016/10/2017-Mazda3-Hatchback-On-White.png",
      "numeroPuertas": 4,
      "motor": "2.0L",
      "combustible": "Gasolina",
      "categoria": "Económico",
      "precio": 25500
    },
    {
      "codigo": 1010,
      "tipo": "Pickup 🚛",
      "modelo": "Ford F-150",
      "caracteristicas": "Resistente y duradero, capacidad de remolque",
      "imagen": "https://vehicle-images.dealerinspire.com/stock-images/ford/6e8545b98972a6fc71cb5386f12ed692.png",
      "numeroPuertas": 4,
      "motor": "5.0L",
      "combustible": "Gasolina",
      "categoria": "Trabajo Premium",
      "precio": 52000
    },
    {
      "codigo": 1011,
      "tipo": "Coupé 🏎️",
      "modelo": "BMW Serie 2",
      "caracteristicas": "Lujo y rendimiento en un diseño compacto",
      "imagen": "https://corporate.sixt.com/es-es/wp-content/uploads/sites/9/2022/10/sixt.com-alquiler-de-bmw-x4-sixt.com-bmw-2er-coupe-2d-blau.png",
      "numeroPuertas": 2,
      "motor": "3.0L",
      "combustible": "Gasolina",
      "categoria": "Lujo",
      "precio": 48000
    },
    {
      "codigo": 1012,
      "tipo": "Furgoneta 🚐",
      "modelo": "Mercedes-Benz Sprinter",
      "caracteristicas": "Gran capacidad de carga, ideal para negocios",
      "imagen": "https://www.motortrend.com/uploads/sites/10/2018/04/2018-mercedes-benz-sprinter-2500-170-wb-high-roof-passenger-van-angular-front.png",
      "numeroPuertas": 4,
      "motor": "2.1L",
      "combustible": "Diesel",
      "categoria": "Comercial Premium",
      "precio": 45000
    },
    {
      "codigo": 1013,
      "tipo": "Convertible 🚗",
      "modelo": "Chevrolet Corvette",
      "caracteristicas": "Estilo clásico y potencia deslumbrante",
      "imagen": "https://d3s2hob8w3xwk8.cloudfront.net/autos-landing/chevrolet/corvette-2023/colores/AMPLIFY-TINTCOAT.png",
      "numeroPuertas": 2,
      "motor": "6.2L",
      "combustible": "Gasolina",
      "categoria": "Superdeportivo",
      "precio": 65000
    },
    {
      "codigo": 1014,
      "tipo": "SUV 🚙",
      "modelo": "BMW X5",
      "caracteristicas": "5 asientos, potente motor y tecnología avanzada",
      "imagen": "https://images.carprices.com/pricebooks_data/usa/colorized/2023/BMW/View2/X5_M/X5_M/23XK_300.png",
      "numeroPuertas": 4,
      "motor": "3.0L",
      "combustible": "Gasolina",
      "categoria": "Lujo Premium",
      "precio": 65000
    },
    {
      "codigo": 1015,
      "tipo": "Sedán 🚗",
      "modelo": "Audi A4",
      "caracteristicas": "Diseño elegante, tecnología de punta",
      "imagen": "https://images.dealer.com/ddc/vehicles/2023/Audi/A4/Sedan/perspective/front-left/2023_76.png",
      "numeroPuertas": 4,
      "motor": "2.0L",
      "combustible": "Gasolina",
      "categoria": "Lujo",
      "precio": 45000
    },
    {
      "codigo": 1016,
      "tipo": "Sedán 🚗",
      "modelo": "Mercedes-Benz C-Class",
      "caracteristicas": "Lujo y rendimiento en cada detalle",
      "imagen": "https://images.dealer.com/ddc/vehicles/2023/Mercedes-Benz/C-Class/Coupe/perspective/front-left/2023_24.png",
      "numeroPuertas": 4,
      "motor": "2.0L",
      "combustible": "Gasolina",
      "categoria": "Lujo Premium",
      "precio": 48000
    },
    {
      "codigo": 1017,
      "tipo": "Eléctrico 🚗",
      "modelo": "Tesla Model S",
      "caracteristicas": "Rendimiento eléctrico, autonomía de largo alcance",
      "imagen": "https://file.kelleybluebookimages.com/kbb/base/evox/CP/52152/2024-Tesla-Model%20S-front_52152_032_1822x709_PPSB_cropped.png",
      "numeroPuertas": 4,
      "motor": "Eléctrico",
      "combustible": "Eléctrico",
      "categoria": "Lujo Premium Eléctrico",
      "precio": 85000
    },
    {
      "codigo": 1018,
      "tipo": "Sedán 🚗",
      "modelo": "Nissan Altima",
      "caracteristicas": "Tecnología avanzada, diseño aerodinámico",
      "imagen": "https://di-uploads-pod42.dealerinspire.com/southparknissan/uploads/2023/11/2024-nissan-altima-main.png",
      "numeroPuertas": 4,
      "motor": "2.5L",
      "combustible": "Gasolina",
      "categoria": "Intermedio",
      "precio": 27000
    }
  ]


# Función para generar datos de ventas simuladas
# Función para generar datos de ventas simuladas
def generar_venta(clientes, vendedores, vehiculos, rango_fechas, cantidad_facturas):
    ventas = []
    for _ in range(cantidad_facturas):
        cliente = random.choice(clientes)
        vendedor = random.choice(vendedores)
        productos = random.sample(vehiculos, random.randint(1, 3))  # Seleccionar entre 1 y 3 vehículos
        total_venta = sum(producto["precio"] for producto in productos)  # Total de todos los productos
        cantidad_total = sum(1 for _ in productos)  # Cantidad total de vehículos en la factura
        fecha_venta = fake.date_between(start_date=rango_fechas[0], end_date=rango_fechas[1])
        
        venta_detalles = []
        for producto in productos:
            venta_detalles.append({
                "producto": producto["modelo"],
                "cantidad": 1,  # Para simplificar, usamos cantidad 1 por cada vehículo
                "total_producto": producto["precio"],
                "imagen": producto["imagen"]  # Mantener la URL de la foto
            })

        # Calcular el total general para la factura
        total_gral = sum(detalle["total_producto"] for detalle in venta_detalles)

        # Obtener una ciudad al azar para la venta (de las definidas)
        ciudad_venta = random.choice(list(ciudades.keys()))

        # Crear una factura con todos los detalles
        venta = {
            "id_venta": fake.uuid4(),
            "vendedor": vendedor,
            "cliente": cliente,
            "productos": venta_detalles,
            "total_venta": total_venta,
            "cantidad_total": cantidad_total,  # Agregar la cantidad total
            "total_gral": total_gral,  # Agregar el total general de la factura
            "fecha_venta": str(fecha_venta),
            "ciudad_venta": ciudad_venta  # Agregar la ciudad de la venta
        }
        ventas.append(venta)
    
    return ventas

# Filtros en Streamlit
st.sidebar.title('Filtros de Generación de Datos')

num_clientes = st.sidebar.slider('Número de Clientes', 1, 500, 100)
num_vendedores = st.sidebar.slider('Número de Vendedores', 1, 200, 50)
num_vehiculos = st.sidebar.slider('Número de Vehículos a Incluir', 1, len(vehiculos), len(vehiculos))
rango_fecha_inicio = st.sidebar.date_input('Fecha de Inicio', datetime(2023, 1, 1))
rango_fecha_fin = st.sidebar.date_input('Fecha de Fin', datetime(2024, 1, 1))
cantidad_facturas = st.sidebar.slider('Cantidad de Facturas', 1, 1000, 100)

# Generar los datos cuando se presiona el botón
if st.sidebar.button('Generar'):
    # Crear listas simuladas de clientes y vendedores
    clientes = [fake.name() for _ in range(num_clientes)]
    vendedores = [fake.name() for _ in range(num_vendedores)]
    
    # Generar ventas simuladas
    ventas_simuladas = generar_venta(clientes, vendedores, vehiculos[:num_vehiculos], [rango_fecha_inicio, rango_fecha_fin], cantidad_facturas)
    
    # Mostrar los resultados en el panel de la derecha
    st.title('Simulador de Ventas')
    st.write(f"Se generaron {len(ventas_simuladas)} facturas")

    for venta in ventas_simuladas:
        st.write(f"**Vendedor:** {venta['vendedor']} - **Cliente:** {venta['cliente']}")
        st.write(f"**Fecha de Venta:** {venta['fecha_venta']}")
        st.write(f"**Ciudad de Venta:** {venta['ciudad_venta']}")  # Mostrar ciudad de venta
        
        # Mostrar los productos de la factura
        for detalle in venta["productos"]:
            st.write(f"  - **Producto:** {detalle['producto']} - **Cantidad:** {detalle['cantidad']} - **Total Producto:** ${detalle['total_producto']}")
            st.image(detalle['imagen'], width=300)  # Mostrar la foto del producto
            
        st.write(f"**Total Venta:** ${venta['total_venta']}")
        st.write(f"**Cantidad Total de Productos:** {venta['cantidad_total']}")
        st.write(f"**Total General Factura:** ${venta['total_gral']}")
        st.write("---")
    
    # Guardar los datos generados en un archivo JSON
    with open('ventas_simuladas.json', 'w') as outfile:
        json.dump(ventas_simuladas, outfile)
        
            # Botón para descargar las ventas simuladas en formato JSON
    st.download_button(
        label="Descargar ventas en formato JSON",
        data=json.dumps(ventas_simuladas, indent=4),
        file_name="ventas_simuladas.json",
        mime="application/json"
    )
