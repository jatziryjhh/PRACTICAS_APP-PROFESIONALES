import React, { useState } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";
import EditUserForm from "./EditUserForm"; // Importamos el formulario de edición

const UserDataTable = ({ data, loading }) => {
  const [message, setMessage] = useState(""); // Mensaje de éxito o error
  const [editingUserId, setEditingUserId] = useState(null); // ID del usuario que se está editando
  const [showEditModal, setShowEditModal] = useState(false); // Para controlar la visibilidad del modal de edición
  const sesion = localStorage.getItem("accessToken"); // Obtener el token o ID del usuario logueado

  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name,
      sortable: true,
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => handleEdit(row)} // Llamamos a la función de editar
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row)} // Llamamos a la función de eliminar
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Función para eliminar un usuario
  const handleDelete = (user) => {
    // Verificar si el usuario logueado está intentando eliminarse a sí mismo
    if (user.id === sesion) {
      setMessage("No puedes eliminarte a ti mismo.");
      return;
    }

    // Confirmar la eliminación
    const isConfirmed = window.confirm(
      `¿Estás seguro de que quieres eliminar a ${user.name}?`
    );
    if (isConfirmed) {
      // Hacer la solicitud DELETE a la API para eliminar al usuario
      axios
        .delete(`http://127.0.0.1:8000/users/api/${user.id}/`, {
          headers: {
            Authorization: `Bearer ${sesion}`, // Pasar el token de acceso en los headers
          },
        })
        .then((response) => {
          setMessage(`Usuario ${user.name} eliminado correctamente.`);
        })
        .catch((error) => {
          setMessage(
            `Error al eliminar el usuario: ${
              error.response?.data?.detail || error.message
            }`
          );
        });
    }
  };

  // Función para manejar la edición
  const handleEdit = (user) => {
    setEditingUserId(user.id); // Establecemos el ID del usuario a editar
    setShowEditModal(true); // Mostramos el formulario de edición
  };

  // Función para cerrar el modal de edición
  const handleCloseEditModal = () => {
    setShowEditModal(false); // Cerramos el modal
  };

  // Función para actualizar la tabla después de editar
  const handleSaveEdit = () => {
    setShowEditModal(false); // Cerramos el modal
    // Aquí podrías hacer una llamada para recargar los datos si lo deseas
  };

  return (
    <div>
      <h3>Tabla de Usuarios</h3>
      {message && <div className="alert alert-info">{message}</div>}{" "}
      {/* Mostrar el mensaje */}
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
      {/* Mostrar el formulario de edición en un modal */}
      {showEditModal && (
        <EditUserForm
          userId={editingUserId}
          onClose={handleCloseEditModal}
          onSave={handleSaveEdit}
        />
      )}
    </div>
  );
};

export default UserDataTable;
