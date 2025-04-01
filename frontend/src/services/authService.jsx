import axios from "axios";

const API_URL = "http://127.0.0.1:8000/users/token/";

export const login = async (email, password) => {
  const response = await axios.post(API_URL, { email, password });
  if (response.data.access) {
    localStorage.setItem("accessToken", response.data.access);
    localStorage.setItem("refreshToken", response.data.refresh);
  }
  alert("Login exitoso");
  alert("Token de acceso: " + response.data.access);
  alert("Token de refresco: " + response.data.refresh);
  return response.data;
};

export const logout = () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
};

//To do
//crear un metodo que jale la informacion del usuario
