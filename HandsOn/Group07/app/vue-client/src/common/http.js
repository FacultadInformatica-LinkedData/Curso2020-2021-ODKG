import axios from "axios";

const HTTP = axios.create({
  baseURL: "http://localhost:8080/"
});

const onResponseSuccess = response => response;

// si el servidor nos devuelve un 401 o 403,
// estamos intentando acceder a un recurso sin
// los permisos correctos
const onResponseFailure = err => {
  return Promise.reject(err);
};

// en cada request hay que añadir el token de autenticación
// si es que lo tenemos
const onRequest = config => {
  return config;
};

HTTP.interceptors.response.use(onResponseSuccess, onResponseFailure);
HTTP.interceptors.request.use(onRequest);

export default HTTP;
