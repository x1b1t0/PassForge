import React, { useState, useEffect } from 'react';
import api from '../services/api';

const PasswordManager = () => {
  const [passwords, setPasswords] = useState([]);
  const [newPassword, setNewPassword] = useState('');
  const token = localStorage.getItem('token');

  useEffect(() => {
    const fetchPasswords = async () => {
      try {
        const response = await api.getPasswords(token);
        setPasswords(response.data);
      } catch (error) {
        console.error('Failed to fetch passwords', error);
      }
    };
    fetchPasswords();
  }, [token]);

  const handleCreatePassword = async () => {
    try {
      await api.createPassword(token, 'user_id_placeholder', newPassword);
      setNewPassword('');
      const response = await api.getPasswords(token);
      setPasswords(response.data);
    } catch (error) {
      console.error('Failed to create password', error);
    }
  };

  const handleDeletePassword = async (userId) => {
    try {
      await api.deletePassword(token, userId);
      const response = await api.getPasswords(token);
      setPasswords(response.data);
    } catch (error) {
      console.error('Failed to delete password', error);
    }
  };

  return (
    <div>
      <h2>Password Manager</h2>
      <div>
        <input
          type="text"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
          placeholder="New Password"
        />
        <button onClick={handleCreatePassword}>Create Password</button>
      </div>
      <ul>
        {passwords.map((password) => (
          <li key={password.user_id}>
            {password.password}
            <button onClick={() => handleDeletePassword(password.user_id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PasswordManager;