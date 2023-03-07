

function ver_password(idInput){
    let inputPassword = document.getElementById(idInput);
    inputPassword.type = 'text';
}

function ocultar_password(idInput){
    let inputPassword = document.getElementById(idInput);
    inputPassword.type = 'password';
}


function copiar_password(idInput){
    let password = document.getElementById(idInput).value;
    navigator.clipboard.writeText(password)
        .then(() => {
            alert('Contraseña copiada con exito');
        });
}