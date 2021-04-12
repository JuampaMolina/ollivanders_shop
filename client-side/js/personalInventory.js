var ip = 'http://127.0.0.1:5000'

const section = document.querySelector('.inventory');

function makeCards(doc){
    const card = document.createElement('div');
                card.className = 'item-card'
                card.innerHTML += `
                    <h3>${doc.name}</h3>
                    <i class="fas fa-hat-wizard"></i>
                    <div class="properties">
                        <h4>Sell In: ${doc.sell_in}</h4>
                        <h4>Quality: ${doc.quality}</h4>
                    </div>
                `;
                section.appendChild(card);
}

function removeCards() {
    var e = document.querySelector(".inventory");
        e.innerHTML = "";
}

let formPersonalInventory = document.querySelector('.personal-inventory');
formPersonalInventory.search.addEventListener('click', getPersonalInventory);

function getPersonalInventory(e) {
    e.preventDefault();
    removeCards();

    let data = {
        user_name: formPersonalInventory.elements.name.value,
        password: formPersonalInventory.elements.password.value
    };

    fetch(`${ip}/user/inventory`, {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            if (Array.isArray(data)) {
                data.forEach(doc => {
                    makeCards(doc);
                });
            } else {
                alert(data.message)
            }
        })
        .catch(error => console.log('It was an error: ' + error.message))

}
