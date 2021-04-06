import React from 'react'
import './Graph.css'

import graphImage from './Graph.PNG'


class Graph extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
        <div>
            <div className="ResultBackground">
                <h2>Graph: COVID19 Results in World Between 01/01/2021 and 01/04/2021</h2>
                <img src={graphImage} alt="img" class="GraphImage"/>
            </div>
        </div>
        )
    }
}

export default Graph;