// src/api/api.js
import axios from 'axios';

const baseURL = 'http://localhost:8000'; // Update with your Django backend URL

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 5000, // Timeout after 5 seconds
  headers: {
    'Content-Type': 'application/json'
  }
});

// Function to get the access token from local storage
const getAccessToken = () => localStorage.getItem('access_token');

// Function to get the refresh token from local storage
const getRefreshToken = () => localStorage.getItem('refresh_token');

// Function to save tokens to local storage
const saveTokens = (access_token, refresh_token) => {
  localStorage.setItem('access_token', access_token);
  localStorage.setItem('refresh_token', refresh_token);
};

// Add a request interceptor to add JWT token to headers
axiosInstance.interceptors.request.use(
  (config) => {
    const token = getAccessToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Function to refresh the access token
const refreshToken = async () => {
  const refresh_token = getRefreshToken();
  if (refresh_token) {
    try {
      const response = await axios.post(`${baseURL}/auth/token/refresh/`, {
        refresh: refresh_token
      });
      const { access } = response.data;
      saveTokens(access, refresh_token);
      return access;
    } catch (error) {
      console.error('Failed to refresh token:', error);
      throw error;
    }
  } else {
    throw new Error('No refresh token available');
  }
};

// Add a response interceptor to handle token refreshing
axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const newAccessToken = await refreshToken();
        axios.defaults.headers.common['Authorization'] = `Bearer ${newAccessToken}`;
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
        return axiosInstance(originalRequest);
      } catch (refreshError) {
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
