import React from 'react'
import { withRouter, Link } from 'react-router-dom';
import './BottomNav.css'

class BottomNav extends React.Component {
    render() {
        return (<nav>
            <ul className="BottomNavBar">
                <li className="BottomNavBarLi"><Link to={{
                    pathname: '/results',
                    state: {
                        data: this.props.location.state.data,
                        startDate: this.props.location.state.startDate,
                        endDate: this.props.location.state.endDate,
                    }
                }}>See Table</Link></li>
                <li className="BottomNavBarLi"><Link to={{
                    pathname: '/graph',
                    state: {
                        data: this.props.location.state.data,
                        startDate: this.props.location.state.startDate,
                        endDate: this.props.location.state.endDate,
                    }
                }}>See Graph</Link></li>
                <li className="BottomNavBarLi"><Link to={{
                    pathname: '/map',
                    state: {
                        data: this.props.location.state.data,
                        startDate: this.props.location.state.startDate,
                        endDate: this.props.location.state.endDate,
                    }
                }}>See Map</Link></li>
            </ul>
        </nav>)
    }
}

export default withRouter(BottomNav);