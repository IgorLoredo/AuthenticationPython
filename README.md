# AuthenticationPython


http://localhost:5001/teste

# # Construir a imagem Docker
docker build -t my-python-app .

# # Executar o container Docker
 docker run -p 5000:5000 my-python-app



@app.route('/login', methods=['POST']) - Esta rota aceita solicitações POST para fazer login de um usuário. O nome de usuário e a senha devem ser fornecidos no corpo da solicitação. Se a autenticação for bem-sucedida, o usuário será logado e a função retornará uma mensagem de sucesso. Se a autenticação falhar, a função retornará uma mensagem de erro.

@app.route('/logout') - Esta rota desloga o usuário atualmente logado e retorna uma mensagem de sucesso. Se nenhum usuário estiver logado, a função retornará uma mensagem de erro.

@login_manager.user_loader - Esta função é usada pelo Flask-Login para carregar um usuário a partir de um ID de usuário. A função aceita um ID de usuário como argumento e retorna o usuário correspondente, se existir. Se o usuário não existir, a função retornará None.

class User(UserMixin) - Esta é a classe de modelo do usuário. Cada usuário tem um ID, que é usado pelo Flask-Login para identificar o usuário. A classe herda de UserMixin, que é uma classe base fornecida pelo Flask-Login que inclui implementações padrão para várias funções de usuário, como is_authenticated e is_active.

CORS(app) - Esta linha permite que qualquer domínio faça solicitações para o seu aplicativo. Isso é feito incluindo o cabeçalho Access-Control-Allow-Origin em todas as respostas do seu aplicativo.