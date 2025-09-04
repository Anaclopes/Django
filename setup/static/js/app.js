document.addEventListener('DOMContentLoaded', () => {
  const bodyId = document.body.id;

  if (bodyId === "auth") {
    const wrapper = document.querySelector('.wrapper');
    const loginLink = document.querySelector('.login-link');
    const registerLink = document.querySelector('.register-link');

    // Verifica a URL atual e aplica a classe
    function showCorrectForm() {
      const path = window.location.pathname;
      if (path.includes('/cadastro')) {
        wrapper.classList.add('active');
      } else {
        wrapper.classList.remove('active');
      }
    }

    // Executa logo ao carregar
    showCorrectForm();

    // Clique em "Sign up"
    registerLink.addEventListener('click', (e) => {
      e.preventDefault(); // impede reload
      wrapper.classList.add('active');
      history.pushState({}, "", "/cadastro"); // troca a URL sem recarregar
    });

    // Clique em "Login"
    loginLink.addEventListener('click', (e) => {
      e.preventDefault();
      wrapper.classList.remove('active');
      history.pushState({}, "", "/login");
    });

    // Suporte ao botão voltar/avançar do navegador
    window.addEventListener('popstate', showCorrectForm);

  } else if (bodyId === "deslog") {
    document.addEventListener("scroll", function () {
      const navbar = document.getElementById("mainNavbar");
      const progressoSection = document.querySelector(".container");

      if (progressoSection) {
        const progressoTop = progressoSection.getBoundingClientRect().top;

        if (progressoTop <= 0) {
          navbar.style.display = "flex";
        } else {
          navbar.style.display = "none";
        }
      }
    });
  }
});

// 1. Seleciona todas as divs com a classe 'alert'
    const alertMessages = document.querySelectorAll('.alert');

    // 2. Para cada mensagem de alerta encontrada...
    alertMessages.forEach(function(message) {
        // 3. ...define um temporizador de 5 segundos para escondê-la
        setTimeout(function() {
            message.style.display = 'none';
        }, 5000); // 5000 milissegundos = 5 segundos. Você pode mudar esse valor.
    });