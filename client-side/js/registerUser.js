var ip = 'http://127.0.0.1:5000'

let formRegisterUser = document.querySelector('.register-user');
formRegisterUser.register.addEventListener('click', registerUser);

function registerUser(e) {
    e.preventDefault();

    let data = {
        user_name: formRegisterUser.elements.name.value,
        email: formRegisterUser.elements.email.value,
        password: formRegisterUser.elements.password.value
    };

    fetch(`${ip}/user`, {
        method: 'POST',
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

}
