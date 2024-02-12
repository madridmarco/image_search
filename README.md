# image_search

## Introducción
Este proyecto tiene como objetivo la creación de una aplicación basada en microservicios, haciendo uso de la tecnología Docker para garantizar la portabilidad y reproducibilidad de los servicios. La aplicación está diseñada para la gestión de imágenes, permitiendo a los usuarios cargar fotos que serán etiquetadas automáticamente. Estas imágenes se almacenan en una carpeta específica, mientras que la información asociada se registra en una base de datos central. La base de datos contiene los paths de las imágenes y las etiquetas asignadas, facilitando la posterior búsqueda de imágenes por etiquetas específicas. Los microservicios implementados incluyen una API desarrollada en Flask y servida mediante Waitress, así como una base de datos MySQL 8.0 para el almacenamiento estructurado de información relacionada con las imágenes. Este enfoque microservicios ofrece flexibilidad y escalabilidad en la aplicación, permitiendo una gestión eficiente de imágenes y etiquetas.




<img width=800 src="architecture/architecture.png"></img>