##########################################
#################CONFIGURACIÓN GENERAL#################
##########################################
#Multiplicador de superresolución
scale=2
#Ruta de parámetros, se puede cambiar
#Versión con reducción de ruido (denoise): Si el original tiene mucho ruido y está mal comprimido, se recomienda usar; actualmente el modelo 2x soporta 3 niveles de reducción de ruido;
#Versión sin reducción de ruido (no-denoise): Si el original no tiene mucho ruido y está bien comprimido, pero quieres aumentar la resolución/nitidez/hacer mejoras generales de restauración, se recomienda usar;
#Versión conservadora (conservative): Si te preocupa perder texturas, cambiar el estilo artístico, realzar colores, en resumen, si tienes varias preocupaciones sobre que la IA deje marcas evidentes de procesamiento, se recomienda usar esta versión.
model_path2 = "weights_v3/up2x-latest-denoise3x.pth"
model_path3 = "weights_v3/up3x-latest-denoise3x.pth"
model_path4 = "weights_v3/up4x-latest-denoise3x.pth"
#half: Las tarjetas gráficas tempranas no aceleran con media precisión, pero la media precisión puede ahorrar VRAM; para tarjetas N >=serie 20, elegir True sin pensar
half=True
#tile: mientras más grande, ahorra más VRAM pero es más lento
tile=5
#cache_mode: Si la VRAM está al límite de explotar, aún puedes luchar, elige 0 o 1 (ambos sin pérdidas), 1 incrementa el tiempo 15% comparado con 0, pero ahorra más VRAM; si la VRAM claramente no puede luchar (por ejemplo, solo 2G VRAM queriendo hacer super resolución >=720P, o entrada de resolución muy alta (ej. 4K)), elige 2 o 3; 2 tiempo +25%, solo agrega 5% de error en imágenes con desenfoque de profundidad de campo; 3 incrementa tiempo 150% pero sin pérdidas
cache_mode=1
#alpha: mientras más pequeño, menor grado de restauración de IA y marcas, más borroso; mientras más grande alpha, procesamiento más intenso, más nitidez, mayor desviación de color (contraste, saturación mejorados)
#Rango ajustable: (0.7,1.3), por defecto 1 sin ajuste
alpha=1
#Modo de superresolución, video o carpeta de imágenes
mode="image"#video#image
############################################
#################CONFIGURACIÓN DE IMÁGENES#################
############################################
#0 representa el número de tarjeta, para múltiples tarjetas se pueden escribir diferentes configs en paralelo, si hay mucha VRAM pero la utilización no está llena, una tarjeta también puede abrir múltiples
#Si quieres usar CPU, llena "cpu" entre las comillas
device="cuda:0"
input_dir="input_dir1"#Ruta de imágenes de entrada
output_dir="output_dir"#Ruta de salida de imágenes con superresolución
############################################
#################CONFIGURACIÓN DE VIDEO#################
############################################
inp_path=r"C:\Users\liujing\Desktop\Z\input.mov"
opt_path=r"C:\Users\liujing\Desktop\Z\output.mp4"
#Número de hilos: hazlo según tu capacidad, si pones muy poco la utilización será baja, si pones mucho explotará la VRAM
nt=2
#Número de GPUs
n_gpu=1
#No tocar
p_sleep=(0.005,0.012)
decode_sleep=0.002
#Parámetros de codificación, no tocar si no entiendes; en términos simples, crf más bajo = alta tasa de bits y alta calidad, slower = baja velocidad de codificación y alta calidad + más demandante de CPU, si la CPU no es suficiente deberías bajar el nivel, por ejemplo slow, medium, fast, faster
encode_params=['-crf', '21', '-preset', 'medium']