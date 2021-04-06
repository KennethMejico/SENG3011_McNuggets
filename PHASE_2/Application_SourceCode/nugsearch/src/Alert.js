import React from 'react'
import './Alert.css'

//import alertImg from './Health-alert.png'

//                <img src={covidImg} alt="img" class="CovidImage"/>

class Alert extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            alertTitle: "",
            alertText: ""
        }

        fetch('/getAlerts').then(res => res.json()).then(data => {
            if (data.alerts.length === 0) {
                this.setState({alertTitle: "None"});
                /*this.state = {
                    alertTitle: "None",
                    alertText: "No lockdowns seem imminent"
                }*/
            }
            else {
                fetch("/getAlertDescription?name=" + data.alerts[0])
                .then(res => res.json())
                .then(data => {
                    this.setState({
                        alertTitle: data.title,
                        alertText: data.text
                    })
                    /*this.state = {
                        alertTitle: data.title,
                        alertText: data.text
                    }*/
                });
            }
        });
    }

    render() {
        return(
        <div>
            <div className="Background">
                <h1 className="Heading">Alert: {this.state.alertTitle}</h1>
                <p className="AlertText">{this.state.alertText}</p>
            </div>
        </div>
        )
    }
}
/*
            <div className="OtherAlerts">
                <div className="Divider"></div>
                <h2 className="OtherHeading"> Other Alerts </h2>
                <div className="row">
                    <div className="column">
                        <img src={alertImg} alt="alert1" className="Alert1" style={{ width: '80%' }}/>
                    </div>
                    <div className="column">
                        <img src={alertImg} alt="alert2" className="Alert2" style={{ width: '80%' }}/>
                    </div>
                    <div className="column">
                        <img src={alertImg} alt="alert3" className="Alert3" style={{ width: '80%' }}/>
                    </div>
                </div>
            </div>
*/

export default Alert;