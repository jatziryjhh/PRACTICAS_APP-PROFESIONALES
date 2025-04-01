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

/// Método para refrescar el token
export const refreshToken = async () => {
  const refreshToken = localStorage.getItem("refreshToken");
  if (refreshToken) {
    try {
      const response = await axios.post("http://127.0.0.1:8000/users/token/refresh/", { refresh: refreshToken });
      localStorage.setItem("accessToken", response.data.access);
    } catch (error) {
      console.error("Error al refrescar el token", error);
    }
  }
};
