async function requestAppVersion(){
  let version = await eel.requestAppVersion()();
  return version;
}

// Requisição de login
async function requestLogin(){
  Login_toggleLoginButtonSpinner();
  let funcional = document.getElementById("funcionalInput").value;
  let senha = document.getElementById("passwordInput").value;
  let responseLogin = await eel.requestLogin(funcional, senha)();
  Login_requestLoginReaction(responseLogin);
}

// Requisição das informações do usuário logado
async function requestUserData(){
  let responseUserData = await eel.requestUserData()();
  return JSON.parse(responseUserData);
}