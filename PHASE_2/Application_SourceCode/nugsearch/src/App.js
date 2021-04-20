import nugLogo from './images/nugSearchLogo300.png'
import Search from './search/Search.js'
import Alert from './alerts/Alert.js'
import AlertBadges from './alerts/AlertBadges.js'
import Map from './search/results/Map.js'
import Graph from './search/results/Graph.js'
import ResultsTable from './search/results/ResultsTable.js'
import About from './staticPages/About.js'
import Contact from './staticPages/Contact.js'
import Signup from './signup/Signup.js'
import SignupFinish from './signup/SignupFinish.js'
import SignupRemove from './signup/SignupRemove.js'
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
              <Link to="/">
              <p className="NavBarLi"><img src={nugLogo} alt="logo" className="SmallLogo"/></p>
              <p className="NavBarLi LogoText" >NugSearch</p>
              </Link>
              <li className="NavBarLi"><Link to="/">Search</Link></li>
              <li className="NavBarLi"><Link to="/about">About</Link></li>
              <li className="NavBarLi"><Link to="/contact">Contact</Link></li>
              <li className="NavBarLi"><Link to="/signup">Sign up to alerts</Link></li>
              {/*<li className="NavBarLi"><Link to="/alerts/default">Alerts</Link></li>
              <li className="NavBarLi"><Link to="/map">Map</Link></li>
              <li className="NavBarLi"><Link to="/graph">Graph</Link></li>*/}
            </ul>
          </nav>

          <Switch>
            <Route path="/about">
              <AlertBadges />
              <About />
            </Route>
            <Route path="/contact">
              <AlertBadges />
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
              <Map date={new Date()} ulocation="Melbourne, Aus"/>
            </Route>
            <Route path="/graph">
              <Graph />
            </Route>
            <Route path="/signupFinish">
              <AlertBadges />
              <SignupFinish />
            </Route>
            <Route path="/signupRemove">
              <AlertBadges />
              <SignupRemove />
            </Route>
            <Route path="/signup">
              <AlertBadges />
              <Signup />
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