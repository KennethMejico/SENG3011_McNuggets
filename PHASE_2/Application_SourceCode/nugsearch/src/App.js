import nugLogo from './nugSearchLogo300.png'
import Search from './Search.js'
import Alert from './Alert.js'
import AlertBadges from './AlertBadges.js'
import Map from './Map.js'
import Graph from './Graph.js'
import ResultsTable from './ResultsTable.js'
import About from './About.js'
import Contact from './Contact.js'
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <div>
          <nav>
            <ul className="NavBar">
              <p className="NavBarLi"><img src={nugLogo} alt="logo" className="SmallLogo"/></p>
              <p className="NavBarLi LogoText">NugSearch</p>
              <li className="NavBarLi"><Link to="/">Home</Link></li>
              <li className="NavBarLi"><Link to="/about">About</Link></li>
              <li className="NavBarLi"><Link to="/contact">Contact</Link></li>
              {/*<li className="NavBarLi"><Link to="/alerts/default">Alerts</Link></li>
              <li className="NavBarLi"><Link to="/map">Map</Link></li>
              <li className="NavBarLi"><Link to="/graph">Graph</Link></li>*/}
            </ul>
          </nav>

          <Switch>
            <Route path="/about">
              <About />
            </Route>
            <Route path="/contact">
              <Contact />
            </Route>
            <Route path="/alerts/:alert">
              <AlertBadges />
              <Alerts />
            </Route>
            <Route path="/results">
              <ResultsTable />
            </Route>
            <Route path="/map">
              <Map />
            </Route>
            <Route path="/graph">
              <Graph />
            </Route>
            <Route path="/">
              <AlertBadges />
              <Home />
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

function Home() {
  return <Search />;
}

function Alerts() {
  return <Alert />;
}

export default App;
