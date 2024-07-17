import React from 'react'
import ReactDOM from 'react-dom/client'
import { createRoot } from 'react-dom/client';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
   <Auth0Provider
    // domain="" the domain from your OAuth dashboard
    // clientId="" here goes the clientID from your dev environment
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
   >
    <App />
  </Auth0Provider>
  </React.StrictMode>
)


