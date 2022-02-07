const plus = document.querySelectorAll('.plus') 
const minus = document.querySelectorAll('.minus');
const close = document.querySelectorAll('.delete');

const UpdateQuantity = async  (type, item) =>{
    const product = item.getAttribute('data-product');

    await fetch('/cart/', {
        method: 'POST',
        headers: {
        'Accept' :'application/json',
        'Content-Type':  'application/json',
          'X-CSRFTOKEN' : csrftoken,
        },
        body:JSON.stringify({'form_type': type, 'product' : product})
    });
}

plus.forEach(element =>{
    element.addEventListener('click',(e) =>{
        const elementContainer = element.parentNode.parentNode
        const total = elementContainer.parentNode.querySelector('.total')
        const price = elementContainer.parentNode.querySelector('.price').innerHTML
        let quantity = elementContainer.querySelector('.quantity').innerHTML;
        elementContainer.querySelector('.quantity').innerHTML = Number(quantity) + 1
        total.innerHTML = (Number(quantity) +1) * Number(price) + '.00'
        UpdateQuantity('increase_qunatity', element) // passing the element as product instance
    })
})

minus.forEach(element =>{
    element.addEventListener('click',(e) =>{
        const elementContainer = element.parentNode.parentNode
        let quantity = elementContainer.querySelector('.quantity').innerHTML;
        if (Number(quantity) <= 1) return
        const price = elementContainer.parentNode.querySelector('.price').innerHTML
        const total = elementContainer.parentNode.querySelector('.total')
        elementContainer.querySelector('.quantity').innerHTML = Number(quantity) - 1
        total.innerHTML = (Number(quantity) -1) * Number(price) + '.00'
        UpdateQuantity('decrease_qunatity', element) // passing the element as product instance
    })
})

close.forEach(element =>{
    element.addEventListener('click',(e) =>{
        UpdateQuantity('delete_cart', element) // passing the element as product instance
        element.parentNode.remove();
    })
})
