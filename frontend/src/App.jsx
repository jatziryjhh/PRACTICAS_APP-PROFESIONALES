import { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import axios from "axios";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import AboutUs from "./pages/AboutUs";
import NotFound from "./pages/404";
import CustomUserForm from "./components/NewUser";
import { AnimatePresence } from "framer-motion";
import "bootstrap/dist/css/bootstrap.min.css";
import UserDataTable from "./components/UserDataTable"; // Importa el componente UserDataTable

const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/" element={<Home />} />
        <Route path="/form" element={<CustomUserForm />} />
        <Route path="/users/table" element={<UserDataTable />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </AnimatePresence>
  );
};

// Home component
function Home() {
  const [data, setData] = useState([]); // Estado para los usuarios
  const [error, setError] = useState(null); // Estado para manejar errores
  const [loading, setLoading] = useState(true); // Estado para saber si los datos están cargando
 
  const sesion = localStorage.getItem("accessToken");

  // Hacer la solicitud para obtener los datos de usuarios
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/") // Endpoint de tu API
      .then((response) => {
        setData(response.data); // Guardamos los datos obtenidos
        setLoading(false); // Ya no estamos cargando
      })
      .catch((error) => {
        setError("Error al cargar los datos: " + error); // Si hay un error, lo guardamos
        setLoading(false); // Ya no estamos cargando
      });
  }, []);

  // Mientras los datos están cargando
  if (loading) {
    return <div>Cargando...</div>;
  }

  // Si ocurre un error
  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Datos de la API desde Django</h1>
      <h2>{sesion}</h2>
      {/* Pasamos los datos y el estado de carga al componente UserDataTable */}
      <UserDataTable data={data} loading={loading} />
    </div>
  );
}

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <div className="row">
          <div className="col">
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;