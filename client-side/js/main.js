const section = document.querySelector('.parent');

function loadItems() {
    fetch('http://127.0.0.1:5000/inventory')
        .then(response => response.json()) //response to JSON
        .then(data => {
            data.forEach(doc => {
                const card = document.createElement('div');
                card.className = 'card'
                card.innerHTML += `
                    <h3>${doc.name}</h3>
                    <h4>Sell In: ${doc.sell_in}</h4>
                    <h4>Quality: ${doc.quality}</h4>
                `;
                section.appendChild(card);
            });
        })
        .catch(error => console.log('It was an error: ' + error.message))
}

loadItems();
