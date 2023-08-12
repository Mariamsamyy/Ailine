const product = [
    {
        id: 1,
        image: './photos/EcoOneWay.png',
        title: 'Economy - One Way',
        price: 160,
},

{
    id: 2,
    image: './photos/EcoRound.png',
    title: 'Economy - Round Trip',
    price: 190,
},

{
    id: 3,
    image: './photos/BusOneWay.png',
    title: 'Business Class - One Way',
    price: 220,
},
{
    id: 4,
    image: './photos/BusRound.png',
    title: 'Business Class - Round Trip',
    price: 230,
},
{
    id: 5,
    image: './photos/EcoDirect.png',
    title: 'Economy - Direct Trip',
    price: 270,
},
{
    id: 6,
    image: './photos/BusDirect.png',
    title: 'Business - Direct Trip',
    price: 210,
},

];

const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "$ "+total+".00";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>$ ${price}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}
