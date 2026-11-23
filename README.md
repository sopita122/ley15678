# Actividad 10: Conciencia digital, algoritmos y marco legal

**Laboratorio de Programación | 5.º año | 2026**

**Estudiante:** Sofia Salaberry

**Institución:** EEST N.º 1 "Eduardo Ader" - Vicente López

**Docente:** Mansilla Muñoz York Elías

---

## 1. Presentación de la actividad

Esta actividad consiste en trabajar sobre la Ley 15.678 de la Provincia de Buenos Aires, relacionada con el uso de teléfonos celulares y dispositivos digitales durante la jornada escolar.

A partir de esta normativa, se propone analizar diferentes situaciones que pueden presentarse dentro del aula y relacionarlas con los conocimientos de programación mediante el desarrollo de un algoritmo de toma de decisiones.

El trabajo incluye la elaboración de un diagrama de flujo, la resolución de un ejercicio utilizando Python y una reflexión sobre el uso responsable de la tecnología en el ámbito educativo.

## 2. Objetivos

- Comprender las principales condiciones de la normativa trabajada en la actividad.
- Reflexionar sobre el uso de celulares y redes sociales durante las clases.
- Aplicar estructuras condicionales para representar diferentes situaciones.
- Interpretar el funcionamiento de un algoritmo de toma de decisiones.
- Utilizar herramientas de programación y control de versiones para organizar la actividad.
- Relacionar los contenidos técnicos con situaciones de la vida cotidiana.

## 3. Consigna y contenidos trabajados

La actividad plantea diseñar un sistema que permita evaluar si un estudiante puede utilizar el celular dentro del aula, teniendo en cuenta las condiciones establecidas en la consigna.

Se consideran tres situaciones:

| Situación | Respuesta del sistema |
|---|---|
| El docente autoriza el uso con fines pedagógicos. | Se permite utilizar el dispositivo para estudiar. |
| Existe una emergencia familiar validada. | Se gestiona la comunicación mediante preceptoría o dirección. |
| No se cumple ninguna de las condiciones anteriores. | El celular debe permanecer guardado en la mochila. |

Además, se solicita responder tres preguntas relacionadas con la interpretación de la norma, la atención durante las clases y la aplicación de la lógica condicional.

## 4. Desarrollo del algoritmo

Para resolver el ejercicio se utiliza Python y una estructura condicional compuesta por `if`, `elif` y `else`.

El programa trabaja con dos variables booleanas:

- `autorizacion_docente`: indica si el docente permitió utilizar el celular con fines pedagógicos.
- `emergencia_familiar`: representa si existe una emergencia familiar previamente validada.

### Funcionamiento de las condiciones

**IF:** verifica si existe autorización docente. Si se cumple, muestra que el uso del dispositivo está permitido con fines pedagógicos.

**ELIF:** comprueba si existe una emergencia familiar validada cuando la primera condición no se cumple.

**ELSE:** se ejecuta cuando ninguna de las condiciones anteriores es verdadera y muestra que el dispositivo debe permanecer guardado.

De esta manera, el programa representa las diferentes decisiones mediante condiciones lógicas.

## 5. Tecnologías y herramientas utilizadas

| Herramienta | Utilización |
|---|---|
| Python | Desarrollo y ejecución del algoritmo. |
| Visual Studio Code | Escritura y edición del código. |
| Git | Control de versiones y seguimiento de los cambios. |
| GitHub | Almacenamiento del repositorio de la actividad. |
| Markdown | Elaboración de la documentación. |

## 6. Ejecución del código

Para ejecutar el archivo de Python se necesita tener instalado Python 3 y contar con un editor de código o una terminal compatible.

El archivo principal se encuentra en:

`src/ley_celulares.py`

Para ejecutarlo desde la terminal, se utiliza:

```bash
python src/ley_celulares.py
```

En Windows también se puede utilizar:

```bash
py src/ley_celulares.py
```

El programa muestra el estado de las variables y la respuesta correspondiente según las condiciones establecidas.

## 7. Pruebas realizadas

Para comprobar el funcionamiento del algoritmo, se pueden modificar los valores de las variables y observar las respuestas que devuelve el programa.

| Autorización docente | Emergencia familiar | Resultado |
|---|---|---|
| `True` | `False` | Uso permitido con fines pedagógicos. |
| `False` | `True` | Canalización institucional. |
| `False` | `False` | Celular guardado. |
| `True` | `True` | Uso permitido con fines pedagógicos. |

En el último caso, se ejecuta primero la condición `if`, ya que Python evalúa las condiciones en orden.

## 8. Organización de los archivos

Para mantener ordenada la entrega, los archivos de la actividad se distribuyen de la siguiente manera:

<pre>
ley15678/
│
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
│
├── src/
│   └── ley_celulares.py
│
├── docs/
│   └── Informe_Ley_15678.pdf
│
└── capturas/
    ├── ejecucion_autorizada.png
    ├── ejecucion_emergencia.png
    └── ejecucion_restringida.png
</pre>
