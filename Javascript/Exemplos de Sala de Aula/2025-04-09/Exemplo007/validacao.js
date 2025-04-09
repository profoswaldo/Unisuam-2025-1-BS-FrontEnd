// Adiciona um evento ao botão de envio do formulário
document.getElementById('meuFormulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário automaticamente

    // Limpa a mensagem de erro anterior
    let mensagemErro = document.getElementById('mensagemErro');
    mensagemErro.textContent = ''; // Limpa qualquer texto de erro anterior

    // Pega os valores dos campos do formulário
    let nome = document.getElementById('nome').value; // Obtém o valor do campo nome
    let email = document.getElementById('email').value; // Obtém o valor do campo email
    let senha = document.getElementById('senha').value; // Obtém o valor do campo senha

    // Simples verificação para garantir que os campos não estejam vazios
    if (nome === '' || email === '' || senha === '') {
        mensagemErro.textContent = 'Por favor, preencha todos os campos obrigatórios.'; // Mostra a mensagem de erro
        return; // Interrompe o envio se houver erro
    }

    // Verifica se a senha tem pelo menos 6 caracteres
    if (senha.length < 6) {
        mensagemErro.textContent = 'A senha deve ter no mínimo 6 caracteres.'; // Mostra a mensagem de erro
        return; // Interrompe o envio se houver erro
    }

    // Verifica se o email contém um "@" (básico)
    if (email.indexOf('@') === -1) {
        mensagemErro.textContent = 'Por favor, insira um email válido.'; // Mostra a mensagem de erro
        return; // Interrompe o envio se houver erro
    }

    // Se tudo estiver correto, mostra uma mensagem de sucesso
    alert('Formulário enviado com sucesso!');
});
