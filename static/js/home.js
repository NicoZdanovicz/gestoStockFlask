
document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('miGrafico').getContext('2d');

    // Hacer una solicitud AJAX para obtener los datos desde Flask
    fetch('/datos-json')
        .then(response => response.json())
        .then(data => {
            // 'data' contiene el objeto JSON devuelto por Flask
           

            // Preparar los datos para el gráfico de pastel
            var labels = Object.keys(data.ventasPorCategoria);
            var valores = Object.values(data.ventasPorCategoria);

            // Crear el gráfico de pastel con Chart.js
            const ctx = document.getElementById('miGrafico').getContext('2d');
            
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Cantidad de Ventas',
                        data: valores,
                        backgroundColor: getRandomColors(labels.length),

                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'left',
                            labels: {
                                color: 'white' // Color de las etiquetas de la leyenda
                            }
                        }
                    }
                }
            });

            
            // Extraer etiquetas (categorías) y valores (precio) del objeto
            const categorias = Object.keys(data.ingresosPorCategoria) ;
            const ingresos = Object.values(data.ingresosPorCategoria);

            document.getElementById("ingTotales").innerHTML = '$ ' + parseInt(data.ingresosTotales);
            document.getElementById("ingDiarios").innerHTML = '$ ' + parseInt(data.ingresosTotales/7);
            // Crear el gráfico de barras vertical con Chart.js
            const ctx1 = document.getElementById('miGraficoBarras').getContext('2d');
            new Chart(ctx1, {
                type: 'bar',
                data: {
                    labels: categorias,
                    datasets: [{
                        label: 'Ingresos por Categoría',
                        data: ingresos,
                        backgroundColor: getRandomColors(labels.length), // Color de las barras
                        borderColor: 'rgba(54, 162, 235, 1)', // Borde de las barras
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            ticks: {
                                color: 'white', // Color de las etiquetas (categorías)
                                font: {
                                    weight: 'bold' // Establecer negrita para las etiquetas
                                }
                            }
                        },
                        y: {
                            beginAtZero: true, // Iniciar el eje Y en 0
                            ticks: {
                                color: 'white', // Color de las etiquetas (ingresos)
                                callback: (value) => `${value} $` // Agregar símbolo de dólar a los ticks del eje Y
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false // Ocultar la leyenda (incluyendo los labels de clic)
                        }
                    }
                }
            });


                // Función para generar colores aleatorios
            function getRandomColors(num) {
                const colors = [];
                for (let i = 0; i < num; i++) {
                    const color = '#' + Math.floor(Math.random() * 16777215).toString(16);
                    colors.push(color);
                }
                return colors;
            }
            
        })
        .catch(error => console.error('Error al obtener datos:', error));
    
    
        
});


