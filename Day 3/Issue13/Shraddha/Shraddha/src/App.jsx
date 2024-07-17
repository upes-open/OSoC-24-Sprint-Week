import React from 'react';
import { useAuth0 } from "@auth0/auth0-react";

function App() {
  const { user, loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return (
    <div className='App'>
      <div className='login'>
        {isAuthenticated ? (
          <div>
            <p>Welcome, {user?.name}</p>
            <button onClick={() => logout({ returnTo: window.location.origin })}>Logout</button>
          </div>
        ) : (
          <div>
            <input type="email" placeholder="Enter email" name="email" />
            <input type="password" placeholder="Enter password" name="password" />
            <button onClick={() => loginWithRedirect()}>Login</button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
