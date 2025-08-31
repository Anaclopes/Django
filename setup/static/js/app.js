const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

// Função para verificar a URL e mostrar a tela correta
function showCorrectForm() {
    // Pega o caminho da URL
    const path = window.location.pathname;

    // Se a URL for de cadastro, adiciona a classe 'active'
    if (path.includes('/cadastro')) {
        wrapper.classList.add('active');
    } else {
        // Se a URL for de login, remove a classe 'active'
        wrapper.classList.remove('active');
    }
}

// Chama a função quando a página carregar
window.onload = showCorrectForm;

// Adiciona os eventos de clique para mudar entre as telas
registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

