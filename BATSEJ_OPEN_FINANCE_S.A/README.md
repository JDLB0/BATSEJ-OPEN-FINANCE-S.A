# BATSEJ Open Finance - Sistema de Cálculo de Comisiones

Este sistema permite calcular comisiones para diferentes empresas basándose en sus peticiones API, genera reportes en Excel y los envía por correo electrónico utilizando Outlook.

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- Git
- Microsoft Outlook (para el envío de correos)
- Privilegios de administrador (para algunas instalaciones)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JDLB0/BATSEJ-OPEN-FINANCE-S.A.git
cd BATSEJ-OPEN-FINANCE-S.A
```



## 📁 Estructura del Proyecto

```
BATSEJ-OPEN-FINANCE-S.A/
├── BATSEJ_OPEN_FINANCE_S.A/
│   ├── data/
│   │   └── database.sqlite
│   └── src/
│       ├── calcular_comision.py
│       ├── cargar_db.py
│       ├── enviar_correo.py
│       ├── generar_reportes.py
│       ├── explorar_base_datos.py
│       ├── inspeccionar_tablas.py
│       └── main.py
├── Salidas/
├── requirements.txt
└── README.md
```

## ⚙️ Configuración

1. Asegúrate de que la base de datos SQLite esté en la ruta correcta:
   ```
   BATSEJ_OPEN_FINANCE_S.A/data/database.sqlite
   ```

2. Verifica que Microsoft Outlook esté configurado con tu cuenta de correo.

3. Asegúrate de que la carpeta `Salidas` exista en el directorio raíz del proyecto.

## 🔧 Uso

1. Ejecutar el programa principal Comisionador_BATSEJ.bat:


2. Seguir las opciones del menú:
   - Opción 1: Cargar datos de la base de datos
   - Opción 2: Calcular comisiones
   - Opción 3: Generar reporte en Excel
   - Opción 4: Enviar reporte por correo
   - Opción 5: Salir

## 📦 Dependencias Principales

Crear un archivo `requirements.txt` con las siguientes dependencias:

```
pandas==2.0.0
xlsxwriter==3.1.2
pywin32==306
```

## 🔍 Exploración de Datos

Para explorar la estructura de la base de datos:

```bash
python src/explorar_base_datos.py
python src/inspeccionar_tablas.py
```

## 📄 Reglas de Negocio

Las comisiones se calculan según las siguientes reglas por empresa:

- **Innovexa Solutions**: 300 por petición exitosa
- **NexaTech Industries**: 
  - 0-10000: 250 por petición
  - 10001-20000: 200 por petición
  - 20001+: 170 por petición
- **QuantumLeap Inc.**: 600 por petición exitosa
- **Zenith Corp.**:
  - 0-22000: 250 por petición
  - 22001+: 130 por petición
  - Descuento 5% si peticiones no exitosas > 6000
- **FusionWave Enterprises**: 
  - 300 por petición exitosa
  - Descuento 5% si peticiones no exitosas entre 2500-4500
  - Descuento 8% si peticiones no exitosas > 4500

## 🛠️ Solución de Problemas Comunes

1. **Error al conectar con la base de datos**
   - Verificar que la ruta de la base de datos sea correcta
   - Comprobar permisos de lectura

2. **Error al enviar correos**
   - Verificar que Outlook esté instalado y configurado
   - Comprobar la conexión a internet
   - Verificar que el correo destino sea válido

3. **Error al generar reportes**
   - Verificar que la carpeta `Salidas` exista
   - Comprobar que no haya archivos abiertos con el mismo nombre

## 👥 Contribuir

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas Adicionales

- Los reportes se generan con timestamp en el nombre para evitar sobrescrituras
- El sistema está configurado para procesar datos de julio y agosto de 2024
- Se requiere Outlook instalado para la funcionalidad de envío de correos

## 📧 Contacto

Tu Nombre - [tu.email@ejemplo.com](mailto:tu.email@ejemplo.com)

Link del Proyecto: [https://github.com/tu-usuario/BATSEJ-OPEN-FINANCE-S.A](https://github.com/tu-usuario/BATSEJ-OPEN-FINANCE-S.A)
