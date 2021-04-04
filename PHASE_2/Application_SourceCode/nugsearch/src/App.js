import nugLogo from './nugSearchLogo300.png'
import Search from './Search.js'
import Alert from './Alert.js'
import './App.css';

function App() {
  return (
    <div className="App">
      <div>
        <ul className="NavBar">
          <li className="NavBarLi"><img src={nugLogo} alt="logo" className="SmallLogo"/></li>
          <li className="NavBarLi LogoText">NugSearch</li>
          <li className="NavBarLi"><a href="default.asp">Home</a></li>
          <li className="NavBarLi"><a href="about.asp">About</a></li>
          <li className="NavBarLi"><a href="contact.asp">Contact</a></li>
          <li className="NavBarLi"><a href="news.asp">Alerts</a></li>
        </ul>
      </div>
      <Alert />
    </div>
  );
}

export default App;
