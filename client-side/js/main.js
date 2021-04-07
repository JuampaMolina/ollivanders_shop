const section = document.querySelector('.parent');

function loadItems() {
    removeCards();
    fetch('http://127.0.0.1:5000/inventory')
        .then(response => response.json()) //response to JSON
        .then(data => {
            data.forEach(doc => {
                makeCards(doc);
            });
        })
        .catch(error => console.log('It was an error: ' + error.message))
}

function updateQuality() {
    removeCards();
    fetch('http://127.0.0.1:5000/update_quality')
        .then(response => response.json()) //response to JSON
        .then(data => {
            data.forEach(doc => {
                makeCards(doc);
            });
        })
        .catch(error => console.log('It was an error: ' + error.message))
}

function makeCards(doc){
    const card = document.createElement('div');
                card.className = 'card'
                card.innerHTML += `
                    <h3>${doc.name}</h3>
                    <h4>Sell In: ${doc.sell_in}</h4>
                    <h4>Quality: ${doc.quality}</h4>
                `;
                section.appendChild(card);
}

function removeCards() {
    var e = document.querySelector(".parent");
        e.innerHTML = "";
}
