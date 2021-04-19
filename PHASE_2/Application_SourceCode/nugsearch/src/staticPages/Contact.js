import React from 'react'
import './Contact.css'
import { withRouter } from 'react-router-dom';
import nugLogo from '../images/nugSearchLogo300.png';

class Contact extends React.Component {

    render() {
        return (<div className="contact">
            <h1><img src={nugLogo} alt="logo" className="MediumLogo"/>Contact NugSearch</h1>
            <ul className="contactInfo">
                <li>We're third year Uni students at UNSW doing this for a group project</li>
                <li>Why would you need to contact us</li>
            </ul>
        </div>)
    }
}

export default withRouter(Contact);