import React from 'react'
import './About.css'
import { withRouter } from 'react-router-dom';
import nugLogo from './nugSearchLogo300.png';

class About extends React.Component {

    render() {
        return (<div className="about">
            <h1><img src={nugLogo} alt="logo" className="MediumLogo"/>All About NugSearch</h1>
            <ul className="facts">
                <li>Created by a brave team of UNSW students known as the McNuggets.</li>
                <li>Designed as a one stop shop for information about emerging and ongoing epidemics</li>
                <li>Search for diseases of interest</li>
                <li>Receive advance warning of possible lockdowns based on growing numbers of cases</li>
                <li>Data sourced from <a href="https://promedmail.org/">Program for Monitoring Emerging Diseases (ProMED)</a></li>
                <li>All data is updated daily</li>
            </ul>
        </div>)
    }
}

export default withRouter(About);