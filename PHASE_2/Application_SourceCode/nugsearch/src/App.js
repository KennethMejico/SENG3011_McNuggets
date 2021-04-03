import logo from './logo.svg';
import nugLogo from './nugSearchLogo300.png'
import Search from './Search.js'
import './App.css';

function App() {
  return (
    <div className="App">
      <div>
        <ul className="NavBar">
          <li className="NavBarLi"><img src={nugLogo} alt="logo" className="SmallLogo"/></li>
          <li className="NavBarLi LogoText">NugSearch</li>
          <li className="NavBarLi"><a href="default.asp">Home</a></li>
          <li className="NavBarLi"><a href="news.asp">About</a></li>
          <li className="NavBarLi"><a href="contact.asp">Contact</a></li>
          <li className="NavBarLi"><a href="about.asp">Alerts</a></li>
        </ul>
      </div>
      <Search />
    </div>
  );
}

export default App;
