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
                    <button onclick="buyItem(this)">Buy</button`; 
                card.setAttribute("name", doc.name)
                card.setAttribute("sell_in", doc.sell_in)
                card.setAttribute("quality", doc.quality)
                section.appendChild(card);
}

function removeCards() {
    var e = document.querySelector(".inventory");
        e.innerHTML = "";
}

function wait(ms)
{
    var d = new Date();
    var d2 = null;
    do { d2 = new Date(); }
    while(d2-d < ms);
}

function loadItems() {
    removeCards();
    fetch('http://0.0.0.0:4000/inventory')
        .then(response => response.json()) //response to JSON
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

let form = document.querySelector('.add-del-item');
form.add.addEventListener('click', addItem)

function addItem(e) {
    e.preventDefault();

    let data = {
        name: form.elements.name.value,
        sell_in: form.elements.sell_in.value,
        quality: form.elements.quality.value,

    };

    fetch('http://0.0.0.0:4000/item', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then((response) => {
            if (response.ok) {
                console.log("Response OK Status:", response.status);
                console.log("Reponse OK status text:", response.statusText);
            } else {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText);
            }
        })
        .catch((error) => {
            console.log(error.message);
        });
    wait(500);
    loadItems();
}

form.delete.addEventListener('click', deleteItem);

function deleteItem(e) {
    e.preventDefault();
    
    let data = { 
        name: form.elements.name.value,            
        sell_in: form.elements.sell_in.value,
        quality: form.elements.quality.value 

    };

    fetch('http://0.0.0.0:4000/item', {
        method: 'DELETE',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then((response) => {
            if (response.ok) {
                console.log("Response OK Status:", response.status);
                console.log("Reponse OK status text:", response.statusText);
            } else {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText);
            }
        })
        .catch((error) => {
            console.log(error.message);
        });
    wait(500);
    loadItems();
}

let filterForm = document.querySelector('.filter-item');
filterForm.filter.addEventListener('click', filterItem);

function filterItem(e) {
    e.preventDefault();
    
    let property = document.getElementById("property").value;
    let value = document.getElementById("itemValue").value;
    
    removeCards();
    fetch(`http://0.0.0.0:4000/item/${property}/${value}`)
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

function updateQuality() {
    removeCards();
    fetch('http://0.0.0.0:4000/update_quality')
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

function getPersonalInventory(e) {
    e.preventDefault();
    removeCards();

    let data = {
        user_name: formPersonalInventory.elements.name.value,
        password: formPersonalInventory.elements.password.value
    };

    fetch('http://0.0.0.0:4000/user/inventory', {
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

function buyItem(button){
    let item = button.parentElement;
    let user = prompt("Introduce your user name:");
    if (user===null) {
        return;
    }
    let password = prompt(`Introduce the password for the user ${user}`)
    if (password===null) {
        return;
    }

    let data = {
        user_name: user,
        password: password,
        name: item.getAttribute("name"),
        sell_in: item.getAttribute("sell_in"),
        quality: item.getAttribute("quality")
    };

    fetch('http://0.0.0.0:4000/buy', {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json()) 
        .then(data => {
                alert(data.message)
            }
        )
        .catch(error => console.log('It was an error: ' + error.message))
    wait(500);
    loadItems();
}
