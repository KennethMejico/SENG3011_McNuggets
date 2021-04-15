import React from 'react'
import './Map.css'

import mapImage from './Map.PNG'
import { withRouter, Link } from 'react-router-dom';


class Map extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
    }

    render() {
        return(
        <div>
            <div className="ResultBackground">
                <h2>Map: COVID19 Results in World Between {this.props.location.state.startDate} and {this.props.location.state.endDate}</h2>
                <img src={mapImage} alt="img" className="ResultImage"/>
                <p />
                <Link to={{
                    pathname: '/graph',
                    state: { 
                        data: this.props.location.state.data,
                        startDate: this.props.location.state.startDate,
                        endDate: this.props.location.state.endDate, 
                    }
                }}>See Graph</Link>
            </div>
        </div>
        )
    }
}

export default withRouter(Map);
