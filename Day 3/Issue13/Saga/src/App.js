import logo from './logo.svg';
import './App.css';
import { useAuth0 } from "@auth0/auth0-react";

function App() {

  const { loginWithRedirect, user, isAuthenticated, logout } = useAuth0();

  const handleSubmit = (event) => {
    event.preventDefault();
    loginWithRedirect();
  };

  return (
    <div className="App">
      <div className="login-container">
        {isAuthenticated ?
          <div className='maindiv'>
            <h3>Hello {user.name}</h3>
            <button className='logout' onClick={e => logout()}>Logout</button>
          </div> :
          <button type='submit' className="button-75" onClick={handleSubmit}>Login using OAuth!</button>}
      </div>
    </div>
  );
}

export default App;
