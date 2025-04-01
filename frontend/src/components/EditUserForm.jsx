import React, { useState, useEffect } from "react";
import axios from "axios";

const EditUserForm = ({ userId, onClose, onSave }) => {
  const [userData, setUserData] = useState({
    name: "",
    email: "",
    tel: "",
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Obtener los datos del usuario para editar
  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/users/api/${userId}/`)
      .then((response) => {
        setUserData(response.data);
        setLoading(false);
      })
      .catch((err) => {
        setError("Error al cargar los datos");
        setLoading(false);
      });
  }, [userId]);

  // Manejo del formulario de edición
  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const isConfirmed = window.confirm("¿Seguro que deseas actualizar al usuario?");
    if (isConfirmed) {
      axios
        .put(
          `http://127.0.0.1:8000/users/api/${userId}/`,
          userData,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
          }
        )
        .then((response) => {
          alert("Usuario actualizado correctamente.");
          onSave(); // Actualizamos la tabla después de la edición
          onClose(); // Cerramos el formulario
        })
        .catch((err) => {
          alert("Error al actualizar el usuario.");
        });
    }
  };

  if (loading) return <div>Cargando...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="modal fade show" style={{ display: "block" }} aria-modal="true">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Editar Usuario</h5>
            <button type="button" className="btn-close" onClick={onClose}></button>
          </div>
          <div className="modal-body">
            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="name" className="form-label">
                  Nombre
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="name"
                  name="name"
                  value={userData.name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="email" className="form-label">
                  Email
                </label>
                <input
                  type="email"
                  className="form-control"
                  id="email"
                  name="email"
                  value={userData.email}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="tel" className="form-label">
                  Teléfono
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="tel"
                  name="tel"
                  value={userData.tel}
                  onChange={handleChange}
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary">
                Guardar cambios
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EditUserForm;
