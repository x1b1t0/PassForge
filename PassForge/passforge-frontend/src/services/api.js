import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

const register = (username, email, password) => {
  return axios.post(`${API_URL}/register`, {
    username,
    email,
    password
  });
};

const login = (username, password) => {
  return axios.post(`${API_URL}/login`, {
    username,
    password
  });
};

const getPasswords = (token) => {
  return axios.get(`${API_URL}/passwords`, {
    headers: {
      'x-access-token': token
    }
  });
};

const createPassword = (token, userId, password) => {
  return axios.post(`${API_URL}/passwords`, {
    user_id: userId,
    password
  }, {
    headers: {
      'x-access-token': token
    }
  });
};

const updatePassword = (token, userId, password) => {
  return axios.put(`${API_URL}/passwords/${userId}`, {
    password
  }, {
    headers: {
      'x-access-token': token
    }
  });
};

const deletePassword = (token, userId) => {
  return axios.delete(`${API_URL}/passwords/${userId}`, {
    headers: {
      'x-access-token': token
    }
  });
};

export default {
  register,
  login,
  getPasswords,
  createPassword,
  updatePassword,
  deletePassword
};