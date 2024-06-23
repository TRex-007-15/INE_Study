// authe_reducer.js

// Initial state
export const initialState = {
    isAuthenticated: false,
    user: null,
    error: null,
  };
  
  // Action types
  export const actionTypes = {
    LOGIN_SUCCESS: 'LOGIN_SUCCESS',
    LOGIN_FAILURE: 'LOGIN_FAILURE',
    LOGOUT: 'LOGOUT',
  };
  
  // Reducer function
  const authe_reducer = (state, action) => {
    switch (action.type) {
      case actionTypes.LOGIN_SUCCESS:
        return {
          ...state,
          isAuthenticated: true,
          user: action.payload.user,
          error: null,
        };
      case actionTypes.LOGIN_FAILURE:
        return {
          ...state,
          isAuthenticated: false,
          user: null,
          error: action.payload.error,
        };
      case actionTypes.LOGOUT:
        return {
          ...state,
          isAuthenticated: false,
          user: null,
          error: null,
        };
      default:
        return state;
    }
  };
  
  export default authe_reducer;
  