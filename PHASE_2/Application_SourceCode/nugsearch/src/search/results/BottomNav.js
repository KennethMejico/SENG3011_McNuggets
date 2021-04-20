import React from 'react'
import { withRouter } from 'react-router-dom';
import './BottomNav.css'

class BottomNav extends React.Component {
    render() {
        return (<nav>
            <ul className="BottomNavBar">
                <li className="BottomNavBarLi">Table</li>
                <li className="BottomNavBarLi">Results</li>
                <li className="BottomNavBarLi">Map</li>
            </ul>
        </nav>)
    }
}

export default withRouter(BottomNav);