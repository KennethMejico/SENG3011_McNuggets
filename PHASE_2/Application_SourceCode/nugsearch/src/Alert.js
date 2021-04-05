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
There were 17 cases of COVID-19 in Sydney on 10/04/2021.

In the past, this amount of cases has lead to a lockdown in your area. Be prepared for another to happen again.

COVID-19 has caused a lockdown in your area THREE times before. COVID-19 has caused lockdowns to happen way too many times in total.

The last COVID-19 lockdown happened after 15 cases were reported in a day.

See government alerts for your area: https://www.nsw.gov.au/
*/
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