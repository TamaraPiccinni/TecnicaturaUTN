const shopContent = document.getElementById('shopContent');

productos.forEach(producto => { 
    const content = document.createElement('div');
    content.innerHTML = `
    <img src="${producto.img}" alt="${producto.productName}">
    <h3>${producto.productName}</h3>
    <p>$${producto.price}</p>
    `;
    shopContent.appendChild(content);
});
