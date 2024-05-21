document.addEventListener("DOMContentLoaded", function() {
    // Agregar al carrito
    const carrito = document.getElementById('carrito');
    const listaProductos = document.getElementById('lista-1');
    const listaCarrito = document.getElementById('lista-carrito').querySelector('tbody');
    const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

    listaProductos.addEventListener('click', agregarProducto);
    carrito.addEventListener('click', eliminarProducto);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);

    function agregarProducto(e) {
        e.preventDefault();
        if (e.target.classList.contains('agregar-carrito')) {
            const producto = e.target.parentElement.parentElement;
            leerDatosProducto(producto);
        }
    }

    function leerDatosProducto(producto) {
        const infoProducto = {
            imagen: producto.querySelector('img').src,
            titulo: producto.querySelector('h3').textContent,
            precio: producto.querySelector('.precio').textContent,
            id: producto.querySelector('a').getAttribute('data-id')
        }
        insertarCarrito(infoProducto);
    }

    function insertarCarrito(producto) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                <img src="${producto.imagen}" width=100>
            </td>
            <td>${producto.titulo}</td>
            <td>${producto.precio}</td>
            <td>
                <a href="#" class="borrar-producto" data-id="${producto.id}">X</a>
            </td>
        `;
        listaCarrito.appendChild(row);
    }

    function eliminarProducto(e) {
        e.preventDefault();
        if (e.target.classList.contains('borrar-producto')) {
            e.target.parentElement.parentElement.remove();
        }
    }

    function vaciarCarrito(e) {
        e.preventDefault();
        while (listaCarrito.firstChild) {
            listaCarrito.removeChild(listaCarrito.firstChild);
        }
    }

    // Redirigir al checkout
    const pagarBtn = document.getElementById('pagar');
    pagarBtn.addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = '/checkout/';
    });
});
