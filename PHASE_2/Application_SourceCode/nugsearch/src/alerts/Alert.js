import React from 'react'
import { withRouter } from 'react-router';
import './Alert.css'

class Alert extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            location: "",
            alertText: "",
            baseText0: "In the past, these numbers of cases has lead to lockdowns in Australia.",
            baseText1: "Based on statistics surrounding past cases and current cases in your area, it is possible for a lockdown to occur.",
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
        <div class="alertPage">
            <h1> COVID-19 Alert: {this.state.location.toUpperCase()} </h1>
            <p>{this.state.lastUpdateDate}</p>
            <div className="Background">
                <p className="AlertText">
                    {this.state.alertText}
                    <br></br><br></br>
                    {this.state.baseText0} {this.state.baseText1}
                    <br></br><br></br>
                    Please be cautious and plan accordingly - further restrictions may be enforced in upcoming days.
                    <br></br><br></br>
                    <h3>Common COVID-19 symptoms:</h3>
                    <li>fever</li>
                    <li>dry cough</li>
                    <li>tiredness</li>
                    <h3>Less common symptoms:</h3>
                    <li>aches and pains</li>
                    <li>sore throat</li>
                    <li>diarrhoea</li>
                    <li>conjunctivitis</li>
                    <li>headache</li>
                    <li>loss of taste or smell</li>
                    <li>a rash on skin, or discolouration of fingers or toes</li>
                    <h3>Serious symptoms:</h3>
                    <li>difficulty breathing or shortness of breath</li>
                    <li>chest pain or pressure</li>
                    <li>loss of speech or movement</li>
                    <br></br><br></br>
                    Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility.
                    People with mild symptoms who are otherwise healthy should manage their symptoms at home.
                    On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.
                    <br></br><br></br>
                    Further information and announcements may be found here: <a href={this.state.govText} rel="noreferrer">{this.state.govText}</a>
                </p>
            </div>
        </div>
        )
    }
}

export default withRouter(Alert);