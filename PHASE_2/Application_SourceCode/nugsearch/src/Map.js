import React from 'react'
import './Map.css'

import mapImage from './Map.PNG'
import { withRouter } from 'react-router-dom';


class Map extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
        <div>
            <div className="ResultBackground">
                <h2>Map: COVID19 Results in World Between 01/01/2021 and 01/04/2021</h2>
                <img src={mapImage} alt="img" className="ResultImage"/>
                <p />
                <a href="/graph">See Graph</a>
            </div>
        </div>
        )
    }
}

export default withRouter(Map);
