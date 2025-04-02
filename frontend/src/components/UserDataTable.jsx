import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";
import Swal from "sweetalert2"; // Para mostrar los mensajes de confirmación
import { Modal, Button, Form } from 'react-bootstrap'; // Importar el modal y los componentes necesarios

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga
  const [selectedUser, setSelectedUser] = useState(null); // Para manejar el usuario seleccionado para editar
  const [showModal, setShowModal] = useState(false); // Para controlar si el modal está abierto
  const [formData, setFormData] = useState({
    id: '',
    email: '',
    name: '',
    surname: '',
    control_number: '',
    age: '',
    tel: '',
  });

  const accessToken = localStorage.getItem("accessToken");
  const refreshToken = localStorage.getItem("refreshToken");

  // Configuración de columnas
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
            onClick={() => handleEdit(row)} // Llamar a la función de edición
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row)} // Llamar a la función de eliminar
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Obtener datos desde la API
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);;

  // Función para refrescar el token si ha expirado
  const refreshAccessToken = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/users/token/refresh/", {
        refresh: refreshToken,
      });
      localStorage.setItem("accessToken", response.data.access);
      return response.data.access;
    } catch (error) {
      console.error("Error al refrescar el token:", error);
      return null;
    }
  };

  // Función para borrar un usuario
  const handleDelete = (user) => {
    if (user.id === 1) { // Suponiendo que el usuario logueado tiene el id 1, esto es solo un ejemplo.
      Swal.fire("Error", "No puedes eliminarte a ti mismo.", "error");
      return;
    }

    Swal.fire({
      title: "¿Estás seguro?",
      text: `Quieres eliminar al usuario ${user.name}?`,
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sí, eliminar",
      cancelButtonText: "Cancelar",
    }).then((result) => {
      if (result.isConfirmed) {
        axios
          .delete(`http://127.0.0.1:8000/users/api/${user.id}/`, {
            headers: { Authorization: `Bearer ${accessToken}` },
          })
          .then((response) => {
            Swal.fire("Eliminado", "Usuario eliminado correctamente", "success");
            // Volver a cargar los datos
            setData(data.filter((u) => u.id !== user.id));
          })
          .catch(async (error) => {
            if (error.response && error.response.status === 401) {
              // Si el token ha expirado, refrescarlo
              const newToken = await refreshAccessToken();
              if (newToken) {
                // Intentar eliminar de nuevo con el nuevo token
                handleDelete(user); // Llamar a la función nuevamente
              } else {
                Swal.fire("Error", "No se pudo autenticar. Inicia sesión nuevamente.", "error");
              }
            } else {
              Swal.fire("Error", "No se pudo eliminar al usuario", "error");
            }
          });
      }
    });
  };

  // Función para editar un usuario
  const handleEdit = (user) => {
    setSelectedUser(user); // Guarda el usuario seleccionado para la edición
    setFormData({ name: user.name, email: user.email, tel: user.tel, surname:user.surname,control_number: user.control_number, age:user.age }); // Pre-pobla el formulario con los datos
    setShowModal(true); // Abre el modal
  };

  // Función para manejar el cambio en el formulario de edición
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  // Función para guardar los cambios
  const handleSaveChanges = async () => {
    if (!accessToken) {
      Swal.fire("Error", "No tienes permiso para actualizar el usuario", "error");
      return;
    }

    try {
      const response = await axios.put(
        `http://127.0.0.1:8000/users/api/${selectedUser.id}/`,
        formData,
        { headers: { Authorization: `Bearer ${accessToken}` } }
      );

      Swal.fire("Actualizado", "Usuario actualizado correctamente", "success");
      setData((prevData) =>
        prevData.map((user) => (user.id === selectedUser.id ? response.data : user))
      );

      setShowModal(false); // Cerrar el modal
    } catch (error) {
      if (error.response && error.response.status === 401) {
        // Si el token ha expirado, refrescarlo
        const newToken = await refreshAccessToken();
        if (newToken) {
          // Intentar actualizar de nuevo con el nuevo token
          handleSaveChanges();
        } else {
          Swal.fire("Error", "No se pudo autenticar. Inicia sesión nuevamente.", "error");
        }
      } else {
        Swal.fire("Error", "No se pudo actualizar el usuario", "error");
      }
    }
  };

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />

      {/* Modal para editar el usuario */}
      <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Editar Usuario</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group className="mb-3" controlId="formName">
              <Form.Label>Nombre</Form.Label>
              <Form.Control
                type="text"
                placeholder="Ingrese el nombre"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formSurname">
              <Form.Label>Apellido</Form.Label>
              <Form.Control
                type="text"
                placeholder="Ingrese el apellido"
                name="surname"
                value={formData.surname}
                onChange={handleInputChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formControlNumber">
              <Form.Label>Número de Control</Form.Label>
              <Form.Control
                type="text"
                placeholder="Ingrese el número de control"
                name="control_number"
                value={formData.control_number}
                onChange={handleInputChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formAge">
              <Form.Label>Edad</Form.Label>
              <Form.Control
                type="number"
                placeholder="Ingrese la edad"
                name="age"
                value={formData.age}
                onChange={handleInputChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formTel">
              <Form.Label>Teléfono</Form.Label>
              <Form.Control
                type="text"
                placeholder="Ingrese el teléfono"
                name="tel"
                value={formData.tel}
                onChange={handleInputChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                placeholder="Ingrese el email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowModal(false)}>
            Cancelar
          </Button>
          <Button variant="primary" onClick={handleSaveChanges}>
            Guardar Cambios
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default UserDataTable;





/* import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios"; // Si deseas obtener datos desde una API

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
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
            onClick={() => alert(`Editando ${row.name}`)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => alert(`Editando ${row.name}`)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Obtener datos desde una API (puedes cambiar esta parte)
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
    </div>
  );
};

export default UserDataTable;
 */