# 🚀 **Proyecto de Red Neuronal en Keras - MNIST** 🤖

¡Bienvenido a este proyecto de aprendizaje profundo! En este repositorio, se construye una **Red Neuronal** utilizando **Keras** y **TensorFlow** para reconocer dígitos manuscritos del conjunto de datos **MNIST**.

---

## 📂 **Estructura del Proyecto**

tarea2/ │── main.py # Punto de entrada para ejecutar el entrenamiento │── src/ # Carpeta que contiene los módulos │ ├── data.py # Carga y preprocesa los datos │ ├── model.py # Define el modelo de red neuronal │ ├── train.py # Contiene la función para entrenar el modelo


---

## 🧩 **Descripción del Proyecto**

Este proyecto está organizado de forma modular para facilitar su comprensión y mantenimiento. Cada archivo tiene una responsabilidad bien definida:

### 1. **`main.py`**  
   El **punto de entrada** del proyecto. Aquí se orquesta todo el flujo: cargamos los datos, construimos el modelo y entrenamos la red neuronal.

### 2. **`src/data.py`**  
   Contiene la función `load_data()`, que se encarga de cargar el conjunto de datos **MNIST**, normalizarlo y convertir las etiquetas a formato **one-hot encoding**.

### 3. **`src/model.py`**  
   Define el modelo de la red neuronal utilizando **Keras**. El modelo tiene una capa densa de 128 neuronas con activación **ReLU** y una capa de salida con 10 neuronas (una por cada dígito) utilizando **softmax** para clasificación multiclase.

### 4. **`src/train.py`**  
   Contiene la función `train_model()` que entrena el modelo utilizando el conjunto de entrenamiento, durante 5 épocas.

---

## 📜 **Requisitos**

Antes de comenzar, asegúrate de tener instaladas las siguientes dependencias:

- **TensorFlow**: Para construir y entrenar el modelo de aprendizaje profundo.
- **Keras**: API de alto nivel para redes neuronales.
- **NumPy**: Para manejar matrices y realizar operaciones matemáticas.
- **Matplotlib**: Para visualizar las imágenes de los dígitos del conjunto de datos **MNIST**.

Para instalar todas las dependencias, simplemente ejecuta el siguiente comando:

```bash
pip install numpy keras tensorflow matplotlib

🚀 Cómo Ejecutar el Proyecto
Sigue estos pasos para ejecutar el código en tu máquina:

1. Instalar las Dependencias
Primero, instala todas las librerías necesarias:

pip install numpy keras tensorflow matplotlib

2. Navegar a la Carpeta del Proyecto
En tu terminal, ve al directorio donde has descargado el proyecto:

cd C:/Users/LapOneMX/tarea2

3. Ejecutar el Script Principal
Finalmente, ejecuta el archivo main.py para iniciar el entrenamiento del modelo:

python main.py


El script descargará automáticamente el conjunto de datos MNIST, construirá la red neuronal, y la entrenará durante 5 épocas.

🔍 ¿Qué Puedes Esperar?
Cuando ejecutes el script, verás el progreso del entrenamiento, incluyendo la pérdida y la precisión del modelo en cada época.

🏆 Resultados
Al finalizar el entrenamiento, el modelo estará listo para reconocer los dígitos del conjunto MNIST y podrá clasificarlos con alta precisión.


🤝 Contribuciones
¡Me encantaría ver mejoras y contribuciones de tu parte! Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama para tus cambios.
Envía un pull request con una descripción detallada de tus mejoras.
📝 Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

🌟 Gracias por visitar este proyecto 🌟
Espero que disfrutes explorando cómo construir y entrenar una red neuronal con Keras. ¡No dudes en contactarme si tienes preguntas o sugerencias!

"La inteligencia artificial no es el futuro, es el presente. ¡Haz que tu código sea increíble!" ✨