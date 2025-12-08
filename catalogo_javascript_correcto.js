  <script>
        // Función para mostrar categoría específica
        function showCategory(categoryId) {
            // Ocultar todas las secciones
            document.querySelectorAll('.category-section').forEach(section => {
                section.classList.remove('active');
            });

            // Mostrar la sección seleccionada
            const targetSection = document.getElementById(categoryId);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            // Actualizar botones de navegación
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });

            const activeBtn = document.querySelector(`[data-category="${categoryId}"]`);
            if (activeBtn) {
                activeBtn.classList.add('active');
            }

            // Scroll al inicio del contenido
            window.scrollTo({
                top: 100,
                behavior: 'smooth'
            });
        }

        // Event listeners para botones de navegación
        document.addEventListener('DOMContentLoaded', function() {
            // Navegación principal
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const category = this.getAttribute('data-category');
                    showCategory(category);
                });
            });

            // Botón de volver arriba
            const backToTopBtn = document.getElementById('backToTop');

            // Mostrar/ocultar botón de volver arriba
            window.addEventListener('scroll', function() {
                if (window.pageYOffset > 300) {
                    backToTopBtn.classList.add('show');
                } else {
                    backToTopBtn.classList.remove('show');
                }
            });

            // Funcionalidad del botón de volver arriba
            backToTopBtn.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });

            // Iniciar mostrando mensaje de bienvenida
            showCategory('welcome');
        });

        // Prevenir que los enlaces de productos se cierra la categoría
        document.querySelectorAll('.product-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        });
    </script>
</body>
</html>