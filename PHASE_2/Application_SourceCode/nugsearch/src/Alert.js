import React from 'react'
import { withRouter } from 'react-router';
import './Alert.css'

class Alert extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            location: "",
            alertText: "",
            baseText0: "In the past, this amount of cases has lead to a lockdown in your area. Be prepared for another to happen again. COVID-19 has caused lockdowns to happen way too many times in total.",
            baseText1: "February 12, 2021, it was announced that a five-day lockdown under Stage 4 restrictions would take effect beginning at 11:59 pm. AEDT, due to a cluster of 13 cases tied to a Holiday Inn quarantine hotel near Melbourne Airport, which have been assumed to be the UK variant. Based on statistics surrounding these cases and current cases in your area, it is possible for a lockdown and further restrictions to occur.",
            govText: "",
            lastUpdateDate: ""
        }
    }

    setAlertText = (text) => {
        this.setState({
            alertText: text
        })
    }

    componentDidMount() {
        this.createAlertText(this.props.match.params.alert);
    }

    createAlertText(alert) {
        fetch('/getAlertData?location=' + alert).then(res => res.json()).then(data => {
            this.setAlertText("There were " + data.latest + " local cases of COVID-19 in " + data.location.toUpperCase() + " today, with a weekly average of " + data.average + " cases.");
            this.setState({
                location: data.location,
                lastUpdateDate: data.time,
                govText: "https://www." + data.location + ".gov.au/"
            })
        });
    }

    componentWillReceiveProps(nextProps) {
        this.createAlertText(nextProps.match.params.alert);
    }

    render() {
        return(
        <div class="page">
            <h1> COVID-19 Alert: {this.state.location.toUpperCase()} </h1>
            <p>{this.state.lastUpdateDate}</p>
            <div className="Background">
                <p className="AlertText">{this.state.alertText}</p>
                <p className="AlertText">{this.state.baseText0}</p>
                <p className="AlertText">{this.state.baseText1}</p>
                <p className="AlertText">Further information and announcements may be found here: <a href={this.state.govText} rel="noreferrer">{this.state.govText}</a>
                </p>
            </div>
        </div>
        )
    }
}

export default withRouter(Alert);