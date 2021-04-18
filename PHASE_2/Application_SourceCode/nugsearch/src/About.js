import React from 'react'
import './About.css'
import { withRouter } from 'react-router-dom';
import nugLogo from './nugSearchLogo300.png';

class About extends React.Component {

    render() {
        return (<div className="about">
            <h1><img src={nugLogo} alt="logo" className="MediumLogo"/>All About NugSearch</h1>
            <ul className="facts">
                <li>created by a brave team of UNSW students known as the McNuggets.</li>
                <li>designed as a one stop shop for information about emerging and ongoing epidemics</li>
                <li>search for diseases of interest</li>
                <li>receive advance warning of possible lockdowns based on growing numbers of cases</li>
            </ul>
        </div>)
    }
}

export default withRouter(About);