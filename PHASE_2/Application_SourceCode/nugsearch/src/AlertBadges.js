import React from 'react';
import './AlertBadges.css'
import { withRouter } from 'react-router-dom';

class AlertBadges extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            alerts: []
        };
    }

    componentDidMount() {
        let currAlert = this.props.match.params.alert;
        this.getAlerts(currAlert);
    }

    getAlerts(alert) {
        fetch('/getAlerts').then(res => res.json()).then(data => {
            var index = data.alerts.indexOf(alert);
            if (index !== -1) {
                data.alerts.splice(index, 1);
            }
            this.setState({alerts: data.alerts});
        })
    }

    componentWillReceiveProps(nextProps) {
        this.getAlerts(nextProps.match.params.alert);
    }

    navigateToPage = (event) => {
        this.props.history.push('/alerts/' + event.target.dataset.alertname);
        this.setState({alerts: []});
    }

    checkAlert(alert) {
        fetch('/checkAlert?alert=covid-19').then(res => res.json()).then(data => {
            return data.checkAlert;
        })
        return false;
    }

    AlertBadge(alert) {
        if (this.checkAlert(alert) == false) { // SHOULD BE TRUE, BUT WILL BE LEFT FALSE FOR DEMO (Alerts won't be shown as they check if average weekly cases are over '1' or latest case over '5')
            return (
                <div className="AlertBadge" key={alert} data-alertname={alert} onClick={this.navigateToPage}>
                    {alert.toUpperCase()}: POTENTIAL COVID-19 LOCKDOWN
                </div>
            );
        }
    }

    render() {
        return (
            <div className="AlertBadgeArea">
                {Object.keys(this.state.alerts).map((alert) => (
                    this.AlertBadge(this.state.alerts[alert])
                ))}
            </div>
        )
    }
}

export default withRouter(AlertBadges);